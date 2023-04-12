from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app.extensions import db

from app.main import bp
from .models import (
    Park,
    Attraction,
    Ticket
)
from .schemas import (
    ReportSchema,
)
from app.connectors import RedisConnector


@bp.route('/report-by-park')
@jwt_required()
def report_by_park():
    r_connector = RedisConnector()

    cached_data = r_connector.get('report_by_park')

    if not cached_data:
        data = Park.query.all()
        schema = ReportSchema(many=True)
        cached_data = schema.dump(data)
        r_connector.set('report_by_park', cached_data)

    return cached_data


@bp.route('/report-by-attraction')
@jwt_required()
def report_by_attraction():
    r_connector = RedisConnector()

    cached_data = r_connector.get('report_by_attraction')

    if not cached_data:
        data = Attraction.query.all()
        schema = ReportSchema(many=True)
        cached_data = schema.dump(data)
        r_connector.set('report_by_attraction', cached_data)

    return cached_data


@bp.route("/add-ticket", methods=['POST'])
@jwt_required()
def add_ticket():
    user_id = request.json.get("user_id", None)
    price_id = request.json.get("price_id", None)
    count = request.json.get("count", None)

    try:
        ticket = Ticket(
            user_id=user_id,
            price_id=price_id,
            count=count
        )
        db.session.add(ticket)
        db.session.commit()
        return jsonify({
            'result': 'OK',
            'errors': None
        })
    except IntegrityError:
        error = f"Error into database."
        return jsonify({
            'result': 'error',
            'errors': error
        }), 401
