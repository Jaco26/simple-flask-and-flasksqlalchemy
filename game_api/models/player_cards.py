from game_api.db import db

class Game(db.Model):
  __tablename__ = 'game'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)


class Player(db.Model):
  __tablename__ = 'player'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)


class Role(db.Model):
  __tablename__ = 'role'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  description = db.Column(db.Text)


game_player = db.Table('game_player',
  db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
  db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
  db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
)


