from flask_jwt_extended import jwt_required

from app.main import bp
from .models import (
    Park,
    Attraction
)
from .schemas import (
    ReportSchema,
)


@bp.route('/report-by-park')
@jwt_required()
def report_by_park():
    parks = Park.query.all()
    schema = ReportSchema(many=True)
    return schema.dump(parks)


@bp.route('/report-by-attraction')
@jwt_required()
def report_by_attraction():
    parks = Attraction.query.all()
    schema = ReportSchema(many=True)
    return schema.dump(parks)
