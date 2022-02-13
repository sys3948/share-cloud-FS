from flask import jsonify, request, current_app
import os
import cryptocode

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
    print(request.form)
    print(request.form.get('id'))
    print(cryptocode.decrypt(request.form.get('id'), current_app.config('DECODE_KEY')))
    # os.mkdir('/SFS/' + request.form.get('id'))
    return 'hello world!'

