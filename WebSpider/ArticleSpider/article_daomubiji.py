# -*- coding:utf-8 -*-
# Time: 2019-10-03 18:26:43
# Auther: ZhangJunFeng

import requests
from lxml import etree
import threading


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

page_urls = []


def poducer():
    for i in range(1, 10):
        url = 'http://www.daomubiji.org/' + str(i) + '.html'
        page_urls.append(url)


def consumer():
    page_url = page_urls.pop()
    response = requests.get(page_url, headers=headers)
    html = etree.HTML(response.text)
    title = html.xpath('//div[@class="bg"]/h1/text()')
    print(title)


def main():
    for x in range(5):
        th = threading.Thread(target=poducer())
        th.start()
    for x in range(5):
        th = threading.Thread(target=consumer())
        th.start()


if __name__ == '__main__':
    main()