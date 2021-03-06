from app.db import db
from datetime import datetime

class GameInfectionDeck(db.Model):
  __tablename__ = 'game_infection_deck'

  id = db.Column(db.Integer, primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('game_info.id'))
  
  reshuffled_on_top = db.Column(db.ARRAY(db.Integer))
  current_discard_pile = db.Column(db.ARRAY(db.Integer))
  cards_removed_from_deck = db.Column(db.ARRAY(db.Integer))
  ts = db.Column(db.DateTime, default=datetime.utcnow)
  cards = db.relationship('InfectionCard', lazy='joined')

  def json(self):
    return {
      'id': self.id,
      'reshuffled_on_top': self.reshuffled_on_top,
      'current_discard_pile': self.current_discard_pile,
      'cards_removed_from_deck': self.cards_removed_from_deck,
      'ts': datetime.isoformat(self.ts),
      # 'cards': [card.id for card in self.cards]
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()


  

  


  
