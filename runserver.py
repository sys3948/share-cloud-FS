from distutils.log import debug
from app import create_app

app = create_app('default')
app.run(host='0.0.0.0', debug = True)