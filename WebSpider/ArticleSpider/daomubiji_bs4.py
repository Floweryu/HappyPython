# -*- coding:utf-8 -*-
# Time: 2019-05-04 14:16:19
# Auther: ZhangJunFeng

import requests
from bs4 import BeautifulSoup

url = "http://seputu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/73.0.3683.103 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

full_list = []

mulu_list = soup.find_all("div", class_="mulu")
for mulu in mulu_list:
    # 寻找大标题
    big_title = mulu.find("div", class_="mulu-title")
    if big_title is not None:
        big_title = big_title.center.h2.text
        # 寻找小题目
        little_titles = mulu.find("div", class_="box").find_all("li")
        for title in little_titles:
            if title.a is not None:
                content = (big_title, title.a.text, title.a.get("href"))
                full_list.append(content)

filename = "盗墓笔记.txt"
with open(filename, "w", encoding="utf-8") as f:
    for full in full_list:
        f.write(str(full) + "\n")

