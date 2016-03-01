from flask import render_template, redirect, flash
from datetime import datetime
from app import app, db
from .models import Task, Goal, CompletedTask
from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField

# Having these forms up top breaks db creation/updates
# TODO: Fix it.
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

    return render_template('index.html', title="Tasks", tasks=tasks, goals=goals,
                            taskForm = TaskAddForm(), goalForm = GoalAddForm())


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

@app.route('/task/<int:task_id>/complete', methods=['POST', 'GET'])
def complete_task(task_id):
  task = Task.query.get(task_id)
  print task.title
  if task:
    newCompletion = CompletedTask(task)
    db.session.add(newCompletion)

    task.last_completed = datetime.utcnow()
    if not task.repeat_interval:
      task.archived_at = datetime.utcnow()

    db.session.commit()
    flash('"%s" was completed' % task.title, 'success')
  else:
    flash('There is no task with an ID of %s' % task_id, 'error')
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
