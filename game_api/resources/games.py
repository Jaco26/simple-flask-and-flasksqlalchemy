from flask_restful import Resource, reqparse
from game_api.models import Game, Player

def msg(message):
  return { 'message': message }

class GamesList(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name')
  parser.add_argument('status')
  parser.add_argument('date_started')
  parser.add_argument('date_finished')

  def get(self):
    try:
      games = [g.json() for g in Game.query.all()]
      return { 'games': games }, 200
    except:
      return msg('The was an error getting games'), 500

  def post(self):
    try:
      data = GamesList.parser.parse_args()
      if Game.find_by_name(data['name']):
        return msg('A game called "{}" already exists'.format(data['name'])), 400
      game = Game(**data)
      game.save()
      return msg('Game created!'), 201
    except:
      return msg('There was an error creating your game')


class GameById(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('player_id', type=int)

  def get(self, _id):
    try:
      game = Game.find_by_id(_id)
      return { 'game': game.json() }
    except :
      return msg('There was an error fetching the game'), 500

  def delete(self, _id):
    try:
      game = Game.find_by_id(_id)
      if game:
        game.delete()
        return msg('Game {} deleted'.format(_id)), 200
      else:
        return msg('Game {} was already gone'.format(_id)), 400
    except:
      return msg('Error deleting game'), 500
  
  def patch(self, _id):
    try:
      data = GameById.parser.parse_args()
      player = Player.find_by_id(data['player_id'])
      game = Game.find_by_id(_id)
      if player.id in [p.json()['id'] for p in game.players]:
        return msg('Player {} is already in game {}'.format(player_id, _id)), 200
      game.players.append(player)
      game.save()
      return msg('Player joined game {}'.format(_id)), 200
    except:
      return msg('Error with player joining game'), 500

