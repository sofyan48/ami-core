import os
from agent.configs import Config
from flask import Flask
from flask_cors import CORS

root_dir = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from agent.controllers import api_blueprint
    from agent.controllers import swaggerui_blueprint

    app.register_blueprint(swaggerui_blueprint, url_prefix=os.getenv('SWAGGER_URL'))
    app.register_blueprint(api_blueprint)

    return app
