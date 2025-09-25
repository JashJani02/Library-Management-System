from flask import Flask, render_template
from models.library import Library
from models.user_manager import UserManager
from routes import books_blueprint, users_blueprint, admin_blueprint, user_blueprint


app = Flask(__name__)

# Global singletons
app.config["LIBRARY"] = Library()
app.config["USER_MANAGER"] = UserManager()

# Register API blueprints
app.register_blueprint(books_blueprint, url_prefix="/api/books")
app.register_blueprint(users_blueprint, url_prefix="/api/users")

# Register Web UI blueprints
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(user_blueprint, url_prefix="/user")

# Root (optional homepage)
@app.route("/")
def home(): 
    library = app.config["LIBRARY"]
    user_manager = app.config["USER_MANAGER"]

    return render_template("home.html",total_books=library.count_total_books(),total_users=user_manager.count_users())

if __name__ == "__main__":
    app.run(debug=True)
