from pprint import pprint
from app.db import db
from app import create_app
from app.calculations.find_city_connections import connect_cities
from app.models.cities import Cities


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


def main():
  app = create_app()
  with app.app_context():
    cities = [c.json() for c in OldCities.query.all()]
    for city in cities:
      c = connect_cities(city, cities)
      pprint(c)
      # new_city = Cities(**c)
      # new_city.save_to_db()
      # new_city.save_to_db()

if __name__ == '__main__':
  main()