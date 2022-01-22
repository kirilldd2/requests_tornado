import os
import os.path
from databases import Database
import databases
from tornado.ioloop import IOLoop
import tornado.web
from tornado.httpserver import HTTPServer
from dotenv import load_dotenv
from requests_app.handlers import RequestAddHandler



def make_app(database: Database):
    # pass connection to each handler
    return tornado.web.Application([
        tornado.web.url(
            r'/api/add', RequestAddHandler, {'connection': database.connection()}, name='add'
        ),
    ])


def main():
    # todo: remove after docker
    load_dotenv()
    # create database object and connect
    database = Database(os.getenv('DATABASE_URL'))
    IOLoop.current().run_sync(lambda: database.connect())
    # create app and run server
    app = make_app(database)
    server = HTTPServer(app)
    server.listen(os.getenv('APP_PORT'), address=os.getenv('APP_HOST'))
    print(f"The server is up and running at {os.getenv('APP_HOST')}:{os.getenv('APP_PORT')}")
    IOLoop.current().start()


if __name__ == '__main__':
    main()