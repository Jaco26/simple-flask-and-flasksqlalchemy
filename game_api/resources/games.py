from flask_restful import Resource, reqparse
from game_api.models import Game

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

