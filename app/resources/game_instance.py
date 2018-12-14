from flask_restful import Resource, reqparse
from app.models import PlayerCardDeck, InfectionCardDeck, Cities, Game

def msg(message):
  return { 'message': message }

class GameCitiesList(Resource):
  def get(self):
    try:
      cities = Cities.query.all()
      return { 'cities': cities }
    except:
      return msg('Error getting all cities')