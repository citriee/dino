#!/bin/env python
#encoding:utf-8


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = "%s/../../logs" % CURRENT_DIR
LOG_CONF = "%s/../../conf/log4py.cfg" % CURRENT_DIR

import logging
import logging.config

class DLogger(object):
        
    def __init__(self, name):
        logging.config.fileConfig(LOG_CONF, defaults={"logpath":LOG_DIR})
        if name:
            self.logger = logging.getLogger(name)
        else:
            self.logger = logging.getLogger()
        
        
    def getLog(self):
        return self.logger

def log(name = None):
    return DLogger(name).getLog()
