from datetime import datetime
from flask_restful import Resource, reqparse
from app.models import Game


class StartGame(Resource):
  def put(self, _id):
    game = Game.find_by_id(id=_id)
    game.date_started = datetime.utcnow()
    game.save_to_db()

