from flask import render_template
from app import app, db
from .models import Task

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', title="Tasks", tasks=tasks)