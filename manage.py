import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from game_api import create_app
from game_api.db import db

import game_api.models

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()