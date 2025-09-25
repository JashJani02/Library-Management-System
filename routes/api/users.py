from flask import Blueprint, request, jsonify, current_app
from models.user import User


users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/", methods=["GET"])
def list_users():
    user_manager = current_app.config["USER_MANAGER"]
    users = [user.to_dict() for user in user_manager.users]
    return jsonify(users)

@users_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user_manager = current_app.config["USER_MANAGER"]
    user = user_manager.find_user(user_id)

    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@users_blueprint.route("/", methods=["POST"])
def add_user():
    user_manager = current_app.config["USER_MANAGER"]
    data = request.json
    
    if user_manager.find_user(data.get("user_id")):
        return jsonify({"error": "User with this ID already exists."}), 409

    user = User(user_id=data.get("user_id"), name=data.get("name"), email=data.get("email"))
    user_manager.add_user(user)
    return jsonify({"message": f"User {user.name} is added."}), 201

@users_blueprint.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    user_manager = current_app.config["USER_MANAGER"]
    if not user_manager.find_user(user_id):
        return jsonify({"error": "User not found"}), 404

    user_manager.remove_user(user_id)
    return jsonify({"message": f"User {user_id} removed."})

@users_blueprint.route("/<int:user_id>/borrowed", methods=["GET"])
def borrowed_books(user_id):
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    user = user_manager.find_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    borrowed = [book.to_dict() for book in user.list_borrow_book(library)]
    return jsonify(borrowed)
