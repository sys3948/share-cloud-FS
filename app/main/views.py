from flask import jsonify, request

from . import main

@main.route('/upload', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    if request.method == 'POST':
        print('upload/ POST Method 요청함.')
    if request.method == 'OPTIONS':
        print('upload/ OPTIONS Method 요청함.')
    return jsonify({'msg' : 'Hello World!'})

