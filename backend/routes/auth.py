from flask import Blueprint, request, jsonify
import jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
  d = request.json
  if("username" not in d or "password" not in d):
    raise Exception("Unable to authenticate")
  if not check_password_hash (
    allowed_users[d["username"]],
    d["password"]
  ):
    raise Exception("Invalid Password")

  encoded_jwt = jwt.encode({
      "sub" : 1,
      "name": "pan"},
      "mysecret", algorithm="HS256")

  return jsonify({
      "token": encoded_jwt
  })




  