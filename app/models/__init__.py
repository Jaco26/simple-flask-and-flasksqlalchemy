from app.db import db
from sqlalchemy import and_
from datetime import datetime


class Game(db.Model):
  __tablename__ = 'game_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  status = db.Column(db.String, default="created")
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  date_started = db.Column(db.DateTime)
  date_finished = db.Column(db.DateTime)
  game_players = db.relationship('PlayerInstance', cascade="delete", backref='game')

  def json(self, *args):
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status,
      'date_created': datetime.isoformat(self.date_created) if self.date_created else None,
      'date_started': datetime.isoformat(self.date_started) if self.date_started else None,
      'date_finished': datetime.isoformat(self.date_finished) if self.date_started else None,
      'game_players': [p.json('player', 'role') for p in self.game_players] if 'game_players' in args else None
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
    # for p in self.game_players:
    #   self.game_players.remove(p)
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

  def json(self, *args):
    return {
      'id': self.id,
      'player': self.player.json() if 'player' in args else None,
      'game': self.game.json() if 'game' in args else None,
      'role': self.role.json() if self.role and 'role' in args else None,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  @classmethod
  def player_in_game(cls, player_id, game_id):
    print('player and game id', player_id, game_id)
    print(and_)
    return cls.query.filter(and_(cls.player_id == player_id, cls.game_id == game_id)).first()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()



class Player(db.Model):
  __tablename__ = 'player_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  player_instances = db.relationship('PlayerInstance', cascade='delete', backref='player')

  def json(self, *args):
    return {
      'id': self.id,
      'name': self.name,
      'player_instances': [p.json('game', 'role') for p in self.player_instances] if 'player_instances' in args else None
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
  role_players = db.relationship('PlayerInstance', cascade='delete', backref='role', lazy=True)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

