from flask import Flask
from getter.getter import getterBlueprint

app = Flask(__name__)

def create_app():
    app.config.update(
        DEBUG=True,
        SECRET_KEY='this%isVvery*secret(and)you$cant#guess'
    )
    app.register_blueprint(getterBlueprint)
    return app