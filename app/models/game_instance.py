from app.db import db

class GamePlayerDeck(db.Model):
  __tablename__ = 'game_player_deck'
  id = db.Column(db.Integer, primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('game_info.id'))
  cards_in_deck = db.Column(db.ARRAY(db.Integer))
  cards_in_hand = db.Column(db.ARRAY(db.Integer))
  cards_discarded = db.Column(db.ARRAY(db.Integer))

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()



class GameInfectionDeck(db.Model):
  __tablename__ = 'game_infection_deck'
  id = db.Column(db.Integer, primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('game_info.id'))
  cards_in_deck = db.Column(db.ARRAY(db.Integer))
  cards_discarded = db.Column(db.ARRAY(db.Integer))

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()



class GameCities(db.Model):
  __tablename__ = 'game_cities'
  id = db.Column(db.Integer, primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('game_info.id'))
  has_research_station = db.Column(db.ARRAY(db.Integer))
  uninfected = db.Column(db.ARRAY(db.Integer))
  i_one = db.Column(db.ARRAY(db.Integer))
  i_two = db.Column(db.ARRAY(db.Integer))
  i_three = db.Column(db.ARRAY(db.Integer))

  def json(self, *args):
    return {
      'id': self.id,
      'game_id': self.game_id,
      'has_research_station': self.has_research_station,
      'uninfected': self.uninfected,
      'i_one': self.i_one,
      'i_two': self.i_two,
      'i_three': self.i_three,
    }

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
