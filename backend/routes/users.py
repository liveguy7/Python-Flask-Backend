from flask import Blueprint, jsonify, request, Response
from werkzeug.security import generate_password_hash
from backend.routes import basic_auth, token_auth
from backend.entities.user import User as u
from backend.entities import _db

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route('', methods=["GET"])
@basic_auth.login_required
def get_all_users():
  users = _db.session.scalars(select(User)).all()
  return jsonify([{
    "id": u.id,
    "username": u.username
  } for u in users])

@users_bp.route('', methods=["POST"])
@token_auth.login_required
def create_user():
  d = request.json
  print(d)

  _db.session.execute(insert(User).values(
    username = d["username"],
    email = d["email"],
    password=generate_password_hash(d["password"])
  ))
  _db.session.commit()
  
  return Response(status=204)
  

@users_bp.route('/<int:user_id>', methods=["GET"])
@token_auth.login_required
def get_user(user_id):
  user = _db.session.scalars(select(User).where(User.id == user_id)).one()
  return jsonify({"id": user.id, "username": user.username})












