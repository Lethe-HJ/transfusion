# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.account.account_libs import edit_profile,send_email_libs, auth_email_libs
from libs.redis_conn.redis_conn import conn
import json



class ManagePageHandler(BaseHandler):
    def get(self):
        self.render('manage.html')


class UserGetHandler(BaseHandler):
    def get(self):
        username = self.session.get("user_name")
        self.write(json.dumps(username))































class ProfileHandler(BaseHandler):
    """用户信息函数"""
    def get(self):
        self.render('account/main.html')


class ProfileEditHandler(BaseHandler):
    """编辑用户信息"""
    def get(self):
        self.render('account/account_edit.html')

    def post(self):
        name = self.get_argument('name', '')
        password = self.get_argument('password', '')
        result = edit_profile(self, name, password)
        if result['status'] is False:
            return self.render('account/account_profile.html', message=result['msg'])
        return self.render('account/account_profile.html', message=result['msg'])


class ProfileModifyEmailHandler(BaseHandler):
    """修改邮箱"""
    def get(self):
        self.render('account/account_send_email.html')

    def post(self):
        email = self.get_argument('email', '')
        result = send_email_libs(self, email)
        if result['status'] is True:
            return self.write(result['msg'])
        return self.write(result['msg'])


class ProfileAuthEmailHandler(BaseHandler):
    """验证邮箱验证码"""
    def get(self):
        email_code = self.get_argument('code', '')
        email = self.get_argument('email', '')
        u = self.get_argument('user_id', '')
        print email_code, email, u
        result = auth_email_libs(self, email, email_code,  u)
        if result['status'] is True:
            return self.redirect('/account/user_edit')
        return self.write(result['msg'])


class RoadmsgPageHandler(BaseHandler):
    def get(self):
        self.render("account/road.html")


class UserFeedbackHandler(BaseHandler):
    def get(self):
        self.render("account/feedback.html")


class IndexPageHanlder(BaseHandler):
    def get(self):
        username = self.session.get("user_name")
        print('*'*20 + str(username))
        self.render("account/select.html", username=username)


class ManageEntryHandler(BaseHandler):
    def get(self):
        self.render("account/manage.html")




#
# class RefreshHanlder(BaseHandler):
#     def post(self):
#         if conn.get('control') == 'auto':
#             scoket_message_handle.traffic_hadler()
#         msg_send = conn.get('send_msg')
#         # print('send_msg的值为' + str(msg_send))
#         if msg_send != '':
#             if msg_send is not None:
#                 ChatServer.send_msg_to_client(msg_send, 'hardware_client', 'GBK')
#         conn.setex('send_msg', '', 6000)  # 清空发送缓存
#         for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
#             conn.setex(i, '0', 6000)  # 清零数据


class SupervisePageHanlder(BaseHandler):
    def get(self):
        self.render('account/supervise.html')


class SuperviseSubmitHanlder(BaseHandler):
    def post(self):
        control = self.get_argument('control1', '')
        change_road = self.get_argument('change_road1', '')
        time = self.get_argument('time1', '')
        conn.setex('control', control, 50000)
        if control == 'auto':
            print('自动模式')
        elif control == 'manual':
            print('手动模式')
        else:
            print('error')
        conn.setex('now_status', change_road, 6000)
        pre = conn.get('pre_status')
        now = conn.get('now_status')
        if conn.get('control') == 'manual':
            print('进入了手动程序')
            message = ''
            # print('pre=%s now=%s' % (pre, now))
            if pre == now:
                pass
            elif pre == "R" and now == "EN":
                message = '9'
            elif pre == "EN" and now == "R":
                message = '8'
            elif pre == "R" and now == "WS":
                message = '7'
            elif pre == "WS" and now == "R":
                message = '6'
            else:
                pass
            print('message = ' + message)
            if message != '':
                message = message + 'T' + str(int(time)/10) + '\r\n'
                ChatServer.send_msg_to_client(message, 'hardware_client', 'GBK')
            else:
                print('没有改变状态，不发送指令')
            conn.setex('pre_status', now, 6000)



class AjaxHanlder(BaseHandler):
    def get(self):
        data = "i love you"
        return self.write(data)