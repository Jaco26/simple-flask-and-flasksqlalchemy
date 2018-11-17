import click
from flask import current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = db = SQLAlchemy()

@click.command('init-db')
@with_appcontext
def init_db_command():
  print(current_app)
  db.create_all()

class Person(db.Model):
  __tablename__ = 'person'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

