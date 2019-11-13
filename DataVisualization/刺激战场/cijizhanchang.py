# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import requests
import jsonpath
import pygal

filename = ""
count = 0
"""为了练习json文件的处理"""
"""锻炼列表和字典结合的处理方法"""


def get_data():
    response = requests.get("http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json")
    gun_datas = jsonpath.jsonpath(eval(response.text), "$..ldtw_f2")
    gun_names = jsonpath.jsonpath(eval(response.text), "$..dx_2a")
    """获取枪的信息"""
    for i in range(0, len(gun_datas)):
        datas = gun_datas[i][0]
        data = [int(datas['wl_45']), int(datas['sc_54']), int(datas['ss_d0']),
                int(datas['wdx_a7']), int(datas['zds_62'])]

        global filename
        filename = "guns" + str(i) + ".svg"
        make_rader(data)

    print(len(gun_names))
    print(len(gun_names[0]))

    """获取武器的名称"""
    for i in range(0, len(gun_names)):
        for j in range(0, len(gun_names[i])):
            names = gun_names[i][j]
            data_key = "mc_94"
            for key in names.keys():
                if key == data_key:
                    name = names[key]
                    print(name)
                    global count
                    count += 1
    print(count)


def make_rader(data):
    # 雷达图设计
    rader_chart = pygal.Radar()
    # 添加雷达图标题
    rader_chart.title = "AKM_性能"
    # 添加雷达图各顶点含义
    rader_chart.x_labels = ["威力", "射程", "射速", "稳定性", "子弹数"]
    rader_chart.add("AKM", data)
    global filename
    # 保存图片
    rader_chart.render_to_file(filename)


get_data()
