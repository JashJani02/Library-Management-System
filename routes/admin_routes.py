from flask import Blueprint, render_template, request, redirect, url_for, current_app
from models.book import Book
from models.user import User


admin_blueprint = Blueprint("admin", __name__, template_folder="/templates/admin")


@admin_blueprint.route("/dashboard")
def dashboard():
    library = current_app.config["LIBRARY"]
    user_manager = current_app.config["USER_MANAGER"]

    return render_template(
        "admin/dashboard.html",
        total_books=library.count_total_books(),
        total_users=user_manager.count_users()
    )


@admin_blueprint.route("/books", methods=["GET"])
def manage_books():
    library = current_app.config["LIBRARY"]
    return render_template("admin/books_admin.html", books=library.books)


@admin_blueprint.route("/books/add", methods=["POST"])
def add_book():
    library = current_app.config["LIBRARY"]

    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("isbn")
    pages = int(request.form.get("pages", 0))
    release_date = request.form.get("release_date")
    price = float(request.form.get("price", 0))

    new_book = Book(title, author, isbn, pages, release_date, price,True)
    library.add_book(new_book)

    return redirect(url_for("admin.manage_books"))


@admin_blueprint.route("/books/delete/<isbn>", methods=["POST"])
def delete_book(isbn):
    library = current_app.config["LIBRARY"]
    library.remove_book(isbn)
    return redirect(url_for("admin.manage_books"))


@admin_blueprint.route("/users", methods=["GET"])
def manage_users():
    user_manager = current_app.config["USER_MANAGER"]
    return render_template("admin/users_admin.html", users=user_manager.users)


@admin_blueprint.route("/users/add", methods=["POST"])
def add_user():
    user_manager = current_app.config["USER_MANAGER"]

    name = request.form.get("name")
    email = request.form.get("email")

    # Simple auto-increment for user_id
    user_id = len(user_manager.users) + 1

    new_user = User(user_id, name, email)
    user_manager.add_user(new_user)

    return redirect(url_for("admin.manage_users"))


@admin_blueprint.route("/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user_manager = current_app.config["USER_MANAGER"]
    user_manager.remove_user(user_id)
    return redirect(url_for("admin.manage_users"))
