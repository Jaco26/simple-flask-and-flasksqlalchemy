from flask_restful import Resource
from app.models import Role

def msg(message):
  return { 'message': message }

class RolesList(Resource):
  def get(self):
    try:
      return [role.json() for role in Role.query.all()]
    except:
      return msg('The was an error getting all roles'), 500
