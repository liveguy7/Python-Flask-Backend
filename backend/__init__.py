from flask import Flask
from backend.routes.health import health_bp
from backend.routes.users import users_bp
from backend.routes.error import error_bp
from backend.routes.auth import auth_bp
from backend.routes.extensions import _db

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jello.db'
  _db.app = app
  _db.init_app(app)
  _db.create_all()
  
  
  app.register_blueprint(health_bp)
  app.register_blueprint(users_bp)
  app.register_blueprint(error_bp)
  app.register_blueprint(auth_bp)
  
  return app

