# -*- coding: UTF-8 -*-

from flask import Blueprint
from flask_restful import Resource as BaseResource, Api

__author__ = 'lpe234'

api_bp_v1 = Blueprint('api_v1', __name__)
api = Api(api_bp_v1)


class Resource(BaseResource):
    """
    base resource
    """
    method_decorators = []


import api_article
