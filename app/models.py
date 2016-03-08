from app import db
from datetime import datetime
import arrow

goals = db.Table('goals_tasks',
    db.Column('goal_id', db.Integer, db.ForeignKey('goal.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
)

class Task(db.Model):
  id                = db.Column(db.Integer, primary_key=True)
  title             = db.Column(db.String(500), index=True)
  repeat_interval   = db.Column(db.Integer)
  repeat_unit       = db.Column(db.String(32))
  last_completed    = db.Column(db.DateTime)
  created_at        = db.Column(db.DateTime)
  due_at            = db.Column(db.DateTime)
  archived_at       = db.Column(db.DateTime)
  deleted_at        = db.Column(db.DateTime)
  goals             = db.relationship('Goal', secondary=goals, backref=db.backref('tasks', lazy='dynamic'))
  completed_tasks   = db.relationship('CompletedTask', backref='task', lazy='dynamic')

  def __init__(self, title, repeat_interval=None, repeat_unit=None):
    self.title = title
    self.repeat_interval = repeat_interval
    self.repeat_unit = repeat_unit
    self.created_at = datetime.utcnow()

    # If the task repeats, set a due date.
    if repeat_unit and repeat_interval:
      kw = {repeat_unit : repeat_interval}
      arw = arrow.utcnow()
      arw = arw.replace(**kw)
      self.due_at = arw.datetime

  def __repr__(self):
    return '<Task %r>' % (self.title)

  def delete(self):
    self.deleted_at = datetime.utcnow()

class CompletedTask(db.Model):
  id              = db.Column(db.Integer, primary_key=True)
  completed_at    = db.Column(db.DateTime)
  task_id         = db.Column(db.Integer, db.ForeignKey('task.id'))

  def __init__(self, task):
    self.task_id = task.id
    self.completed_at = datetime.utcnow()

  def __repr__(self):
    task_title = Task.query.get(self.task_id).title
    return '<CompletedTask %r>' % (task_title)

class Goal(db.Model):
  id              = db.Column(db.Integer, primary_key=True)
  title           = db.Column(db.String(500), index=True, unique=True)
  description     = db.Column(db.String(5000))
  target          = db.Column(db.Integer)
  completed_by    = db.Column(db.DateTime)
  created_at      = db.Column(db.DateTime)
  archived_at     = db.Column(db.DateTime)
  deleted_at      = db.Column(db.DateTime)

  def __init__(self, title, description="", target=None, completed_by=None):
    self.title = title
    self.description = description
    self.target = target
    self.completed_by = completed_by
    self.created_at = datetime.utcnow()

  def __repr__(self):
    return '<Goal %r>' % (self.title)

  def completions_count(self):
    count = 0
    for task in self.tasks:
      if task.deleted_at == None:
        completed_tasks = CompletedTask.query.filter_by(task_id=task.id).all()
        count += len(completed_tasks)
    return count