from app.db import db

class InfectionCard(db.Model):
  __tablename__ = 'infection_deck'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())

  def json(self, *args):
    return {
      'id': self.id,
      'name': self.name,
    }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()