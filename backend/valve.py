from main import db
import datetime


class Valve(db.Model):

    __tablename__ = "Valves"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default = False)
    last_opened = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def __repr__(self):
        return '<Valve: id={}, state={}, last_opened={}>'.format(self.id, self.state, self.last_opened)

    def __str__(self):
        return "Valve with id: " + str(self.id) + ", state: " + str(self.state) + ", last opened: " + str(self.last_opened)
    
    def as_dict(self):
        to_return = {}
        for c in self.__table__.columns:
            if type(getattr(self, c.name)) == datetime.datetime:
                to_return[c.name] = str(getattr(self, c.name))
            else:
                to_return[c.name] = getattr(self, c.name)
        # Add minutes and seconds ago
        seconds_diff = (datetime.datetime.utcnow() - self.last_opened).seconds
        to_return["last_opened_minutes_ago"] = int(seconds_diff / 60)
        to_return["last_opened_seconds_ago"] = seconds_diff % 60
        return to_return
        