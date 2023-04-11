from app.extensions import db


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
