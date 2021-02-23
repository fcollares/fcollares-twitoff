"""Main app/routing file for Twitoff"""

from os import getenv
from flask import Flask, render_template
from .models import DB, User, Tweet, insert_example_users


def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route("/")
    def root():
        """At end point '/'"""
        users = User.query.all()
        return render_template("base.html", title="Home", users=users)

    @app.route("/update")
    def update

    @app.route("/reset")
    def reset():
        """reset DB using drop_all()"""
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        return render_template("base.html", title="RESET",
                               users=User.query.all())

    return app
