from main import db


class Valve(db.Model):

    __tablename__ = "Valves"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean)

    def __repr__(self):
        return '<Valve: id={}, state={}>'.format(self.id, self.state)

    def __str__(self):
        return "Valve with id: " + str(self.id) + " state: " + str(self.state)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}