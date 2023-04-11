from flask_jwt_extended import jwt_required

from app.main import bp


@bp.route('/')
@jwt_required()
def index():
    return 'This is The Main Blueprint'
