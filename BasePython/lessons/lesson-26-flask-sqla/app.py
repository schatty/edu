from flask import Flask
from flask_migrate import Migrate

from models.database import db
from views.products import products_app 

app = Flask(__name__)

app.register_blueprint(products_app, url_prefix="/products")
app.config.update(
    SECRET_KEY="abc",
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://app:password@localhost/shop"
)
db.init_app(app)

migrate = Migrate(app, db)


@app.get("/")
def hello_world():
    return "<p>Hello world!</p>"

