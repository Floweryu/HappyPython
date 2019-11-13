# -*- coding:utf-8 -*-
# Time: 2019-05-07 20:57:20
# Auther: ZhangJunFeng
import requests
import json


class Fanyi(object):
    def __init__(self, query_string):
        self.query_string = query_string
        self.url = "https://fanyi.baidu.com/transapi"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
        }

    def get_post_data(self):
        post_data = {
            'from': 'en',
            'to': 'zh',
            'query': self.query_string
        }
        return post_data

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return response.content.decode()

    def get_data(self, json_str):
        temp_dict = json.loads(json_str)
        ret = temp_dict['data'][0]['dst']
        print("翻译结果：%s" % ret)

    def run(self):
        post_data = self.get_post_data()
        json_str = self.parse_url(self.url, post_data)
        self.get_data(json_str)


if __name__ == '__main__':
    string = input("请输入要翻译的字符：")
    fanyi = Fanyi(string)
    fanyi.run()
