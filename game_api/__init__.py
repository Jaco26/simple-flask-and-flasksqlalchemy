from flask import Flask, render_template
from flask_migrate import Migrate

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    # other default config keys and values
  )

  app.config.from_pyfile('config.py')

  @app.route('/')
  def hello():
    return render_template('index.html')

  from .db import db, init_db_command, init_db_data
  from .blueprints.player import player

  db.init_app(app)
  app.register_blueprint(player)
  app.cli.add_command(init_db_command)
  app.cli.add_command(init_db_data)
  Migrate(app, db)

  return app
