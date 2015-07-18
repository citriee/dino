#!/usr/bin/python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process
import tornado.httpserver
import argparse
import logging
import tornado.options
from tornado.options import define, options
import router

define("port", default=19777, help="run on the given port", type=int)
define("thread", default=5, help="server threads", type=int)

def startServer():
    #tornado.options.options.logging = "debug"
    tornado.options.parse_command_line()
    app = tornado.web.Application(router.Router().dynamicImport())
    sockets = tornado.netutil.bind_sockets(options.port)
    tornado.process.fork_processes(options.thread)
    server = tornado.httpserver.HTTPServer(app)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.current().start()  

if __name__ == "__main__":
    startServer()

