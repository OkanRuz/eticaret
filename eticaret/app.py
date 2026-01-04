from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("shop.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (user, pwd))
        db.commit()
        return redirect("/shop")

    return render_template("login.html")

@app.route("/shop")
def shop():
    db = get_db()
    cur = db.cursor()
    products = cur.execute("SELECT * FROM products").fetchall()
    return render_template("shop.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/add/<int:id>")
def add_cart(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO cart (user_id, product_id) VALUES (1,?)", (id,))
    db.commit()
    return redirect("/shop")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO products (name, price) VALUES (?,?)", (name, price))
        db.commit()
    return render_template("admin.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
