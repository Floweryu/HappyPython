# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import requests

from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

response = requests.get("http://www.666n.com/meiwenshangxi/977.html", headers=headers)
response.encoding = 'utf-8'
text = response.text
soup = BeautifulSoup(text, 'lxml')
article = soup.find(id="CntArticle")

filename = 'sanwen.txt'
with open(filename, 'w', encoding="utf-8") as f:
    f.write(article.text)


