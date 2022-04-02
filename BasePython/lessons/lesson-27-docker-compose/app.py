from os import getenv
from flask import Flask
from flask_migrate import Migrate

from models.database import db
from views.products import products_app 

app = Flask(__name__)

CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.register_blueprint(products_app, url_prefix="/products")
app.config.from_object(CONFIG_OBJECT_PATH)
db.init_app(app)

migrate = Migrate(app, db)


@app.get("/")
def hello_world():
    return "<p>Hello world!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

