from app import db
from datetime import datetime

goals = db.Table('goals_tasks',
    db.Column('goal_id', db.Integer, db.ForeignKey('goal.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
)

class Task(db.Model):
  id              = db.Column(db.Integer, primary_key=True)
  title           = db.Column(db.String(500), index=True, unique=True)
  repeats         = db.Column(db.String(32))
  timeframe       = db.Column(db.String(32))
  last_completed  = db.Column(db.DateTime)
  created_at      = db.Column(db.DateTime)
  archived_at     = db.Column(db.DateTime)
  deleted_at      = db.Column(db.DateTime)
  goals           = db.relationship('Goal', secondary=goals, backref=db.backref('tasks', lazy='dynamic'))
  completed_tasks = db.relationship('CompletedTask', backref='task', lazy='dynamic')


  def __init__(self, title, repeats=False, timeframe="sometime"):
    self.title = title
    self.repeats = repeats
    self.timeframe = timeframe
    self.created_at = datetime.utcnow()

  def __repr__(self):
    return '<Task %r>' % (self.title)

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