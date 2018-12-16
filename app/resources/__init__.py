from flask import Blueprint
from flask_restful import Api

from app.resources.setup import (
  GamesList,
  GameById,
  ChooseRole,
  JoinGame,
  PlayerById,
  PlayerList,
  RolesList,
)

from app.resources.play import (
  GameCitiesList,
  CityById,
)

# Endpoints dealing with game setup
setup_bp = Blueprint('setup', __name__, url_prefix='/api/setup')
setup_api = Api(setup_bp)

setup_api.add_resource(PlayerList, '/players')
setup_api.add_resource(PlayerById, '/player/<int:_id>')
setup_api.add_resource(RolesList, '/roles')
setup_api.add_resource(GamesList, '/games')
setup_api.add_resource(GameById, '/game/<int:_id>')
setup_api.add_resource(JoinGame, '/game/<int:_id>/join')
setup_api.add_resource(ChooseRole, '/game/<int:_id>/chooserole')


# Endpoints dealing with gameplay
play_bp = Blueprint('play', __name__, url_prefix='/api/play')
play_api = Api(play_bp)

play_api.add_resource(GameCitiesList, '/game/<int:_id>/cities')
play_api.add_resource(CityById, '/game/<int:_id>/city/<int:city_id>')

