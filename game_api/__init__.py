from flask import Flask, render_template

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

  from game_api.db import db
  from game_api.blueprints.users import user

  app.register_blueprint(user)

  db.init_app(app)
  ctx = app.app_context()
  ctx.push()
  db.create_all()

  return app
