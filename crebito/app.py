from flask import Flask

from .blueprints import clients
from .db import CrebitoDB
from .jsonprovider import CrebitoJSONProvider


def create_app() -> Flask:
    app = Flask(__name__)
    app.db = CrebitoDB()
    app.json = CrebitoJSONProvider(app)
    app.register_blueprint(clients)

    return app