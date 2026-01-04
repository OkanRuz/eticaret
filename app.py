from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shop")
def shop():
    products = [
        ("Kulaklık", 500),
        ("Klavye", 900),
        ("Mouse", 400)
    ]
    return render_template("shop.html", products=products)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # şimdilik kontrol yok
        return redirect("/shop")
    return render_template("login.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
