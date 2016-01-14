# -*- coding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hola Castellón!")

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(sys.version)

def application():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/version", VersionHandler),
    ])

if __name__ == "__main__":
    app = application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
