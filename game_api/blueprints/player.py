from flask import Blueprint, jsonify, request
from game_api.models import Player

def not_found(item):
  return { 'message': '{} was not found'.format(item)}

player = Blueprint('player', __name__, url_prefix='/player')


@player.route('<int:_id>', methods=["GET", "DELETE", "PUT"])
def player_by_id(_id):
  data = request.get_json()

  if request.method == "GET":
    return Player.find_by_id(_id)


@player.route('', methods=["GET", "POST"])
def players():
  data = request.get_json()
  if request.method == "POST":
    if data and data['name']:
      player = Player.find_by_name(data['name'])
      if player is None:
        new_player = Player(name=data['name'])
        try:
          new_player.save()
        except:
          return 'There was a problem saving the new player', 500
        return 'Success', 201 
      else:
        return 'Player {} already exits'.format(player.name), 400
    else:
      return 'No "name" in request body', 400

  elif request.method == "GET":
    return jsonify({ 'players': [p.json() for p in Player.query.all()] })