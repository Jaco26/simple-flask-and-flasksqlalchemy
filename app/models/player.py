from app.db import db

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

  def save_to_db(self):
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

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
