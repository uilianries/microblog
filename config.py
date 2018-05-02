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
