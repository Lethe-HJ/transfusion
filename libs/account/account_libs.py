#coding=utf-8
import json
from uuid import uuid4
from random import choice
from string import printable
from datetime import datetime
from libs.common.send_email.send_email_libs import send_qq_html_email
from models.account.account_user_model import User_bak

def add_user(self, tbname, username, password):
    if password == "":
        return {'status': False, 'msg': "密码不能为空"}
    if username == "":
        return {'status': False, 'msg': "姓名不能为空"}

    user = self.current_user
    user.name = username
    user.password = password
    user.update_time = datetime.now()
    self.db.add(user)
    self.db.commit()
    return {'status': True, 'msg': "修改成功"}

def edit_profile(self, name, password):
    """编辑个人信息"""
    if password == "":
        return {'status': False, 'msg': "密码不能为空"}

    if name == "":
        return {'status': False, 'msg': "姓名不能为空"}
    user = self.current_user
    user.name = name
    user.password = password
    user.update_time = datetime.now()
    self.db.add(user)
    self.db.commit()
    return {'status': True, 'msg': "修改成功"}

def send_email_libs(self, email):
    """发送邮件"""
    email_code = ''.join([choice(printable[:62]) for i in xrange(4)])
    u = str(uuid4())
    text_dict = {
        u: self.current_user.id,
        'email_code': email_code
    }
    redis_text = json.dumps(text_dict)

    content = """
          <p>html邮件格式练习</p>
          <p><a href="http://192.168.201.135:8000/account/auth_email_code?code={}&email={}&user_id={}">邮箱绑定链接</a></p>
      """.format(email_code, email, u)

    send_fail = send_qq_html_email("3002832062@qq.com", [email], "第一课", content)
    if send_fail:
        return {'status': False, 'msg': "邮箱发送失败"}
    self.conn.setex('email:%s' % email, redis_text, 500)
    return {'status': True, 'msg': "邮箱发送成功"}


def auth_email_libs(self, email, email_code, u):
    """验证邮箱验证码"""
    redis_text = self.conn.get('email:%s' % email)
    if redis_text:
        text_dict = json.loads(redis_text)
        if text_dict and text_dict['email_code'] == email_code:
            user = self.current_user
            if not user:
                user = User_bak.by_id(text_dict[u])
            print user
            user.email = email
            user.update_time =datetime.now()
            self.db.add(user)
            self.db.commit()
            return {'status': True, 'msg': "邮箱修改成功"}
        return {'status': False, 'msg': "验证码错误"}
    return {'status': False, 'msg': "验证码过期"}

