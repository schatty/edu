from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from werkzeug.exceptions import NotFound, BadRequest


products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Laptop",
    2: "Smartphone"
}


@products_app.get("/", endpoint="products_list")
def list_products():
    # return jsonify(PRODUCTS)
    return render_template("products/list.html", products=list(PRODUCTS.items()))


@products_app.get("/<int:product_id>/", endpoint="product_details")
def get_product(product_id: int):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise NotFound(f"Product {product_id}")

    return render_template(
        "products/detail.html",
        product_id=product_id,
        product_name=product_name
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    print(request.form)
    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Product name is required, please fill `product-name`")

    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name

    url = url_for("products_app.product_details", product_id=product_id)
    return redirect(url)