from flask_restful import Resource, reqparse
from game_api.models import Player, Game

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
      if player in game.players:
        return msg('Player has already joined game'), 200
      game.players.append(player)
      game.save()
      # if GamePlayerRole.find_by_player_game(player_id=data['player_id'], game_id=_id):
      #   return msg('Player has already joined game'), 200
      # game_player = GamePlayerRole(game_id=_id, player_id=data['player_id'])
      # game_player.save()
      return msg('Player {} joined game {}'.format(data['player_id'], _id)), 201
    except:
      return msg('Player game join error'), 500

  