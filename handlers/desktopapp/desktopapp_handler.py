# coding=utf-8

from handlers.base.base_handler import BaseHandler
from models.account.account_user_model import *
from libs.redis_conn.redis_conn import conn
from libs.account.account_auth_libs import login

class DeskAppLoginInterface(BaseHandler):
    def get(self):
        """
        提供桌面应用程序的登录接口
        url参数示例:/desk_login?username=hujin&password=3457
        返回数据示例：{'status': 400, 'msg': '请输入用户名或密码'}
        """
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        print("name=%s password=%s" % (username, password))
        result = login(self, username, password, User_new)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


