from flask import Flask
from flask_smorest import Api as RestApi

from resources.item import blp as item_blp
from resources.store import blp as store_blp

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

rest_api = RestApi(app)

rest_api.register_blueprint(item_blp)
rest_api.register_blueprint(store_blp)
