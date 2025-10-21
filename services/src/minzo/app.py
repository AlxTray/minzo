# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    @app.route("/health")
    def health():
        return jsonify("Minzo service is online!")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
