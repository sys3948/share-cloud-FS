from flask import jsonify, request

from . import main

@main.route('/upload', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    if request.method == 'POST':
        print('upload/ POST Method 요청함.')
    if request.method == 'OPTIONS':
        print('upload/ OPTIONS Method 요청함.')
    return jsonify({'msg' : 'Hello World!'})


@main.route('/create_folder', methods=['POST'])
def create_folder():
    print('Http 통신 성공!')
    return 'hello world!'

