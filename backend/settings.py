from main import db

class Settings(db.Model):
    __tablename__ = "Settings"
    key = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.String(1000), default = False)
