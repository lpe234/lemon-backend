# -*- coding: UTF-8 -*-

from flask import Flask

from api_v1 import api_bp_v1


__author__ = 'lpe234'


lemon_app = Flask(__name__)

# api_v1
lemon_app.register_blueprint(api_bp_v1, url_prefix='/api_v1')


@lemon_app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    lemon_app.run()

