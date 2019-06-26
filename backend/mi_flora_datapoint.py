from main import db

class MiFloraDatapoint(db.Model):
    __tablename__ = "MiFloraDatapoints"
    id = db.Column(db.Integer, primary_key=True)
    jsonBlob = db.Column(db.String(1000), default = False)
