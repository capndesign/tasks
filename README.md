## A little preamble

Oh hi! You are here.

I’m building a little to-do app for myself because I want to learn a bunch of stuff about application development. And you have found it. Well done!

At any given point, this app may not work (at least, as long as you see this text).

## Installation

This is a Python app, powered by Flask and SQLite. So, you’ll need:

* a unix-y machine
* Python and pip
* virtualenv

There are "6" steps:

1. After you `git clone`, create a [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and `cd` into the root directory of the repo.
2. Run `pip install -r requirements.txt`.
3. Run `python ops/db_create.py` followed by `python ops/db_upgrade.py`.
4. Run `npm install -g gulp`.
5. Run `npm install` followed by `gulp`.
6. `python run.py`.

## What it does

Right now, it lists your tasks and goals.

## Resources

I’m learning a lot of new stuff while doing this. Here’s what I’ve been looking at throughout the process.

* Miguel Grinberg’s [Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Explore Flask](https://exploreflask.com/index.html)
* [Flask-SQLAlchemy’s Quickstart guide](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/)
* [Getting started with gulp](https://markgoodyear.com/2014/01/getting-started-with-gulp/)