#!/usr/bin/python3
"""API application entry point"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(self):
    """Tear down app context"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 error handler"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
