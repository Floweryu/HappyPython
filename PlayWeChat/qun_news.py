# -*- coding:utf-8 -*-
# Time: 2019-05-05 19:27:22
# Auther: ZhangJunFeng

import itchat

itchat.auto_login()
groups = itchat.get_chatrooms(update=True)  # 获取所有的群
for g in groups:
    print(g['UserName'])
    print(g['NickName'])