from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, set_access_cookies, unset_jwt_cookies, get_jwt_identity
from app.models.user import User
from app.services.user_service import register_user, authentication, get_all_users, update_user, delete_user, get_user_by_id
from app.extensions import db
from app.utils.validators import validate_register, validate_login, validate_update_user

user_bp = Blueprint("users",__name__)

# /register -> Register User
@user_bp.route("/register",methods=["POST"])
def register():
    is_valid, error = validate_register(request.json)
    if not is_valid:
        return jsonify({"message": error}), 400
    register_user(request.json)
    return jsonify({"message":"Registrasi Berhasil"}), 201

# /login -> Login User
@user_bp.route("/login", methods=["POST"])
def login():
    is_valid, error = validate_login(request.json)
    if not is_valid:
        return jsonify({"message": error}), 400
    user = authentication(request.json["username"], request.json["password"])
    if not user:
        return jsonify({"message": "Username atau password salah"}), 401
    token = create_access_token(identity=str(user.id))
    response = jsonify({
        "message": "Login berhasil",
        "user": {
            "id": user.id,
            "username": user.username,
            "nama": user.nama,
            "email": user.email
        }
    })
    set_access_cookies(response, token)
    return response, 200

# /me -> get active user data
@user_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(int(current_user_id))
    return jsonify({
        "id": user.id,
        "username": user.username,
        "nama": user.nama,
        "email": user.email
    }), 200
    
# /logout -> logout and clear session
@user_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"message": "Logout berhasil"})
    unset_jwt_cookies(response)
    return response, 200

# / -> get all users data
@user_bp.route("/",methods=["GET"])
@jwt_required()
def all_users():
    users = get_all_users()
    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "nama": u.nama
        }
        for u in users
    ]), 200


# /id -> update user data
@user_bp.route("/<int:id>",methods=["PUT"])
def edit_user(id):
    is_valid, error = validate_update_user(request.json)
    if not is_valid:
        return jsonify({"message": error}), 400
    update_user(id, request.json)
    return{"message" : "Data user berhasil diperbarui"}, 200

# /id -> delete user data
@user_bp.route("/<int:id>",methods=["DELETE"])
def delete_user_route(id):
    delete_user(id)
    return {"message" : "User berhasil dihapus"}, 200

