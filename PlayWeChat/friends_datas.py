# -*- coding:utf-8 -*-
# Time: 2019-05-05 10:45:36
# Auther: ZhangJunFeng

import itchat
import os
import math
import PIL.Image as Image
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud
import jieba
import re


class Weixin(object):
    def __init__(self):
        itchat.login()
        self.friends = itchat.get_friends(update=True)

    # 获取头像
    def head_img(self):
        # 获得列表好友的下标和信息
        for count, f in enumerate(self.friends):
            # 根据username获取头像
            img = itchat.get_head_img(userName=f["UserName"])
            imgfile = open("img/" + str(count) + ".jpg", "wb")
            imgfile.write(img)
            imgfile.close()

    # 头像拼接图
    @staticmethod
    def create_img():
        x = 0
        y = 0
        imgs = os.listdir("img")
        random.shuffle(imgs)
        # 创建640*640的图片用于填充小图片
        newimg = Image.new('RGBA', (640, 640))
        # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高
        width = int(math.sqrt(640 * 640 / len(imgs)))
        # 每行图片数
        numline = int(640 / width)

        for i in imgs:
            try:
                img = Image.open("img/" + i)
                # 缩小图片
                img = img.resize((width, width), Image.ANTIALIAS)
                # 拼接图片，一行排满，换行拼接
                newimg.paste(img, (x * width, y * width))
                x += 1
                if x >= numline:
                    x = 0
                    y += 1
            except IOError:
                print("img/ %s cannot open" % i)
        newimg.save("all.png")

    # 性别统计
    def get_sex(self):
        sex = dict()  # 创建空字典
        for f in self.friends:
            if f["Sex"] == 1:  # 男
                sex["man"] = sex.get("man", 0) + 1
            elif f["Sex"] == 2:  # 女
                sex["women"] = sex.get("women", 0) + 1
            else:  # 未知
                sex["unknow"] = sex.get("unknow", 0) + 1
        # 柱状图展示
        for i, key in enumerate(sex):
            plt.bar(key, sex[key])
        plt.savefig("getsex.png")
        plt.ion()
        plt.pause(5)  # 图片显示5s
        plt.close()

    # 获取个性签名
    def get_signature(self):
        file = open('sign.txt', 'a', encoding='utf-8')
        for f in self.friends:
            signature = f["Signature"].strip().replace("emoji", "").replace("span", "").replace("class", "")
            rec = re.compile(r"1f\d+\w*|[<>/=]")
            signature = rec.sub("", signature)
            file.write(signature + "\n")

    # 生成词云图
    @staticmethod
    def create_word_cloud(filename):
        # 读取文件内容
        text = open("{}.txt".format(filename), encoding="utf-8").read()

        # 注释部分用结巴分词
        # worldlist = jieba.cut(text, cut_all=True)
        # wl = " ".join(worldlist)
        # 设置词云
        wc = WordCloud(
            # 设置背景颜色
            background_color="white",
            # 设置最大显示的词云数
            max_words=2000,
            # 选择字体
            font_path=r"C:\Windows\Fonts\simfang.ttf",
            height=500,
            width=500,
            # 设置字体最大值
            max_font_size=60,
            # 设置配色方案
            random_state=30,
        )

        myword = wc.generate(text)  # 生成词云
        plt.imshow(myword)
        plt.axis("off")
        plt.show()
        wc.to_file("signature.png")


wechat = Weixin()
wechat.head_img()
wechat.create_img()
wechat.get_sex()
wechat.get_signature()
wechat.create_word_cloud("sign")
