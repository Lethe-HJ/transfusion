# coding=utf-8
import tornado.escape
import tornado.web
from libs.pycket.session import SessionMixin
from libs.db.dbsession import dbSession
from libs.redis_conn.redis_conn import conn
from models.account.account_user_model import User_bak

users = {
    'user': User_bak
}


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db = dbSession
        self.conn = conn
        self.cache_name = None

    def set_default_headers(self):  # 允许跨域请求
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        # self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get_current_user(self):
        """获取当前用户 当用户进行第一次请求时调用一次该方法 此后通过self.current_user来获得用户"""
        username = self.session.get("user_name")
        user = None
        if username:
            user = User_bak.by_name(username)
        return user if user else None

        # return username

        # if username:
        #     user = users[username['user_tablename']].by_id(username['user_id'])
        #     return user if user else None
        # else:
        #     return None

    def on_finish(self):
        self.db.close()

