from game_api.db import db
from datetime import datetime


class Game(db.Model):
  __tablename__ = 'game_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  status = db.Column(db.String, default="created")
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  date_started = db.Column(db.DateTime)
  date_finished = db.Column(db.DateTime)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status,
      'date_created': datetime.isoformat(self.date_created) if self.date_created else None,
      'date_started': datetime.isoformat(self.date_started) if self.date_started else None,
      'date_finished': datetime.isoformat(self.date_finished) if self.date_started else None,
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




class PlayerInstance(db.Model):
  # Each row in player_instance will have:
  # a relationship to a 'player' as defined in player_info,
  # a relationship to a 'game' as defined in game_info,
  # and a relationship to a 'role' as defined in role_info 
  __tablename__ = 'player_instance'

  id = db.Column(db.Integer, primary_key=True)
  player_id = db.Column(db.Integer, db.ForeignKey('player_info.id'))
  game_id = db.Column(db.Integer, db.ForeignKey('game_info.id'))
  role_id = db.Column(db.Integer, db.ForeignKey('role_info.id'))
  player = db.relationship('Player', uselist=False, backref='player_instances')
  game = db.relationship('Game', uselist=False, backref="game_players")
  role = db.relationship('Role', uselist=False)


  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()



class Player(db.Model):
  __tablename__ = 'player_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
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
  __tablename__ = 'role_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  description = db.Column(db.Text)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

