from flask import request
from flask_restful import Resource, reqparse

from app.models.infection_deck import InfectionCard
from app.models.game_instance import GameInfectionDeck
from app.models.game import Game

class ChangeGameInfectionDeck(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('cards_in_deck', type=list)
  parser.add_argument('cards_discarded', type=list)
  parser.add_argument('new_game', type=bool, location='args')

  def post(self, _id):
    '''add an infection card deck to a game'''
    data = self.parser.parse_args()
    if data['new_game'] == 'true':
      card_ids = [card.id for card in InfectionCard.query.all()]
      game_infection_deck = GameInfectionDeck(game_id=_id, cards_in_deck=card_ids)
      game_infection_deck.save_to_db()
      return 'added', 201
    


