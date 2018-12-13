from app.db import db
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