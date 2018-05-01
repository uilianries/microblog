#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '389rjwddefje892jf29eijf'
