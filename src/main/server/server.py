from flask import Flask
from src.main.routes.tag_routes import tag_routes_bp

app = Flask(__name__)

app.register_blueprint(tag_routes_bp)
