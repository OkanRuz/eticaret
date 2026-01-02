import sqlite3

conn = sqlite3.connect("shop.db")
c = conn.cursor()

# Kullanıcılar
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Ürünler
c.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER
)
""")

# Sepet
c.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER
)
""")

# Örnek ürünler
c.execute("INSERT INTO products (name, price) VALUES ('Kulaklık', 500)")
c.execute("INSERT INTO products (name, price) VALUES ('Klavye', 900)")
c.execute("INSERT INTO products (name, price) VALUES ('Mouse', 400)")

conn.commit()
conn.close()
