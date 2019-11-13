# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import requests
import time
import json


class SendOne(object):
    """天津电子化商务短信接口"""
    def __init__(self, mobiles):
        self.url = "http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login"
        # 请求form data数据的heards传参
        self.header = {
            "Referer": "http://qydj.scjg.tj.gov.cn/reportOnlineService/",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.mobile = mobiles

    def get_response(self):
        # 请求form data数据
        data = {
            'MOBILENO': self.mobile,
            'TEMP': 1
        }

        try:
            response = requests.post(url=self.url, data=data, headers=self.header)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SendTwo(object):
    """小归用车"""
    def __init__(self, mobiles):
        self.mobile = mobiles
        self.url = "https://ems.xg-yc.com/ent/sendMobileCode"
        # 请求request payload数据的headers传参
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_response(self):
        # 请求requests payload数据
        data = {
            'mobile': self.mobile,
        }

        try:
            response = requests.post(url=self.url,  data=json.dumps(data), headers=self.headers)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SendThree(object):
    """瓜子二手车"""
    def __init__(self, mobiles):
        self.mobile = mobiles
        self.url = "https://www.airbnb.cn/users/send_mobile_confirmation_code"
        # 请求 form data 形式的headers传参
        self.headers = {
            "Referer": "https://www.guazi.com/bj/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

    def get_response(self):
        # 请求form data数据
        data = {
            "phone": self.mobile,
            "time": "1554813365",
            "token": "text/html"
        }

        try:
            response = requests.post(url=self.url, data=data, headers=self.headers)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SendFour(object):
    """易法通"""
    def __init__(self, mobiles):
        self.mobile = mobiles
        self.url = "http://www.yifatong.com/Customers/gettsms?rnd="
        # 请求 form data 形式的headers传参
        self.headers = {
            "Connection": "keep-alive",
            "Host": "www.yifatong.com",
            "Referer": "http://www.yifatong.com/Customers/login?url=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    def get_response(self):
        time_now = time.time()
        time_new = ("%0.3f" % time_now)

        url = self.url + time_new + "&mobile=" + str(self.mobile)
        # 请求form data数据
        data = {
            "mobile": self.mobile,
            "rnd": time_new
        }

        try:
            response = requests.get(url=url, data=data, headers=self.headers)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SendFive(object):
    """IT桔子"""
    def __init__(self, mobiles):
        self.mobile = mobiles
        self.url = "https://www.itjuzi.com/api/verificationCodes"
        # 请求 form data 形式的headers传参
        self.headers = {
            "Referer": "https://www.itjuzi.com/retrieve",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        self.header = {
            "Content-Type": "application/json"
        }

    def get_response(self):
        # 请求form data数据
        data = {
            "account": self.mobile,
        }

        try:
            response = requests.post(url=self.url, data=json.dumps(data), headers=self.header)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SendSix(object):
    """图灵联邦"""
    def __init__(self, mobiles):
        self.mobile = mobiles
        self.url = "http://api.turingtopia.com/tllbManagement/sms/reqSmsCode"
        # 请求request payload数据的headers传参
        self.headers = {
            "Referer": "http://www.turingtopia.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Content-Type": "application/json"
        }

    def get_response(self):
        # 请求requests payload数据
        data = {
            'phone': self.mobile,
        }

        try:
            response = requests.post(url=self.url,  data=json.dumps(data), headers=self.headers)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


if __name__ == "__main__":
    mobile = input("Please enter phonenumbers: ")
    while True:
        one = SendOne(mobile)   # 可用
        two = SendTwo(mobile)   # 可用
        three = SendThree(mobile)
        four = SendFour(mobile)
        five = SendFive(mobile)  # 可用
        six = SendSix(mobile)   # 可用
        one.run()
        two.run()
        three.run()
        four.run()
        five.run()
        six.run()
        time.sleep(60)
