# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import requests
from lxml import etree

response = requests.get("https://ibaotu.com/shipin/")
html = etree.HTML(response.text)
title_list = html.xpath('//span[@class="video-title"]/text()')
src_list = html.xpath('//div[@class="video-play"]/video/@src')
for title, src in zip(title_list, src_list):
    response = requests.get("http:" + src)
    filename = "video\\" + title + ".mp4"
    print("正在保存视频文件：" + filename)
    with open(filename, "wb") as f:
        f.write(response.content)