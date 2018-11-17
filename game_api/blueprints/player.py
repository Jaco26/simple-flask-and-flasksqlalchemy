from flask import Blueprint, jsonify, request
from game_api.models.player_cards import Player


player = Blueprint('player', __name__, url_prefix='/player')


@player.route('<int:_id>', methods=["GET", "POST", "DELETE", "PUT"])
def handle_user(_id):
  data = request.get_json()
  print('DATA', _id)
  # if request.method == "GET":
    
#   if request.method == "GET":
#     # users = [p.json() for p in Person.query.all()]
#     return jsonify({ 'users': users }), 200
#   elif request.method == "POST":
#     data = request.get_json()
#     # user = Person(name=data['name'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({ 'message': 'added person' }), 201
    

# @user.route('/<int:_id>', methods=["DELETE"])
# def handle_delete(_id):
#   # Person.query.filter(Person.id == _id).delete()
#   db.session.commit()
#   return 'Success', 200