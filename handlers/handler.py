# coding=utf-8
import json
from handlers.base.base_handler import BaseHandler
from libs.wx_api.wx_api import WxApi
from libs.account.account_libs import edit_profile
from libs.account.account_auth_libs import login
from models.account.account_user_model import *
from libs.db.dbsession import dbSession




class WxAuthLoginInterface(BaseHandler):
    def get(self):
        js_code = self.get_arguments('code')[-1]  # 获取微信小程序请求中的js_code信息
        openid = WxApi.send_code(js_code)  # 将js_code发送到微信官方API获取open_id
        self.write(openid)  # 返回的数据


class WxUserLoginInterface(BaseHandler):
    def get(self):
        username = self.get_argument("username", '')
        password = self.get_argument("password", '')
        print("username=%s password=%s" % (username, password))
        result = login(self, username.encode("utf-8"), password, Patient)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class WxCaseHistoryInterface(BaseHandler):
    def get(self):
        IDcard = "430922199710143136"
        case_history_query = case_history.by_IDcard(IDcard)
        case_history_data = {
            "department" : case_history_query.dpt,
            "family": case_history_query.family,
            "HPC" : case_history_query.HPC,
            "PMH" : case_history_query.PMH,
            "PH" : case_history_query.PH,
            "FH" : case_history_query.FH,
            "PS" : case_history_query.PS
        }
        patient_query = pt_bs_msg.by_IDcard(IDcard)
        case_history_data["name"] = '胡劲'
        case_history_data["gender"] = '男'
        case_history_data["roomnum"] = '001'
        case_history_data["bednum"] = '1'

        return self.write(case_history_data)


class WxTipDataInterface(BaseHandler):
    def get(self):
        username = self.session.get("user_name")
        print("username = " + str(username))
        TipData = {
            "ND":"青霉素、红霉素、青霉素",
            "AD":"阿莫西林、地衣芽孢菌胶囊",
            "NF":"辛辣食物、海带、紫菜",
            "AF":"苹果、蔬菜、葡萄",
            "suggest":"建议患者少吃辛辣刺激食物,饮食正常,少熬夜，多做运动，营养均衡。"
            }
        return self.write(TipData)


class WxDrugUsageInterface(BaseHandler):
    def get(self):

        Usage1 = {
            "drug":"复方氨酚皖胶囊",
            "usage":"口服，一次1粒，一日2次",
        }
        Usage2 = {
            "drug":"999感冒灵颗粒",
            "usage":"冲服，一次1袋，一日3次"
        }
        Usage3 = {
            "drug":"氨麻美敏片",
            "usage":"口服，一次1片，一日2次"
        }
        Usage4 = {
            "drug": "阿莫西林胶囊",
            "usage": "口服，一次1粒，一日3次"
        }


        dataList = [Usage3, Usage1, Usage2, Usage4]
        return self.write(json.dumps(dataList))


class DbAddData(BaseHandler):
    def get(self):
        for i in range(2, 200):
            add_data = pt_bs_msg(
                bednum= str(i),
                name=str(i),
                gender = str(i),
                age = i,
                contact = str(i),
                doctor = str(i),
                IDcard = str(i),
                ill = str(i),
            )
            dbSession.add(add_data)
            dbSession.commit()


class PageDataHandler(BaseHandler):
    def get(self):
        page = self.get_argument('page', '')
        limit = self.get_argument('limit', '')
        data_list = []
        end = int(page) * int(limit)
        start = end - int(limit)
        print("***************************************")
        print("page=" + page + "limit=" + limit)
        for i in range(start, end):
            tret_id = i
            query = pt_bs_msg.by_tret_id(tret_id)
            if query:
                data = {
                    "bednum":query.bednum,
                    "name": query.name,
                    "gender": query.gender,
                    "age": query.age,
                    "contact": query.contact,
                    "doctor": query.doctor,
                    "IDcard": query.IDcard,
                    "ill": query.ill
                }
                data_list.append(data)
        patient_info = {
            "code":0,
            "msg":"病人基本信息",
            "count":200,
            "data":data_list
        }
        print(data_list)
        return self.write(patient_info)



class PulseDataInterface(BaseHandler):
    def get(self):
        series = {
            "data":[120,80,120,80],
            "type":"bar"
        }
        xAxis = {
            "type":"category",
            "data":['9/1/12:00','9/3/13:12','9/3/13:12','9/3/13:12']
        }
        pulse_data = {
            "series" : series,
            "xAxis" : xAxis
        }
        return self.write(pulse_data)


class WxTemperatureInterface(BaseHandler):
    def get(self):
        series = {
            "data":['37.5', '37.6', '38.1', '38.2', '37.9', '37.4', '37.1','37.5', '37.6', '38.1', '38.2', '37.9', '37.4', '37.1'],
            "type": "line"
        }
        xAxis = {
            "type": "category",
            "data": ['9/1', '9/2', '9/3', '9/4', '9/5', '9/6', '9/7', '9/1', '9/2', '9/3', '9/4', '9/5', '9/6', '9/7' ]
        }
        Temperature_data = {
            "series": series,
            "xAxis": xAxis
        }
        return self.write(Temperature_data)


class WxSugarInterface(BaseHandler):
    def get(self):
        series = {
            "data":['6.9', '7.0', '6.9', '7.0', '6.9', '7.0', '6.9', '7.0', '6.9', '7.0', ],
            "type": "bar"
        }
        xAxis = {
            "type": "category",
            "data": ['9/1', '9/2', '9/3', '9/4', '9/5', '9/6', '9/7', '9/8', '9/9', '9/10']
        }
        Temperature_data = {
            "series": series,
            "xAxis": xAxis
        }
        return self.write(Temperature_data)

class WxGetConsultMsgInterface(BaseHandler):
    def get(self):
        age = self.get_argument('age','')
        sick = self.get_argument('sick','')
        admin = self.get_argument('admin','')
        txt = self.get_argument('txt','')



class AndroidPatientMsgInterface(BaseHandler):
    def get(self):
        PatientMsg = [
{
"bednum": "0011",
"name": "胡劲",
"gender": "男",
"age": "21",
"contact": "15874159887",
"doctor": "申书琴",
"IDcard": "430922199710143136",
"ill": "阑尾炎"
},
{
"bednum": "0002",
"name": "夏国鑫",
"gender": "男",
"age": "43",
"contact": "18973456021",
"doctor": "邓志华",
"IDcard": "430524197512010011",
"ill": "神经衰落"
},
{
"bednum": "0199",
"name": "舒国",
"gender": "男",
"age": "19",
"contact": "15934670984",
"doctor": "赵丽雯",
"IDcard": "430113199902069998",
"ill": "风疹"
},
{
"bednum": "0109",
"name": "舒静",
"gender": "女",
"age": "19",
"contact": "19924904568",
"doctor": "舒强国",
"IDcard": "430508199909109998",
"ill": "鼾症"
},
{
"bednum": "0071",
"name": "周芳",
"gender": "女",
"age": "86",
"contact": "18248863585",
"doctor": "周利君",
"IDcard": "430122193212075254",
"ill": "偏头痛"
},
{
"bednum": "0066",
"name": "秦莎",
"gender": "女",
"age": "83",
"contact": "19964330138",
"doctor": "秦雄武",
"IDcard": "430309193502041242",
"ill": "脑鸣"
},
{
"bednum": "0036",
"name": "周晓玉",
"gender": "女",
"age": "59",
"contact": "17723943578",
"doctor": "工佳",
"IDcard": "430506195912053817",
"ill": "偏头痛"
},
{
"bednum": "0161",
"name": "胡玉",
"gender": "女",
"age": "77",
"contact": "15209420766",
"doctor": "胡云军",
"IDcard": "430503194112098435",
"ill": "白血病"
},
{
"bednum": "0056",
"name": "胡强",
"gender": "男",
"age": "43",
"contact": "17709429432",
"doctor": "胡胜伍",
"IDcard": "430503197506075360",
"ill": "脑梗塞"
}
]

        return self.write(json.dumps(PatientMsg))






class AddUserHandler(BaseHandler):
    def get(self):
        # name = self.get_argument('name', '')
        # password = self.get_argument('password', '')
        name = "zhangsan"
        password = '222'
        result = edit_profile(self, name, password)
        self.write(result['msg'])


class DeskTestInterface(BaseHandler):
    def get(self):
        return self.write("hello world!")


"""
问题:
1.无法获取微信小程序的current_user
"""

