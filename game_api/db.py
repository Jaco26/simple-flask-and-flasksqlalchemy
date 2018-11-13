import click
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g
from flask.cli import with_appcontext

db = db = SQLAlchemy()

class Person(db.Model):
  __tablename__ = 'person'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

