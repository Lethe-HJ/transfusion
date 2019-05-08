# encoding=utf-8
from libs.redis_conn.redis_conn import *
import re

def match_command(key, value):
    if key == 'n':
        conn.hset('fac', 'ID', value)  # 设置fac中的ID值 设备ID
    elif key == 'p':
        conn.hset('fac', 'Pat_qr', value)  # 设置fac中的Pat_qr值 扫描病人二维码获得
    elif key == 'm':
        conn.hset('fac', 'drug_cd', value)  # 设置fac中的drug_cd值 扫描药品条码时获得
    elif key == 's':
        conn.hset('fac', 'spd', value)  # 设置fac中的spa值 获得点滴流速
    elif key == 'rt':
        conn.hset('fac', 'rm_tm', value)  # 设置fac中的rm_tm 获得点滴的剩余时间
    else:
        print("命令不正确")
    return True


def parse_command(last_msg):
    print("1. 解析消息: ")
    print("2." + last_msg)
    print("3. " + str(type(last_msg)))
    last_msg_li = last_msg.split('&')  # 以'&'为界切割字符串，返回一个列表
    for i in last_msg_li:
        kv_li = i.split('=')
        key = kv_li.split('=')[0]
        value = kv_li.split('=')[0]
        match_command(key, value)

