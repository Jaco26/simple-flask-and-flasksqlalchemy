from flask import Flask, render_template
from flask_restful import Api
from flask_migrate import Migrate

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
    return render_template('index.html')

  from .db import db, init_db_command, init_db_data
  from .resources.player import PlayerList, PlayerById
  from .resources.roles import RolesList

  api.add_resource(PlayerList, '/players')
  api.add_resource(PlayerById, '/player/<int:_id>')
  api.add_resource(RolesList, '/roles')


  db.init_app(app)

  app.cli.add_command(init_db_command)
  app.cli.add_command(init_db_data)
  
  Migrate(app, db)

  return app
