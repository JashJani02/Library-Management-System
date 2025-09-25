from flask import Blueprint, render_template, request, redirect, url_for, current_app

user_blueprint = Blueprint("user", __name__, template_folder="../templates/user")

# 👤 User Dashboard
@user_blueprint.route("/dashboard")
def user_dashboard():
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    # For now, assume user with ID=1 is logged in
    user = user_manager.find_user(1)

    borrowed_books = []
    if user:
        borrowed_books = user.list_borrow_book(library)

    return render_template("user/dashboard.html",user=user,borrowed_books=borrowed_books)

# 📖 View Books
@user_blueprint.route("/books", methods=["GET"])
def view_books():
    library = current_app.config["LIBRARY"]
    return render_template("user/books_user.html", books=library.books)

# ✅ Borrow Book
@user_blueprint.route("/books/borrow/<isbn>", methods=["POST"])
def borrow_book(isbn):
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    user = user_manager.find_user(1)  # hardcoded until login system is added
    if user:
        user.borrow_book(library, isbn)

    return redirect(url_for("user.view_books"))

# 🔄 Return Book
@user_blueprint.route("/books/return/<isbn>", methods=["POST"])
def return_book(isbn):
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    user = user_manager.find_user(1)  # hardcoded until login system is added
    if user:
        user.return_book(library, isbn)

    return redirect(url_for("user.view_books"))
