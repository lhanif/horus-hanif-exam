from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# register user
def register_user(data):
    user = User(
        username=data["username"],
        password=generate_password_hash(data["password"]),
        email=data["email"],
        nama=data["nama"]
    )
    db.session.add(user)
    db.session.commit()
    return user

# login authentication
def authentication(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

# list all users
def get_all_users():
    return User.query.all()

# update user data
def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.nama = data.get("nama", user.nama)
    db.session.commit()
    return user

# delete user data
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

# get user by id
def get_user_by_id(user_id):
    return User.query.get(user_id)