# -*- coding: UTF-8 -*-
import socket
import logging

from flask import Flask
from flask_pymongo import PyMongo

from lemon import settings

__author__ = 'lpe234'


lemon_app = Flask(__name__)

# logger
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.DEBUG)
FORMAT = '%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)d - %(message)s'
file_handler.formatter = logging.Formatter(FORMAT)
lemon_app.logger.setLevel(logging.DEBUG)
lemon_app.logger.addHandler(file_handler)

# load config by hostname, and check config.
host_name = socket.gethostname().capitalize().replace('.', '_').replace('-', '')
lemon_app.config.from_object(getattr(settings, '{}Config'.format(host_name), settings.Config))
if lemon_app.config.get('CONFIG_NAME'):
    info_msg = 'load config from: {}'.format(lemon_app.config.get('CONFIG_NAME'))
    lemon_app.logger.info(info_msg)
else:
    err_msg = 'Config Wrong, Please Check With host_name: {}'.format(host_name)
    exit(err_msg)

# use mongodb
mongo = PyMongo(lemon_app)

# api_v1
from api_v1 import api_bp_v1
lemon_app.register_blueprint(api_bp_v1, url_prefix='/api_v1')


@lemon_app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    lemon_app.run()

