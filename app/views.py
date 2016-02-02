from flask import render_template, redirect, flash
from app import app, db
from .models import Task
from flask_wtf import Form
from wtforms import StringField

class TaskAddForm(Form):
  title = StringField('title')

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.filter_by(deleted_at=None).all()
    return render_template('index.html', title="Tasks", tasks=tasks, form = TaskAddForm())


@app.route('/add-task', methods=['POST', 'GET'])
@app.route('/task/add', methods=['POST', 'GET'])
def add_task():
  form = TaskAddForm()
  if form.validate_on_submit():
    print form.title.data
    newTask = Task(form.title.data)
    flash('"%s" was added' % newTask.title, 'success')
    db.session.add(newTask)
    db.session.commit()
  else:
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