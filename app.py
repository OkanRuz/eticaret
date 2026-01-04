from flask import Flask, render_template

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
        username = request.form.get("username")
        password = request.form.get("password")

        # Şimdilik kontrol yok, direkt shop'a gönderiyoruz
        return redirect("/shop")

    return render_template("login.html")
