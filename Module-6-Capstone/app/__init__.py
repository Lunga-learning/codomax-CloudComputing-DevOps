from flask import Flask, render_template
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "development-secret-key-change-later"
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {
            "status": "healthy"
        }, 200

    return app
