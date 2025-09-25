from flask import Blueprint, request, jsonify, current_app
from models.book import Book

# ✅ define blueprint here
books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/", methods=["GET"])
def list_books():
    library = current_app.config["LIBRARY"]
    books = [book.to_dict() for book in library.books]
    return jsonify(books)

@books_blueprint.route("/<isbn>", methods=["GET"])
def get_book(isbn):
    library = current_app.config["LIBRARY"]
    book = library.find_book(isbn)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404

@books_blueprint.route("/", methods=["POST"])
def add_book():
    library = current_app.config["LIBRARY"]
    data = request.json
    
    if library.find_book(data.get("isbn")):
        return jsonify({"error": "Book with this ISBN already exists."}), 409

    book = Book(
        title=data.get("title"),
        author=data.get("author"),
        isbn=data.get("isbn"),
        pages=data.get("pages", 0),
        release_date=data.get("release_date"),
        price=data.get("price", 0.0),
        available=True
    )
    
    library.add_book(book)
    return jsonify({"message": f"Book '{book.title}' added."}), 201

@books_blueprint.route("/<isbn>", methods=["DELETE"])
def remove_book(isbn):
    library = current_app.config["LIBRARY"]
    if not library.find_book(isbn):
        return jsonify({"error": "Book not found"}), 404

    library.remove_book(isbn)
    return jsonify({"message": f"Book '{isbn}' removed."})

@books_blueprint.route("/<isbn>/borrow", methods=["POST"])
def borrow_book(isbn):
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    data = request.json
    user_id = data.get("user_id")

    user = user_manager.find_user(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if user.borrow_book(library, isbn):
        return jsonify({"message": f"User {user_id} borrowed {isbn}."})
    return jsonify({"error": "Book not available"}), 400

@books_blueprint.route("/<isbn>/return", methods=["POST"])
def return_book(isbn):
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    data = request.json
    user_id = data.get("user_id")

    user = user_manager.find_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if user.return_book(library, isbn):
        return jsonify({"message": f"User {user_id} returned {isbn}."})
    return jsonify({"error": "Book was not borrowed"}), 400
