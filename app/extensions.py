from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_redis import FlaskRedis


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()
rc = FlaskRedis()
