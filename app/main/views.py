import json
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


@main.route('/create_user_folder', methods=['POST'])
def create_user_folder():
    msg = '폴더 생성 완료!'
    status_code = 200
    try:
        folder_name = cryptocode.decrypt(request.form.get('id'), current_app.config['DECODE_KEY'])
        os.mkdir('/SFS/' + folder_name)
    except Exception as e:
        msg = '오류 발생! 오류 내용은 ' + str(e) + '입니다.'
        status_code = 500
    return jsonify({'msg' : msg, 'status' : status_code})

@main.route('/create_folder', methods=['POST'])
def create_folder():
    msg = '폴더 생성 완료!'
    status_code = 200
    folder = ''
    try:
        root_name = cryptocode.decrypt(request.form.get('root'), current_app.config['DECODE_KEY'])
        upper_folder_name = cryptocode.decrypt(request.form.get('upper_folder'), current_app.config['DECODE_KEY'])
        folder_name = cryptocode.decrypt(request.form.get('folder'), current_app.config['DECODE_KEY'])
        
        folder += root_name + '/'
        if upper_folder_name:
            folder += upper_folder_name
        folder += folder_name

        print(folder)

        os.mkdir('/SFS/' + folder)
    except Exception as e:
        msg = '오류 발생! 오류 내용은 ' + str(e) + '입니다.'
        status_code = 500
    return jsonify({'msg' : msg, 'status' : status_code})


@main.route('/test_def')
def test_def():
    msg = '폴더 생성 완료!'
    status_code = 200
    return jsonify({'msg' : msg, 'status' : status_code})