from flask import jsonify

from . import main

@main.route('/upload')
def upload():
    print('hello World')
    json_data = {'msg' : 'Hello World'}
    return jsonify(json_data)
