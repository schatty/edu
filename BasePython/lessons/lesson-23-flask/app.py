from flask import Flask

from views.products import products_app 

app = Flask(__name__)

app.register_blueprint(products_app, url_prefix="/products")


@app.get("/")
def hello_world():
    return "<p>Hello world!</p>"


@app.route("/items/<int:item_id>/")
def get_item(item_id):
    return {"item_id": item_id}


@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_user(name="stranger"):
    return {"message": f"Hello {name}"}