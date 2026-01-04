from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "shop.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template("index.html", products=products)


@app.route("/shop")
def shop():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template("shop.html", products=products)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        db = get_db()
        db.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (name, price)
        )
        db.commit()
        return redirect(url_for("admin"))

    return render_template("admin.html")


# ⛔ DEBUG YOK
# ⛔ 127.0.0.1 YOK
# ✅ SADECE RENDER UYUMLU RUN

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
