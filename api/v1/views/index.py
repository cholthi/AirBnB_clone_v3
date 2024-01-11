#!/usr/bin/python3
"""index blueprint"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {'user': User, 'state': State, 'city': City,
           'review': Review, 'place': Place, 'amenity': Amenity}


@app_views.route('/status', methods=['GET'])
def status():
    """view for status endpoint"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats():
    """ Returns count of the model objects in the app"""
    stat_dict = {}
    for cls in classes:
        stat_dict[cls] = storage.count(classes[cls])
    return jsonify(stat_dict)
