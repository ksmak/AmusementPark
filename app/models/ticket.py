from app.extensions import db


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
