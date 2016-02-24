from flask import render_template, redirect, flash
from app import app, db
from .models import Task, Goal
from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField

class TaskAddForm(Form):
  goal_choices = [(g.id, g.title) for g in Goal.query.all()]
  goal_choices.insert(0, ("0", "Pick a goal"))
  title = StringField('title')
  goal_id = SelectField('goals', coerce=int, choices = goal_choices)

class GoalAddForm(Form):
  title = StringField('title')
  target = IntegerField('target')

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.filter_by(deleted_at=None).all()
    goals = Goal.query.filter_by(deleted_at=None).all()
    taf = TaskAddForm()

    return render_template('index.html', title="Tasks", tasks=tasks, goals=goals,
                            taskForm = taf, goalForm = GoalAddForm())


@app.route('/task/add', methods=['POST', 'GET'])
def add_task():
  form = TaskAddForm()
  if form.validate_on_submit():
    print form.title.data
    newTask = Task(form.title.data)
    if form.goal_id != 0:
      print form.goal_id.data
      goalToAdd = Goal.query.get(form.goal_id.data)
      print goalToAdd
      newTask.goals.append(goalToAdd)
    db.session.add(newTask)
    db.session.commit()
    flash('"%s" was added' % newTask.title, 'success')
  else:
    print form.errors
    flash('The task could not be saved.', 'error')
  return redirect('/')

@app.route('/task/<int:task_id>/delete', methods=['POST', 'GET'])
def delete_task(task_id):
  task = Task.query.get(task_id)
  print task.title
  if task:
    task.delete()
    db.session.commit()
    flash('"%s" was deleted' % task.title, 'success')
  else:
    flash('There is no task with an ID of %s' % task_id, 'error')
  return redirect('/')

@app.route('/goal/add', methods=['POST', 'GET'])
def add_goal():
  form = GoalAddForm()
  if form.validate_on_submit():
    print form.title.data
    newGoal = Goal(form.title.data, target=form.target.data)
    flash('"%s" was added' % newGoal.title, 'success')
    db.session.add(newGoal)
    db.session.commit()
  else:
    flash('The task could not be saved.', 'error')
  return redirect('/')
