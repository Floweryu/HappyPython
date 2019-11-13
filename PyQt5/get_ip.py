# -*- coding:utf-8 -*-
# Time: 2019-05-09 10:40:59
# Auther: ZhangJunFeng

import geoip2.database
import tkinter


class Error(Exception):
    pass


class FindLocation(object):
    def __init__(self):
        self.reader = geoip2.database.Reader(r"D:\Useful_Install\GeoLite2-City_20190507\GeoLite2-City.mmdb")
        # 创建主窗口
        self.root = tkinter.Tk()
        self.root.title('全球定位IP地址(离线)')
        # 创建一个输入框，并设置尺寸
        self.ip_input = tkinter.Entry(self.root, width=30)
        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)
        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.find_position, text="查询")
        self.ip_addr = None

    # 完成布局
    def gui_arrange(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    # 查找 IP 地址
    def find_position(self):
        # 获取输入信息
        self.ip_addr = self.ip_input.get()  # 从输入框得到信息
        try:
            response = self.reader.city(self.ip_addr)
        except ValueError:
            print("The address %s is not in the database." % self.ip_addr)
        else:
            # 获取目标城市
            city = response.city.name
            # 获取目标国家
            country = response.country.name
            # 获取目标省份
            subdivsions = response.subdivisions.most_specific.name
            # 获取目标经度
            longitude = response.location.longitude
            # 获取目标纬度
            latitude = response.location.latitude

            # 创建临时列表
            the_ip_info = ["所在纬度:" + str(latitude), "所在经度:" + str(longitude), "省份:" + str(subdivsions),
                           "所在城市:" + str(city), "所在国家或地区:" + str(country), "需要查询的ip:" + str(self.ip_addr)]
            # 清空回显列表可见部分
            for item in range(10):
                self.display_info.insert(0, "")

            # 为回显列表赋值
            for item in the_ip_info:
                self.display_info.insert(0, item)


if __name__ == "__main__":
    find = FindLocation()
    find.gui_arrange()
    tkinter.mainloop()