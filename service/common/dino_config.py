#!/bin/env python
#encoding:utf-8


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

import ConfigParser


DEFAULT_CONFIG_FILE = "%s/log4py.cfg" % CURRENT_DIR


class DConfig(object):
        
    def __init__(self, config):
        if config:



        
    def getLog(self):
        return self.logger

def log(name):
    return DLogger(name).getLog()
