# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register our routes (we'll build this next)
    from app.routes import audit_bp
    app.register_blueprint(audit_bp)

    return app