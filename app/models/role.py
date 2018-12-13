from app.db import db

class Role(db.Model):
  __tablename__ = 'role_info'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  description = db.Column(db.Text)
  role_players = db.relationship('PlayerInstance', cascade='delete', backref='role', lazy=True)

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

