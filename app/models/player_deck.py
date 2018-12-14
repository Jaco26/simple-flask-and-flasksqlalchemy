from app.db import db

class PlayerCardDeck(db.Model):
  __tablename__ = 'player_deck'

  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String())
  desciption = db.Column(db.String())

  def json(self, *args):
    return {
      'id': self.id,
      'category': self.category,
      'description': self.desciption,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

