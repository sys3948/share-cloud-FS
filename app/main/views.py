from flask import jsonify, Response, request

from . import main

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    res = Response()
    if request.method == 'POST':
        print('upload/ POST Method 요청함.')
        res.headers.add("Access-Control-Allow-Origin", "*")
        res.headers.add("Access-Control-Allow-Headers", "*")
    return res

