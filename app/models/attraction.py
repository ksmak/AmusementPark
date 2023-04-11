from app.extensions import db


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    prices = db.relationship('Price', backref='attraction', lazy=True)
