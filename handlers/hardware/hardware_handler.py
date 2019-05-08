# coding=utf-8

from handlers.base.base_handler import BaseHandler
from models.account.account_user_model import *
from libs.redis_conn.redis_conn import conn
import json
from xpinyin import Pinyin



tret_id = None
class Testhandler(BaseHandler):
    """硬件http请求测试接口"""
    def post(self):
        print(self.get_argument('test','no'))
        # print(self.get_argument('test2','no'))
        send_data={
            "data": "test success!",
        }
        return self.write(send_data)



class DespensaryInputBednumInterface(BaseHandler):
    """配药系统输入病床号的数据接口"""
    def get(self):
        global tret_id
        hdwr_ID = self.get_argument('ID', '')
        bednum = self.get_argument('bednum', '')
        query= pt_bs_msg.by_bednum(bednum)  # 查询该病床上是否安排有病人
        if query:  # 如果查询到该病床有安排病人
            print("该床有安排病人")
            tret_id = query.tret_id  # 获取tret_id
            conn.hset(tret_id, "bednum", bednum)  # 以tret_id为名新建hash 保存bednum与hadwr_ID
            conn.hset(tret_id, "hdwr_ID", hdwr_ID)

            query = pt_bs_msg.by_bednum(bednum)
            Prescription_query = Prescription.by_tret_id(query.tret_id)
            conn.hset(tret_id, "drug_id_msg", Prescription_query.drug_id_msg)
            conn.hset(tret_id, "medicine_msg", Prescription_query.medicine_msg)
            print("++++++++++++++++++++")
            bednum_save = conn.hget(tret_id, "bednum")
            hdwr_ID_save = conn.hget(tret_id, "hdwr_ID")
            medicine_msg_save = conn.hget(tret_id, "medicine_msg")
            drug_id_msg_save = conn.hget(tret_id, "drug_id_msg")
            print("bednum_save = " + str(bednum_save) + str(type(bednum_save)))
            print("hdwr_ID_save = " + str(hdwr_ID_save) + str(type(hdwr_ID_save)))
            print("medicine_msg_save = " + str(medicine_msg_save) + str(type(medicine_msg_save)))
            print("drug_id_msg_save = " + str(drug_id_msg_save) + str(type(drug_id_msg_save)))
            # "该床有安排病人病床号患者药品该病床未安排患者不存在该病床药品匹配成功药品匹配失败该患者药单中没有该药该患者的药单为数据库中无此药品扫码器或病床号不匹配该药品：林可霉素 超出用药数量，请移除该药品后继续操作该药品：氯化钾注射液 不在配药单中，请移除该药品后继续操作不存在该病床尚缺药品药患匹配成功，即将打开药瓶挂钩"
            medicine_res = Prescription_query.medicine_msg  # 查询该tret_ID对应的处方信息
            msg = '病床号:'.decode("utf-8") + bednum + '\n患者:'.decode("utf-8") + query.name + '\n药品:'.decode("utf-8") + medicine_res + "\r\n"
            status = "200"
        elif Bed_rack.by_bednum(bednum):
            status = "401"
            msg = "该病床未安排患者"
        else:
            status = "402"
            msg = "不存在该病床"
        data = {
            "status": status,
            "msg": msg
        }
        # return self.write(json.dumps(data))
        print(msg)
        # return self.write(str(data).encode("gb2312"))
        return self.write(data)
        return data
"""这里有个bug 不会进入else"""


class ScanDrugQRCodeInterface(BaseHandler):
    def get(self):
        global tret_id
        hdwr_ID = self.get_argument('ID', '')
        bednum = self.get_argument('bednum', '')
        drug_id = self.get_argument('qrcode', '')
        print("hdwr_ID = " + hdwr_ID)
        print("hdwr_ID_save" + conn.hget(tret_id, 'hdwr_ID'))
        if hdwr_ID == conn.hget(tret_id, 'hdwr_ID') and bednum == conn.hget(tret_id, 'bednum'):
            drug_id_msg = conn.hget(tret_id, "drug_id_msg")
            print(drug_id_msg)
            drug_id_msg_list = drug_id_msg.split(',')
            print(drug_id_msg_list)
            query = Drug.by_id(drug_id[:8])
            if drug_id[:8] in drug_id_msg_list:  # 如果药品编号的前8位在该列表中就匹配成功
                print("药品匹配成功")
                print(query.drug_name)
                msg = "药品匹配成功 ".decode("utf-8") + query.drug_name
                # 删除这个
                drug_id_msg_list.remove(drug_id[:8])
                print(drug_id_msg_list)
                drug_id_msg = ''
                for i in drug_id_msg_list:
                    drug_id_msg +=  i + ","
                drug_id_msg = drug_id_msg[:-1]
                print(drug_id_msg)
                conn.hset(tret_id, "drug_id_msg", drug_id_msg)
                print(conn.hget(tret_id, "drug_id_msg"))

                conn.hset(tret_id, 'drug_id_msg', drug_id_msg)
            elif query:
                print("药品匹配失败")
                msg = "该患者药单中没有该药:".decode("utf-8") + query.drug_name + "该患者的药单为".decode("utf-8") + conn.hget(tret_id, "medicine_msg")
            else:
                print("数据库中无此药品")
                msg = "数据库中无此药品"
        else:
            print("错误")
            msg = "扫码器或病床号不匹配"
        p = Pinyin()
        print(msg)
        return self.write(msg)


class ConfirmDrug(BaseHandler):
    def get(self):
        hdwr_ID = self.get_argument('ID', '')
        bednum = self.get_argument('bednum', '')




class MsgRecvAndAskHookInterface(BaseHandler):
    """这个接口用于处理输液监控系统发送的流速和剩余时间等信息和定时询问开锁和"""
    def get(self):
        speed = self.get_argument("s",'')
        remain_time = self.get_argument("rt",'')
        conn.hset(self.cache_name, "speed", speed)  #
        # conn.hset(self.cache_name, "rt", remain_time)
        hook = conn.hget(self.cache_name, "hook")  # 去缓存里面查询能否开锁
        data = {"open": hook}
        print("s = " + speed)
        return self.write("op=1&c=100" + "\r\n")

# class DespensaryInputBednumInterface(BaseHandler):
#     def get(self):
#         s = "收到设备D0000001的数据bednum=0011\n开始为0011病床患者配药"
#         print(s)
#         return self.write(s)
#
#
# class ScanDrugQRCodeInterface(BaseHandler):
#     def get(self):
#         qrcode = self.get_argument('qrcode', '')
#         if qrcode == "6939030220131":
#             s = "收到设备D0000001的数据bednum=0011,qrcode=6939030220131\n收到药品条形码数据6939030220131\n经查询这是葡萄糖注射液 该药品在该患者的药单中 药品正确\n"
#         elif qrcode == "6922030220132":
#             s = "收到设备D0000001的数据\n收到药品条形码数据6922030220132\n经查询这是氯化钠注射液 该药品不在该患者的药单中  药品错误"
#         elif qrcode == "6988030220138":
#             s = "收到设备D0000001的数据bednum=0011,qrcode=6988030220138\n收到药品条形码数据6988030220138\n经查询这是头孢呋辛钠\n该药品在该患者的药单中 药品正确"
#         elif qrcode == "6988030220133":
#             s = "收到设备D0000001的数据bednum=0011,qrcode=6988030220138\n收到药品条形码数据6988030220138\n经查询这是头孢呋辛钠 该药品已配置完成\n药品重复\n请移除重复药品\n然后扫描下一药品\n"
#         else:
#             s =''
#         print(s)
#         self.write(s)
#
#
# class DispensaryConfirmInterface(BaseHandler):
#     def get(self):
#         drug = self.get_argument("drug", '')
#         print("drug = " + drug)
#         if drug == "6939030220131":
#             s = "收到设备D0000001的配药结束请求\n该次配药尚缺药物头孢呋辛钠\n确认失败"
#         elif drug == "6939030220131 6988030220138":
#             s = "收到设备D0000001的配药结束请求\n药品已齐全\n确认成功\n"
#         else:
#             pass
#         print(s)
#         self.write(s)
#
#
# class TransfuseScanPtInterface(BaseHandler):
#     def get(self):
#         qrcode = self.get_argument("qrcode", '')
#         bar_code = self.get_argument("bar_code", '')
#         if bar_code == "6939030220131":
#             s = "收到设备P00000001的数据\nID=P00000001&bednum=0011&bar_code=6939030220131\n药患配对成功\n挂钩打开 可以开始输液\n"
#         else:
#             s = "收到设备P00000001的数据\nID=P00000001&bednum=0011&qrcode=http://www.pythonhj.top/phone_scan?tret_id=1\n该患者病床号：0011\n姓名：胡劲\n"
#         print(s)
#         self.write(s)