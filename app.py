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
