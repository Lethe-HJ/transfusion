# coding=utf-8
from handlers.handler import *
from handlers.account.account_urls import accounts_urls
from handlers.hardware.hardware_urls import hardware_urls
from handlers.desktopapp.desktopapp_urls import desktopapp_urls
# 包括主页路由/ 和微信小程序登录API路由/wx
handlers = [
    # (r'/', IndexHandler),
    # (r'/', LoginPageHandler),
    # 微信小程序接口
    (r'/wx_auth_login', WxAuthLoginInterface),
    (r'/wx_user_login', WxUserLoginInterface),
    (r'/wx_case_history', WxCaseHistoryInterface),
    (r'/wx_drug_usage', WxDrugUsageInterface),
    (r'/wx_pulse_data', PulseDataInterface),
    (r'/wx_heat_data', WxTemperatureInterface),
    (r'/wx_sugar_data', WxSugarInterface),
    (r'/wx_consult_msg', WxGetConsultMsgInterface),
    # 安卓程序接口
    (r'/ad_patient_data', AndroidPatientMsgInterface),


    (r'/page_data', PageDataHandler),
    (r'/add_data', DbAddData),
    (r'/add_user', AddUserHandler),
    (r'/wx_tip_data',WxTipDataInterface),

    (r'/desk_test',DeskTestInterface)



]
handlers += accounts_urls  # 将accounts_urls中的路由添加进来
handlers += hardware_urls
handlers += desktopapp_urls