from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db():
    return sqlite3.connect("shop.db")

# Login sayfası
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user, pwd)
        )
        db.commit()
        db.close()

        return redirect("/shop")

    return render_template("login.html")

# Shop sayfası
@app.route("/shop")
def shop():
    db = get_db()
    cur = db.cursor()
    products = cur.execute("SELECT * FROM products").fetchall()
    db.close()

    return render_template("shop.html", products=products)

# ❌ app.run YOK
# Render gunicorn ile çalıştırır
