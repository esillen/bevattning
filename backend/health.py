from main import db
import datetime

class Health(db.Model):
    __tablename__ = "Health"
    id = db.Column(db.Integer, primary_key=True)
    last_access = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def as_dict(self):
        to_return = {}
        to_return['last_access'] = str(self.last_access)
        now = datetime.datetime.utcnow()
        last_access_seconds = (now - self.last_access).seconds
        last_access_minutes = int(last_access_seconds / 60)
        last_access_seconds = last_access_seconds % 60
        to_return['last_access_seconds'] = last_access_seconds
        to_return['last_access_minutes'] = last_access_minutes
        return to_return

