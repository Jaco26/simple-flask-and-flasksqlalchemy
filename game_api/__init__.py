from flask import Flask
from flask_restful import Api

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    # other default config keys and values
  )

  app.config.from_pyfile('config.py')
  api = Api(app)

  @app.route('/')
  def hello():
    return """
    <h1 style="font-family: sans-serif;">
      Welcome to the API!
    </h1>
    """

  from .db import db, init_db_command, init_db_data
  from .resources.player import PlayerList, PlayerById
  from .resources.roles import RolesList
  from .resources.games import GamesList

  api.add_resource(PlayerList, '/api/players')
  api.add_resource(PlayerById, '/api/player/<int:_id>')
  api.add_resource(RolesList, '/api/roles')
  api.add_resource(GamesList, '/api/games')

  db.init_app(app)

  app.cli.add_command(init_db_command)
  app.cli.add_command(init_db_data)

  return app
