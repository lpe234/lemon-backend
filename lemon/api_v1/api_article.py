# -*- coding: UTF-8 -*-

from flask import request
from flask_restful import fields, marshal_with

from . import Resource, api

__author__ = 'lpe234'


article_marshal = {
    'id': fields.String,
    'title': fields.String,
    'summary': fields.String,
    'content': fields.String,
    'create_time': fields.DateTime
}


class ArticlesApi(Resource):

    auth_token_without = ['get']

    def get(self):
        pass

    def post(self):
        pass


class ArticleApi(Resource):

    @marshal_with(article_marshal)
    def get(self, id):
        import datetime
        return {
            'id': str(id),
            'title': 'Title',
            'summary': 'Summary',
            'content': 'Content',
            'create_time': datetime.datetime.now()
        }

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(ArticlesApi, '/articles')
api.add_resource(ArticleApi, '/articles/<int:id>')

