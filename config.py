#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

_BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '389rjwddefje892jf29eijf'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(_BASEDIR, 'app.db')
    # do not signal my app for each new change on DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['uilianries@gmail.com']
    POSTS_PER_PAGE = 3
