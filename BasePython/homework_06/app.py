from http import HTTPStatus
from os import getenv
from werkzeug.exceptions import BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate

from models.database import db
from models import User
from forms import UserForm


app = Flask(__name__)

CONFIG_OBJECT_PATH = f"config.{getenv('CONFIG_NAME', 'DevelopmentConfig')}"
app.config.from_object(CONFIG_OBJECT_PATH)


db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="list_users")
def index():
    users: list[User] = User.query.all()
    return render_template("app/list.html", users=users)


@app.route("/add/", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = UserForm() 
    if request.method == "GET":
        return render_template("app/add_user.html", form=form)

    if not form.validate_on_submit():
        return render_template("app/add_user.html", form=form), HTTPStatus.BAD_REQUEST

    name = form.data["name"]
    username = form.data["username"]
    email = form.data["email"]
    product = User(name=name, username=username, email=email)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not save user with name {name}.")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError("Could not save user. Unexpected error")

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

