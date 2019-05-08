# coding:utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json


class WxApi(object):
    @classmethod
    def send_code(cls, js_code):
        print "**********WxApi.send_code*********"
        appid = 'wx030c86c4fbfe876f'  # 申书琴
        secret = '573fc6b96cce28360dd4eafe967317c0'
        url = 'https://api.weixin.qq.com/sns/jscode2session?' \
            'appid=%s&secret=%s&' \
            'js_code=%s&grant_type=authorization_code' % (appid, secret, js_code)
        r = requests.get(url, verify=False)
        print '*****request status_code is\n%d' % r.status_code
        print '*****request return content is:\n' + r.content
        import json
        rt_openid = json.loads(r.content)["openid"]
        utf8_openid = rt_openid.encode('utf-8')
        print utf8_openid
        return utf8_openid

# if __name__ == "__main__":
#     r = requests.get(url, verify=False)
#     print(r.status_code)

