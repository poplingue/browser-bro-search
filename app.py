import tornado.ioloop
import tornado.web
from search import SearchEngine


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
    tornado.ioloop.IOLoop.current().start()
