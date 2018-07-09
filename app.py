import tornado.platform.asyncio
from search import SearchEngine
from tornado import web, escape, ioloop

import asyncio


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search/([0-9]+)", SearchEngine),
    ], autoreload=True, debug=True)


if __name__ == "__main__":
    app = make_app()

    print("Listening at port 7000")

    app.listen(7000)
    ioloop.IOLoop.instance().start()
    # asyncio.get_event_loop().run_forever()
