# !/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_='Zhang Fengng'

import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import time

# 用来存储所有页面的 url
PAGE_URLS = []


def parse_page(page_url):
    # 对请求身份进行伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    # 获取网页源代码
    response = requests.get(page_url, headers=headers)
    text = response.text
    # 解析源代码
    soup = BeautifulSoup(text, 'lxml')
    # attrs 指寻找的条件
    img_list = soup.find_all("img", attrs={"class": "lazy image_dtb img-responsive"})

    for img in img_list:
        img_url = img['data-original']
        # https://ws1.sinaimg.cn/bmiddle/9150e4e5ly1fd8nsyuvbog204602zjsu.gif
        # 对网址进行分割取最后一个元素
        filename = img_url.split("/")[-1]
        # 创建图片的存储路径，'join' 拼接路径
        full_path = os.path.join("images", filename)
        # 下载图片
        request.urlretrieve(img_url, full_path)
        print("%s下载完成！！" % filename)


def main():
    start = time.time()
    # 1, 先获取所有页面的 url
    for x in range(1, 10):
        page_url = "https://www.doutula.com/article/list/?page=" + str(x)
        PAGE_URLS.append(page_url)
    # 2, 解析每一个页面的数据
    for page_url in PAGE_URLS:
        parse_page(page_url)
    end = time.time()
    print(end-start)


if __name__ == '__main__':
    main()
