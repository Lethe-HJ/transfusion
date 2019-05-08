# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.account.account_auth_libs import (auth_captche,login,)
from models.account.account_user_model import Patient,User_bak
#
# class CaptchaHandler(BaseHandler):
#     """生成验证码"""
#     def get(self):
#         pre_code = self.get_argument('pre_code', '')  # 获取上一次的验证码
#         code = self.get_argument('code', '')  # 获取index.html中#code的值
#         img = create_captcha_img(self, pre_code, code)  # 生成图形验证码
#         self.set_header("Content-Type", "image/jpg")  # 设置头部
#         self.write(img)  # 将图片发送给浏览器


class LoginSubmitHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        print("name=%s password=%s" % (username, password))
        result = login(self, username, password, User_bak, psd_encryp=True)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})

#
# class MobileCodeHandler(BaseHandler):
#     """03发送手机短信"""
#     def post(self):
#         mobile = self.get_argument('mobile', '')
#         code = self.get_argument('code', '')
#         captcha = self.get_argument('captcha', '')
#         print mobile, code, captcha
#         result = get_mobile_code_lib(self,  mobile, code, captcha)
#         if result['status'] is True:
#             return self.write({'status': 200, 'msg': result['msg']})
#         return self.write({'status': 400, 'msg': result['msg']})
#
#
# class RegistHandler(BaseHandler):
#     """04注册函数"""
#     def get(self):
#         self.render("account/auth_regist.html", message="注册")
#
#     def post(self):
#         mobile = self.get_argument('mobile', '')
#         mobile_captcha = self.get_argument('mobile_captcha', '')
#         code = self.get_argument('code', '')
#         name = self.get_argument('name', '')
#         password1 = self.get_argument('password1', '')
#         password2 = self.get_argument('password2', '')
#         captcha = self.get_argument('captcha', '')
#         result = regist(self, name, mobile, mobile_captcha,
#                         password1, password2, captcha, code)
#         if result['status'] is True:
#             return self.write({'status': 200, 'msg': result['msg']})
#         return self.write({'status': 400, 'msg': result['msg']})
#
