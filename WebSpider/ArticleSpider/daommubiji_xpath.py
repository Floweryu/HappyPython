# -*- coding:utf-8 -*-
# Time: 2019-05-04 16:50:44
# Auther: ZhangJunFeng

from lxml import etree
import requests

url = "http://seputu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/73.0.3683.103 Safari/537.36"
}

full_list = []
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
mulu_list = html.xpath('//div[@class="mulu"]')
for mulu in mulu_list:
    # 篇名
    big_tittes = mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    # 章节名
    little_titles = mulu.xpath('./div[@class="box"]/ul/li/a/text()')
    # 链接
    href_list = mulu.xpath('./div[@class="box"]/ul/li/a/@href')
    for little_title, href in zip(little_titles, href_list):
        content = (big_tittes, little_title, href)
        full_list.append(content)

filename = "盗墓笔记xpath.txt"
with open(filename, "w", encoding="utf-8") as f:
    for full in full_list:
        f.write(str(full) + "\n")