from flask_restful import Resource, reqparse
from game_api.models import Player, Role, Game

class ChooseRole(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('player_id', type=int)
  parser.add_argument('role_id', type=int)

  def post(self, _id):
    try:
      data = ChooseRole.parser.parse_args()
      game = Game.find_by_id(_id)
      player = Player.find_by_id(data['player_id'])
      role = Role.find_by_id(data['role_id'])
      
    except:
      pass