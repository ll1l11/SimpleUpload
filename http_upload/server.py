# -*- coding: utf-8 -*-
"""上传文件的服务端
Gunicorn provides many command-line options – see gunicorn -h. For example,
to run a Flask application with 4 worker processes (-w 4) binding to localhost port 4000 (-b 127.0.0.1:4000):

.. code-block::

    gunicorn -w 4 -b 127.0.0.1:4000 http_upload.server:app

When source change, unicorn can add --reload option

"""
# import os.path
# import logging
# from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask.views import MethodView


# 可以把下面的配置写到配置文件
DEBUG = False
RANDOM_KEY = 'abc'
CLIENT_PATH_PREFIX = ''
SERVER_PATH_PREFIX = ''

assert RANDOM_KEY

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('HTTP_UPLOAD_SETTINGS', silent=True)

assert app.config['RANDOM_KEY'] and app.config['CLIENT_PATH_PREFIX'] and app.config['SERVER_PATH_PREFIX']

# log to file
# app.logger.setLevel(logging.INFO)
# log_path = os.path.join(os.path.dirname(__file__), 'web.log')
# handler = RotatingFileHandler(log_path, maxBytes=10*1024*1024, backupCount=1)
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s'
#                               '- %(message)s')
# handler.setFormatter(formatter)
# app.logger.addHandler(handler)


@app.before_request
def before_request():
    # 鉴权
    r = request.args.get('r')
    if r != app.config['RANDOM_KEY']:
        return 'no permission'


class UploadView(MethodView):
    def get(self):
        return 'ok'

    def post(self):
        file_ = request.files['file']
        path = request.form['path']
        app.logger.error('upload-%s', path)
        if file_ and path:
            file_.save(path)
            return 'OK, save-{}'.format(path)
        else:
            return 'Error, path-{}'.format(path)


app.add_url_rule('/', view_func=UploadView.as_view('upload'))
