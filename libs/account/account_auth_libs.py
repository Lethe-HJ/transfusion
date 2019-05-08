# coding=utf-8
from random import randint
from datetime import datetime
# from utils.captcha.captcha import create_captcha
from models.account.account_user_model import Patient,User_bak
# from libs.AliCloudMessage.AliCloudMessage import sendTemplateSMS


# def create_captcha_img(self, pre_code, code):
#     """01生成验证码，保存到redis"""
#     if pre_code:  # 如果不是第一次生成验证码
#         # print('不是第一次生成图形二维码')
#         self.conn.delete("captcha:%s" % pre_code)  # 从redis中删除对应的键值对
#     text, img = create_captcha()  # 生成图形二维码 并得到二维码的值
#     self.conn.setex("captcha:%s" % code, text.lower(), 60)  # 保存键值对
#     return img


def auth_captche(self, captche_code, code):
    """02-1校验验证码"""
    print captche_code, code
    if captche_code == '':
        print '请输入验证码'
        return {'status': False, 'msg': '请输入图形验证码'}
    elif self.conn.get("captcha:%s" % code) != captche_code.lower():
        print "验证码为 %s" % self.conn.get("captcha:%s" % code)
        print "你输入的验证码为 %s" % str(captche_code.lower())
        print '输入的图形验证码不正确'
        return {'status': False, 'msg': '输入的图形验证码不正确'}
    else:
        print "输入的验证码正确"
        return {'status': True, 'msg': '正确'}


def login(self, name, password, tb_name, psd_encryp = False):
    """登录函数 tb_name登录表 psd_encryp解密"""
    if name == '' and password == '':
        return {'status': False, 'msg': '请输入用户名或密码'}
    tb = tb_name.by_name(name)  # 通过name来查询表
    if tb:
        if psd_encryp and tb.auth_encrypsd(password):  # 如果是加密验证方式且密码符合
            print('密码符合 登录成功')
            tb.last_login = datetime.now()  # 修改上一次登录时间
            tb.loginnum += 1  # 修改登录次数
            self.db.add(tb)  # 更新user的数据
            self.db.commit()  # 数据库提交
            self.session.set('user_name', tb.name)  # 通过键和值来设置session
            return {'status': True, 'msg': '登录成功'}
        elif not psd_encryp and tb.auth_password(password):  # 如果是普通验证方式且密码符合
            tb.last_login = datetime.now()  # 修改上一次登录时间
            tb.loginnum += 1  # 修改登录次数
            self.db.add(tb)  # 更新user的数据
            self.db.commit()  # 数据库提交
            return {'status': True, 'msg': '登录成功'}
        else:
            return {'status': True, 'msg': '密码错误 登录失败'}
    else:
        return {'status': False, 'msg': '该用户名不存在 登录失败'}

#
# def get_mobile_code_lib(self,  mobile, code, captcha):
#     """03发送手机短信"""
#     if isinstance(mobile, unicode):
#         mobile = mobile.encode('utf-8')
#
#     if self.conn.get("captcha:%s" % code) != captcha.lower():
#         return {'status': False, 'msg': '图形验证码不正确'}
#
#     # 8976  3744  5456
#     # 你的验证码是8976， 5分钟过期
#     mobile_code = randint(1000, 9999)
#     self.conn.setex("mobile_code:%s" % mobile, mobile_code, 2000)
#     print mobile_code
#     #---
#     # sendTemplateSMS(mobile, mobile_code)
#     return {'status': True, 'msg': '验证码已经发送到%s, 请查收' % mobile}
#
#
# def regist(self, name, mobile, mobile_captcha,
#                         password1, password2, captcha, code):
#     """04注册函数"""
#
#     if self.conn.get("captcha:%s" % code) != captcha.lower():
#         return {'status': False, 'msg': '图形验证码不正确'}
#     if self.conn.get("mobile_code:%s" % mobile) != mobile_captcha:
#         return {'status': False, 'msg': '短信验证码不正确'}
#     if password1 != password2:
#         return {'status': False, 'msg': '两次密码不一致'}
#     #存入数据库
#     user = User_bak()
#     user.name = name
#     user.password = password2
#     user.mobile = mobile
#     self.db.add(user)
#     self.db.commit()
#     return {'status': True, 'msg': "注册成功"}
#
#
#
#
