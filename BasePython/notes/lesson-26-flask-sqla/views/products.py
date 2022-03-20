from http import HTTPStatus

from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from models import Product
from models.database import db
from forms import ProductForm


products_app = Blueprint("products_app", __name__)


@products_app.get("/", endpoint="products_list")
def list_products():
    products: list[Product] = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.get("/<int:product_id>/", endpoint="product_details")
def get_product(product_id: int):
    product = Product.query.get(product_id)
    if product is None: 
        raise NotFound(f"Product {product_id}")

    return render_template(
        "products/detail.html",
        product=product
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm() 
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), HTTPStatus.BAD_REQUEST

    product_name = form.data["name"]
    product_is_new = form.data["is_new"]
    product = Product(name=product_name, is_new=product_is_new)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not save product with name {product_name}.")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError("Could not save product. Unexpected error")


    url = url_for("products_app.product_details", product_id=product.id)
    return redirect(url)