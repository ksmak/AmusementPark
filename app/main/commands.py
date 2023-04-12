import random

from werkzeug.security import generate_password_hash

from app.main import bp
from app.extensions import db
from app.auth.models import User
from .models import (
    Park,
    Attraction,
    Price,
    Ticket,
)

import names


@bp.cli.command('generate-data')
def generate_data():
    park_names = (
        'Парк Первого Президента РК',
        'ЦПКиО им. Горького',
        'Парк им. 28 гвардейцев-панфиловцев',
        'Парк Фемели',
        'Парк фонда Первого Президента',
    )
    attraction_names = (
        'Карусель лошадки',
        'Колесо обозрения',
        'Американские горки',
        'Автодром',
        'Цепочная карусель',
        'Паровозик',
        'Аттракцион Корабль',
        'Пятый элемент',
        'Орбита',
        'Детские игровые комнаты',
        'Детский аттракцион Робот',
        'Детский аттракцион Экскаватор',
    )

    users = []
    parks = []
    attractions = []
    prices = []
    tickets = []

    pas = generate_password_hash('12345')
    for _ in range(100):
        user = User(
            username=names.get_first_name(),
            password=pas
        )
        db.session.add(user)
        db.session.commit()

    for park_name in park_names:
        park = Park(
            name=park_name
        )
        parks.append(park)
    db.session.add_all(parks)
    db.session.commit()

    for attr_name in attraction_names:
        attr = Attraction(
            name=attr_name
        )
        attractions.append(attr)
    db.session.add_all(attractions)
    db.session.commit()

    for park in parks:
        for attr in attractions:
            price = Price(
                park=park,
                attraction=attr,
                price=random.randrange(250, 5000),
            )
            prices.append(price)
    db.session.add_all(prices)
    db.session.commit()

    for _ in range(500):
        user = random.choice(users)
        price = random.choice(price)
        count = random.randrange(1, 10)
        ticket = Ticket(
            user=user,
            price=price,
            count=count
        )
        tickets.append(ticket)
    db.session.add_all(tickets)
    db.session.commit()
