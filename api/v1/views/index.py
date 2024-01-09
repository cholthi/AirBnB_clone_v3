#!/usr/bin/python3
"""index blueprint"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """view for status endpoint"""
    return jsonify({'status': 'OK'})
