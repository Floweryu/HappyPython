# -*- coding:utf-8 -*-
# Time: 2019-05-03 13:47:15
# Auther: ZhangJunFeng

import requests
from lxml import etree
import os


class Spider(object):
    def start_request(self):
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.text)
        title_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        href_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        for title, href in zip(title_list, href_list):
            if os.path.exists(title) is False:
                os.mkdir(title)
            self.next_file(title, href)

    def next_file(self, title, href):
        response = requests.get("http:" + href)
        html = etree.HTML(response.text)
        fiction_little_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        fiction_href_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        for fiction_little, fiction_href in zip(fiction_little_list, fiction_href_list):
            self.download_file(fiction_little, fiction_href, title)

    def download_file(self, fiction_little, fiction_href, title):
        response = requests.get("http:" + fiction_href)
        html = etree.HTML(response.text)
        content = "\n".join(html.xpath('//div[@class="read-content j_readContent"]/p/text()'))

        filename = title + "\\" + fiction_little + ".txt"
        print("正在保存小说文件：" + filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)


spider = Spider()
spider.start_request()