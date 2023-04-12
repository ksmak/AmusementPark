from marshmallow import Schema, fields

from app.auth.schemas import UserSchema


class ParkSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class AttractionSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class PriceSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    park = ParkSchema()
    attraction = AttractionSchema()
    price = fields.Number(required=True)


class TicketSchema(Schema):
    id = fields.Integer(dump_only=True)
    user = UserSchema()
    price = PriceSchema()
    count = fields.Integer(required=True)
