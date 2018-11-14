from flask_sqlalchemy import SQLAlchemy


db = db = SQLAlchemy()

class Person(db.Model):
  __tablename__ = 'person'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

