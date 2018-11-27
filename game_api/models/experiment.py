from game_api.db import db


class GameInfo(db.Model):
  __tablename__ = 'game_info'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()



class RoleInfo(db.Model):
  __tablename__ = 'role_info'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()



class PlayerInfo(db.Model):
  __tablename__ = 'player_info'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()



class PlayerInstance(db.Model):
  # Each row in player_instance will have:
  # a relationship to a 'player' as defined in player_info,
  # a relationship to a 'game' as defined in game_info,
  # and a relationship to a 'role' as defined in role_info 
  __tablename__ = 'player_instance'

  id = db.Column(db.Integer, primary_key=True)
  player = db.relationship('PlayerInfo', uselist=False, backref='player_instances')
  game = db.relationship('GameInfo', uselist=False, backref="game_players")
  role = db.relationship('RoleInfo', uselist=False)


  def json(self):
    return {
      'id': self.id,
      'name': self.name,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()