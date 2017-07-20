# -*- coding: UTF-8 -*-

__author__ = 'lpe234'


"""
config module
"""


class Config(object):
    """
    basic config
    """
    CONFIG_NAME = None
    DEBUG = False

    # mongo
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'lemon'


class ProductConfig(Config):
    """
    product config
    """
    pass


class DevelopConfig(Config):
    """
    develop config
    """
    pass


class Lupengdemacbookpro_localConfig(DevelopConfig):
    """
    self config
    """
    CONFIG_NAME = 'LupengConfig'
    DEBUG = True
    pass


class BogonConfig(Lupengdemacbookpro_localConfig):
    """
    Bogon Fix
    """
    pass


