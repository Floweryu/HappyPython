# -*- coding:utf-8 -*-
# Time: 2019-04-29 22:01:50
# Auther: ZhangJunFeng

"""分析微信好友性别，城市比例"""
from wxpy import *

'''
微信机器人登录有3种模式，
(1)极简模式:robot = Bot()
(2)终端模式:robot = Bot(console_qr=True)
(3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
'''
# 初始化机器人，选择缓存模式（扫码）登录
robot = Bot(cache_path=True)

# 获取好友、群、公众号信息
robot.chats()

# 获取好友的统计信息
Friends = robot.friends()
print(Friends.stats_text())
