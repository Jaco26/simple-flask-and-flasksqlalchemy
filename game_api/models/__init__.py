from game_api.db import db
from datetime import datetime


game_player_role = db.Table('game_player_role',
  db.Column('game_id', db.Integer, db.ForeignKey('games.id'), nullable=True),
  db.Column('player_id', db.Integer, db.ForeignKey('players.id'), nullable=True),
  db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), nullable=True),
)

class Game(db.Model):
  __tablename__ = 'games'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  status = db.Column(db.String, default="created")
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  date_started = db.Column(db.DateTime)
  date_finished = db.Column(db.DateTime)
  players = db.relationship('Player', secondary=game_player_role, lazy='subquery', backref=db.backref('player_games', lazy='dynamic'))


  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status,
      'date_created': datetime.isoformat(self.date_created)if self.date_created else None,
      'date_started': datetime.isoformat(self.date_started) if self.date_started else None,
      'date_finished': datetime.isoformat(self.date_finished) if self.date_started else None,
      'players': [p.json() for p in self.players]
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()





class Player(db.Model):
  __tablename__ = 'players'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)

  def json(self):
    return {
      'id': self.id,
      'name': self.name
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()




class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  description = db.Column(db.Text)

  
  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }

