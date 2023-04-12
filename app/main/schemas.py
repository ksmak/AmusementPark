from app.extensions import ma
from app.auth.schemas import UserSchema


class ParkSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class AttractionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class TicketSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'count')

    user = ma.Nested(UserSchema)


class PriceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'park', 'attraction', 'price', 'tickets',
                  'ticket_count', 'total_price')
    park = ma.Nested(ParkSchema)
    attraction = ma.Nested(AttractionSchema)
    tickets = ma.Nested(TicketSchema, many=True)
    ticket_count = ma.Method('get_ticket_count')
    total_price = ma.Method('get_total_price')

    def get_ticket_count(self, obj):
        count = 0
        for ticket in obj.tickets:
            count += ticket.count

        return count

    def get_total_price(self, obj):
        count = 0
        for ticket in obj.tickets:
            count += ticket.count

        return obj.price * count


class ReportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'prices',
                  'ticket_count', 'total_price')

    prices = ma.Nested(PriceSchema, many=True)
    ticket_count = ma.Method('get_ticket_count')
    total_price = ma.Method('get_total_price')

    def get_ticket_count(self, obj):
        count = 0
        for price in obj.prices:
            for ticket in price.tickets:
                count += ticket.count

        return count

    def get_total_price(self, obj):
        sum = 0
        for price in obj.prices:
            count = 0
            for ticket in price.tickets:
                count += ticket.count

            sum += count * price.price

        return sum
