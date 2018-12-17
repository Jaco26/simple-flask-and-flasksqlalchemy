from flask_restful import Resource, reqparse
from app.models import Player

def msg(message):
  return { 'message': message }

class PlayerList(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name', type=str)

  def get(self):
    try:
      return [player.json('player_instances') for player in Player.query.all()], 200
    except:
      return msg('The was an error getting all players'), 500

  def post(self):
    try:
      data = PlayerList.parser.parse_args()
      if Player.query.filter_by(name=data['name']).first():
        return msg('Player {} already exists!'.format(data['name'])), 400
      player = Player(**data)
      player.save_to_db()
      return msg('Player was saved!'), 201
    except:
      return msg('There was an error saving the player'), 500



class PlayerById(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name', type=str, required=True)

  def get(self, _id):
    player = Player.find_by_id(_id)
    if player:
      return player.json('player_instances'), 200
    return msg('Player {} not found'.format(_id)), 404
  
  def put(self, _id):
    try:
      data = PlayerById.parser.parse_args()
      if Player.find_by_name(*data):
        return msg('Player {} already exists. Please choose a different name'), 400
      player = Player.find_by_id(_id)
      if player:
        player.name = data['name']
        player.save_to_db()
        return player.json(), 201
      else:
        return msg('Player {} does not exist'.format(_id)), 400
    except:
      return msg('An error occured while updating player {}'.format(_id)), 500


  def delete(self, _id):
    player = Player.find_by_id(_id)
    if player:
      player.delete()
    return 'Player deleted', 200
    