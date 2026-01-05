from flask import Flask
from app.auth import auth_bp
from app.shop import shop_bp
from app.admin import admin_bp
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"

    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
