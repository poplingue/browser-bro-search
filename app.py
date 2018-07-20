import tornado.platform.asyncio
from tornado import web, ioloop

from sync_search import SearchEngine


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
