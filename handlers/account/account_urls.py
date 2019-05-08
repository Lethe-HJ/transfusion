# coding=utf-8

from account_auth_handler import *

from account_handler import *

accounts_urls = [

    (r'/login_submit', LoginSubmitHandler),  # 登录路由
    (r'/page_access/manage', ManagePageHandler),
    (r'/user_get', UserGetHandler),
    # (r'/auth/user_login', LoginSubmitHandler),  # 登录路由
    # (r'/auth/captcha', CaptchaHandler),  # 图形验证码路由
    # (r'/auth/user_regist', RegistHandler),
    # (r'/auth/mobile_code', MobileCodeHandler),
    # (r'/account/user_profile', ProfileHandler),
    # (r'/account/user_edit', ProfileEditHandler),
    # (r'/account/send_user_email', ProfileModifyEmailHandler),
    # (r'/account/auth_email_code', ProfileAuthEmailHandler),
    # (r'/road_msg', RoadmsgPageHandler),
    # (r'/feedback', UserFeedbackHandler),
    # (r'/manage', ManageEntryHandler),
    # (r'/index', IndexPageHanlder),
    # (r'/supervise', SupervisePageHanlder),
    # (r'/supervise_submit', SuperviseSubmitHanlder),
    # (r'/refresh', RefreshHanlder),
    # (r'/ajax', AjaxHanlder),
]

