import tornado.ioloop
import tornado.web
import tornado.platform.asyncio
from search import SearchEngine

import asyncio


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchEngine),
    ], autoreload=True, debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(7000)
    asyncio.get_event_loop().run_forever()
