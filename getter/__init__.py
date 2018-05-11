from flask import Flask
from getter.getter import getterBlueprint

app = Flask(__name__)

def create_app():
    app.config.update(
        DEBUG=True
    )
    app.register_blueprint(getterBlueprint)
    return app