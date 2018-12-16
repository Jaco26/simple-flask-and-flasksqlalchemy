from flask import Flask
from flask_restful import Api
from .db import db, init_db_command, init_db_data
from .models import *
from .resources import setup_bp, play_bp

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
    
  app.register_blueprint(setup_bp)
  app.register_blueprint(play_bp)

  db.init_app(app)

  app.cli.add_command(init_db_command)
  app.cli.add_command(init_db_data)

  return app
