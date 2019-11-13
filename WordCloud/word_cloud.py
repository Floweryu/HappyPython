# !/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_='Zhang Fengng'

from wordcloud import WordCloud
import PIL.Image as Image
import numpy as np

"""文本文档与该程序路径一样"""
with open(r"D:\Learn_Python\制作词云\meiwen.txt") as fp:

    """读取文档"""
    text = fp.read()

    """将图片信息转换成数组形式存储"""
    mask = np.array(Image.open(r"D:\Learn_Python\制作词云\images\love2.jpg"))

    """根据需要写入参数"""
    wordcloud = WordCloud(
        mask=mask
    ).generate(text)      # 根据文本生成词云

    image_produce = wordcloud.to_image()
    image_produce.show()
    wordcloud.to_file("D:\Learn_Python\制作词云\output\heart.jpg")
