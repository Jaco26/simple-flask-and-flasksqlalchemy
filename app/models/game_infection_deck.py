from app.db import db

class GameInfectionDeck(db.Model):
  __tablename__ = 'game_infection_deck'

  id = db.Column(db.Integer, primary_key=True)
  reshuffled_on_top = db.Column(db.ARRAY, dimensions=2)
  current_discard_pile = db.Column(db.ARRAY)
  cards = db.relationship('InfectionCard', lazy='joined')

  
