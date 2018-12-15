from flask_restful import Resource, reqparse
from app.models import PlayerCardDeck, InfectionCardDeck, Cities, Game

def msg(message):
  return { 'message': message }

class GameCitiesList(Resource):
  def get(self, _id):
    try:
      cities = [c.simple_json() for c in Cities.query.all()]
      return { 'cities': cities }
    except:
      return msg('Error getting all cities')


class CityById(Resource):
  def get(self, _id, city_id):
    try:
      city = Cities.find_by_id(city_id)
      return { 'city': city.simple_json() }
    except:
      return msg('Error getting all cities')

