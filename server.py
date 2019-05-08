# coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.escape
from tornado.options import define, options
from libs.socketserver.socket_server import ChatServer
from config import settings
from handlers.urls import *
# from libs.socketserver.command_parsing import parsing

define('port', default=8003, help='run port', type=int)
if __name__ == "__main__":
    tornado.options.parse_command_line()  # 解析命令行参数
    app = tornado.web.Application(handlers, **settings)  # 创建应用实例
    http_server = tornado.httpserver.HTTPServer(app)  # 实例化http服务
    http_server.listen(options.port)  # 监听设置的http端口，默认设置为8000端口
    # socketserver = ChatServer()  # 实例化socket
    # socketserver.listen(9000)  # 监听socket端口 9000
    print("Running...")
    # parse_command = parsing()
    # parse_command.get_command()
    tornado.ioloop.IOLoop.instance().start()  # 开始IO轮询


