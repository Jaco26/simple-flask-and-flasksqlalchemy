import click
from flask import current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = db = SQLAlchemy()

@click.command('init-db')
@with_appcontext
def init_db_command():
  import app.models
  db.create_all()
  

@click.command('init-data')
@with_appcontext
def init_db_data():
  from app.initial_data import initial_roles
  for role in initial_roles:
    db.session.add(role)
    db.session.commit()

