#!/bin/env python
#encoding:utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import tornado.web
import tornado.escape
import os.path

import logging
LOG = logging.getLogger(__name__)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("%s/../" % CURRENT_DIR)
sys.path.append("%s/../models" % CURRENT_DIR)

class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        self.resolve()

    def post(self):
        self.resolve()

    def resolve(self):
        '''调度入口'''
        LOG.info(self.request.uri)
        self.pre() # 准备工作
        result = self.doAction() # 业务逻辑处理
        if result: self.ret["data"] = result
        self.resp()

    def pre(self):
        self.ret = {
                "msg":"",
                "code":200,
                "data":[],
            }

    def resp(self):
        '''返回结果'''
        self.write(tornado.escape.json_encode(self.ret))

    def setError(self, code, msg):
        '''设置错误码&错误内容'''
        self.ret["msg"] = msg
        self.ret["code"] = code
    
    def doAction(self):
        '''sub handle 重写的方法'''
        pass
