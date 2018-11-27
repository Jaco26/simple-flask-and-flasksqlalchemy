from flask_restful import Resource, reqparse
from game_api.models import Player, Game, PlayerInstance

def msg(message):
  return { 'message': message }

class JoinGame(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('player_id')

  def post(self, _id):
    try:
      data = JoinGame.parser.parse_args()
      game = Game.find_by_id(_id)
      player = Player.find_by_id(data['player_id'])
      player_in_game = PlayerInstance.player_in_game(player_id=data['player_id'], game_id=_id)
      print('player in game yes or no come on', player_in_game)
      if player_in_game:
        return msg('Player {} has already joined game {}'.format(data['player_id'], _id)), 200
      player_instance = PlayerInstance(player_id=data['player_id'], game_id=_id)
      player_instance.game = game
      player_instance.player = player
      player_instance.save()
      return msg('Player {} joined game {}'.format(data['player_id'], _id)), 201
    except:
      return msg('Player game join error'), 500

  