from flask import Flask

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    # other default config keys and values
  )

  app.config.from_pyfile('config.py')

  @app.route('/')
  def hello():
    return '<h1 style="font-family: sans-serif;">Hey it\'s working!</h1>'

  from game_api.db import db

  db.init_app(app)
  ctx = app.app_context()
  ctx.push()
  db.create_all()

  return app
