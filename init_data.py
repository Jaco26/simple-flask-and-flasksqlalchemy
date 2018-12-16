from pprint import pprint
from app.db import db
from app import create_app
from app.calculations.find_city_connections import connect_cities
from app.models.cities import Cities
from app.models.infection_deck import InfectionCard


class OldCities(db.Model):
  __bind_key__ = 'old_cities'
  __tablename__ = 'old_cities'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  x_rat_key = db.Column(db.Integer) # used to determine width of html5 canvas
  y_rat_key = db.Column(db.Integer) # used to determine width of html5 canvas
  x_rat = db.Column(db.Float(precision=2)) # used to position "city dot" on html5 canvas
  y_rat = db.Column(db.Float(precision=2)) # used to position "city dot" on html5 canvas
  color = db.Column(db.String)
  connections = db.Column(db.JSON())

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'x_rat_key': self.x_rat_key,
      'y_rat_key': self.y_rat_key,
      'x_rat': self.x_rat,
      'y_rat': self.y_rat,
      'color': self.color,
      'connections': self.connections
    }
  
  def simple_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'connections': self.connections
    }



def move_cities():
  cities = [c.json() for c in OldCities.query.all()]
  for city in cities:
    c = connect_cities(city, cities)
    new_city = Cities(**c)
    if not Cities.query.filter_by(name=new_city.name).first():
      new_city.save_to_db()

def add_infection_cards():
  card_names = [c.name for c in Cities.query.all()]
  for name in card_names:
    if not InfectionCard.query.filter_by(name=name):
      card = InfectionCard(name=name)
      card.save_to_db()

def write_oldcities_data_to_json_file():
  import json
  cities = [c.json() for c in OldCities.query.all()]
  with open('old_cities_data.json', 'w') as outfile:

    json.dump(cities, outfile, ensure_ascii=False, indent=2)

def main():
  app = create_app()
  with app.app_context():
    # move_cities()
    # add_infection_cards()
    write_oldcities_data_to_json_file()

if __name__ == '__main__':
  main()