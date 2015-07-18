#!/usr/bin/python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import logging
LOG = logging.getLogger(__name__)
from __init__ import BaseHandler

# 路由
__router__ = "test" 

class TestHandler(BaseHandler):
    '''关键词提取处理逻辑'''
    
    def doAction(self):
        LOG.error("this is test bug")
        return "this is test handler"
