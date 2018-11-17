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

  from .db import db, init_db_command
  from .blueprints.users import user

  db.init_app(app)
  app.register_blueprint(user)
  app.cli.add_command(init_db_command)

  return app
