from flask_restful import Resource, reqparse
from app.models import Role, PlayerInstance

def msg(message):
  return { 'message': message }

class ChooseRole(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('player_id', type=int)
  parser.add_argument('role_id', type=int)

  def post(self, _id):
    try:
      data = ChooseRole.parser.parse_args()
      player_id = data['player_id']
      role_id = data['role_id']
      player_instance = PlayerInstance.player_in_game(player_id=player_id, game_id=_id)
      role = Role.find_by_id(role_id)
      if player_instance and role:
        player_instance.role_id = role_id
        player_instance.role = role
        player_instance.save()
        return msg('Player {} successfully chose adopted role {} for game {}.'.format(player_id, role_id, _id)), 201
      return msg('Could not find player_instance or role'), 404
    except:
      return msg('Error adopting role'), 500