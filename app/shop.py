from flask import Blueprint, render_template

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/shop")
def shop():
    products = [
        ("Kulaklık", 500),
        ("Klavye", 900),
        ("Mouse", 400)
    ]
    return render_template("shop.html", products=products)
