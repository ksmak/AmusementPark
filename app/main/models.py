from sqlalchemy import event

from app.extensions import db
from app.connectors import RedisConnector


class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    prices = db.relationship('Price', backref='park', lazy=True)


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    prices = db.relationship('Price', backref='attraction', lazy=True)


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(
        db.Integer,
        db.ForeignKey('park.id'),
        nullable=False
    )
    attraction_id = db.Column(
        db.Integer,
        db.ForeignKey('attraction.id'),
        nullable=False
    )
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    tickets = db.relationship('Ticket', backref='price', lazy=True)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    price_id = db.Column(
        db.Integer,
        db.ForeignKey('price.id'),
        nullable=False
    )
    count = db.Column(db.Integer, nullable=False, default=1)


@event.listens_for(Ticket, "after_insert")
def delete_redis_keys(mapper, connection, target):
    print("Event run.")
    r_connect = RedisConnector()
    r_connect.delete('report_by_park')
    r_connect.delete('report_by_attraction')
