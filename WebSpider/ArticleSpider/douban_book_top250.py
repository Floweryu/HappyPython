# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import requests
from bs4 import BeautifulSoup

all_titles = []
all_infos = []
all_rate_nums = []
all_hrefs = []
all_comments = []


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(content):
    soup = BeautifulSoup(content, 'lxml')
    tables = soup.find("div", class_="indent").find_all("table")
    for table in tables:
        title = table.find("div", class_="pl2").find("a").get_text()\
                    .replace("\n", " ").replace(" ", "").strip()
        rate_num = table.find("span", class_="rating_nums").get_text()
        info = table.find("p", class_="pl").get_text()
        comment = table.find("span", class_="inq").get_text()
        href = table.find("div", class_="pl2").find("a").get("href")

        all_titles.append(title)
        all_rate_nums.append(rate_num)
        all_infos.append(info)
        all_hrefs.append(href)
        all_comments.append(comment)


def write_file():
    filename = "douban_book_top250.txt"
    with open(filename, "a", encoding="utf-8") as fp:
        for x in range(25):
            fp.write(all_titles[x] + "\t")
            fp.write(all_rate_nums[x] + "\n")
            fp.write(all_comments[x] + "\n")
            fp.write(all_hrefs[x] + "\n")
            fp.write(all_infos[x] + "\n\n")


def main(offset):
    url = "https://book.douban.com/top250?start=" + str(offset)
    html = get_page(url)
    if html:
        parse_page(html)
        # print(len(all_titles), len(all_rate_nums), len(all_comments), len(all_hrefs), len(all_infos))
        write_file()


if __name__ == '__main__':
    # for i in range(5):
        main(50)
