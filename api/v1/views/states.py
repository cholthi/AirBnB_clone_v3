#!/usr/bin/python3
""" State object RESTful routes"""
from models import storage
from flask import jsonify, abort, request
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/', methods=['GET'])
def list_states():
    """Returns a list of states in json format"""
    all_states = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(all_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Return a single State object by id"""
    states = storage.all(State).values()
    any_state = [obj.to_dict() for obj in states if obj.id == state_id]
    if any_state == []:
        abort(404)
    return jsonify(any_state[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes state object by id"""
    all_states = storage.all(State).values()
    deleted = False
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
            deleted = True
        if deleted:
            break
    if not deleted:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a new state object from request"""
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates State"""
    all_states = [obj.to_dict() for obj in storage.all(State).values(
        ) if obj.id == state_id]
    if all_states == []:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    for state in storage.all(State).values():
        if state.id == state_id:
            state.name = request.json['name']
            break
    storage.save()
    return jsonify(state.to_dict()), 200
