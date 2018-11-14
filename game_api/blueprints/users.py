from flask import Blueprint, jsonify, request
from game_api.db import db, Person

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('', methods=["GET", "POST", "DELETE"])
def handle_user():
  if request.method == "GET":
    users = [p.json() for p in Person.query.all()]
    return jsonify({ 'users': users }), 200
  elif request.method == "POST":
    data = request.get_json()
    user = Person(name=data['name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'message': 'added person' }), 201
    

@user.route('/<int:_id>', methods=["DELETE"])
def handle_delete(_id):
  Person.query.filter(Person.id == _id).delete()
  db.session.commit()
  return 'Success', 200