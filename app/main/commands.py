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

    db.session.query(User).delete()
    db.session.query(Ticket).delete()
    db.session.query(Price).delete()
    db.session.query(Attraction).delete()
    db.session.query(Park).delete()
    db.session.commit()

    user_names = []
    while len(user_names) < 500:
        user_name = names.get_first_name()
        if user_name not in user_names:
            user_names.append(user_name)

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

    price_values = (
        150, 200, 300, 400, 500,
        600, 700, 800, 1000, 1200,
        1500, 2000, 2500, 3000, 3500
    )

    users = []
    parks = []
    attractions = []
    prices = []
    tickets = []

    pas = generate_password_hash('12345')
    for user_name in user_names:
        user = User(
            username=user_name,
            password=pas
        )
        users.append(user)

    db.session.add_all(users)
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
                price=random.choice(price_values)
            )
            prices.append(price)
    db.session.add_all(prices)
    db.session.commit()

    for _ in range(10000):
        user = random.choice(users)
        price = random.choice(prices)
        count = random.randrange(1, 10)
        ticket = Ticket(
            user=user,
            price=price,
            count=count
        )
        tickets.append(ticket)
    db.session.add_all(tickets)
    db.session.commit()
