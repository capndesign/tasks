## A little preamble

Oh hi! You are here.

I’m building a little to-do app for myself because I want to learn a bunch of stuff about application development. And you have found it. Well done!

At any given point, this app may not work (at least, as long as you see this text).

## Installation

This is a Python app, powered by Flask and SQLite. So, you’ll need:

* a unix-y machine
* Python and pip
* virtualenv

There are "4" steps:

1. After you `git clone`, create a [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and `cd` into the root directory of the repo.
2. Run `pip install -r requirements.txt`.
3. Run `python ops/db_create.py` followed by `python ops/db_upgrade.py`.
4. `python run.py`.

## What it does

Ha. Right now, it lists your tasks, which you have to enter from a python shell.

In the meantime, I’m using Flask-SQLAlchemy and their [Quickstart guide](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/) plus a poke at the app’s models should get you started.

I’ll do my best to keep this up-to-date as I go forward.