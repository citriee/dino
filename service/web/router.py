#!/usr/bin/python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import os.path
import glob

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 请求处理目录
HANDLE_DIR = "{current_dir}/handlers/".format(current_dir=CURRENT_DIR)

sys.path.append(HANDLE_DIR)

from __init__ import BaseHandler

class Router(object):

    filters = set(["__init__.py", "base_handler.py"])

    def listHandlers(self):
        '''动态加载handlers 配置路由器'''
        handlers = glob.glob("%s/*.py" % HANDLE_DIR)
        assginHandlers = {}
        for handler in handlers:
            handlerName = os.path.basename(handler) 
            if handlerName in self.filters: continue
            module = handlerName.replace(".py", "")
            importModule = __import__(module)
            m = sys.modules[module]
            attrs = dir(m)
            for at in attrs:
                attr = getattr(m, at)
                if type(attr) == type and \
                    issubclass(attr, BaseHandler) and \
                    at != "BaseHandler":
                    try:
                        router = "/%s" % importModule.__router__
                        assginHandlers[router] = attr
                    except: 
                        continue
        return assginHandlers

    def dynamicImport(self):
        modules = self.listHandlers()
        return modules.items()

