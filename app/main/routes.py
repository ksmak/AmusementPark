from flask_jwt_extended import jwt_required

from app.main import bp

from app.auth import bp
from app.extensions import db
from app.models.park import Park
from app.models.attraction import Attraction
from app.models.price import Price
from app.models.ticket import Ticket


@bp.route('/')
@jwt_required()
def index():
    return 'This is The Main Blueprint'
