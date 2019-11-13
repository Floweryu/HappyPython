# -*- coding:utf-8 -*-
# Time: 2019-05-05 15:08:21
# Auther: ZhangJunFeng

import os
import re
import time
import itchat
from itchat.content import *

# 说明：可以撤回的有文本文字、语音、视频、图片、名片、分享、附件

msg_dict = {}

# 文件存储临时目录
filename = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
os.makedirs(filename)  # 创建以时间命名文件夹名

face_bug = None

# 将接收到 Friends and Groups 的消息存放在字典中并对字典进行更新
@itchat.msg_register([TEXT, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isGroupChat=True)
def get_msg_from(msg):
    global face_bug
    global msg_from
    msg_qun = None
    # 获取的是本地时间戳并格式化本地时间戳
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 如果是群消息
    if '@@' in str(msg['ToUserName']) or '@@' in str(msg['FromUserName']):
        msg_qun = msg['User']['NickName']       # 得到群昵称
        from_user = msg["FromUserName"]         # 得到发送者的ID
        friends = itchat.get_friends(update=True)  # 获取所有好友
        for f in friends:
            if from_user == f['UserName']:  # 根据ID判断是否是好友发的
                if f['RemarkName']:         # 如果有备注名
                    msg_from = f['RemarkName']
                else:
                    msg_from = f['NickName']
                break
    # 如果是好友消息
    else:
        if itchat.search_friends(userName=msg['FromUserName'])['RemarkName']:       # 优先使用备注名称
            msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']
        else:
            msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']  # 好友昵称

    msg_id = msg['MsgId']            # 消息ID
    msg_time = msg['CreateTime']     # 消息时间
    msg_content = None               # 消息内容
    msg_share_url = None             # 分享的链接

    # 若发送的消息是文本或好友推荐
    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
        msg_content = msg['Text']
    # 若发送的消息是录音、图片、视频
    elif msg['Type'] == 'Recording' or msg['Type'] == 'Picture' or msg['Type'] == msg['Video']:
        msg_content = msg['FileName']   # 内容就是文件名
        msg['Text'](filename + str(msg_content))     # 保存文件
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_share_url = msg['Url']

    face_bug = msg_content

    # 更新字典
    msg_dict.update(
        {
            msg_id: {
                "msg_qun": msg_qun,
                "msg_from": msg_from,
                "msg_time": msg_time,
                "msg_time_rec": msg_time_rec,
                "msg_type": msg["Type"],
                "msg_content": msg_content,
                "msg_share_url": msg_share_url
            }
        }
    )


# 收到 NOTE 类的通知，收集 Friends 和 Group 撤回的消息并发给助手
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True)
def send_msg_helper(msg):
    global face_bug
    if "撤回了一条消息" in msg['Content']:
        # 获取消息的id
        old_msg_id = re.search("<msgid>(.*?)</msgid>", msg['Content']).group(1)
        old_msg = msg_dict.get(old_msg_id)  # 得到该消息的字典文件

        # 如果发送的是表情包
        if len(old_msg_id) < 11:
            itchat.send_file(filename + face_bug, toUserName='filehelper')
            os.remove(filename + face_bug)
        else:
            if '@@' in str(msg['ToUserName']) or '@@' in str(msg['FromUserName']):
                msg_body = "告诉你一个秘密~~" + "\n" \
                           + old_msg.get('msg_time_rec') + "\n" \
                           + "【" + old_msg.get('msg_qun') + "】\n"\
                           + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息：" + "\n" \
                           + r"" + old_msg.get('msg_content')
            else:
                msg_body = "告诉你一个秘密~~" + "\n" \
                           + old_msg.get('msg_time_rec') + "\n" \
                           + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息：" + "\n" \
                           + r"" + old_msg.get('msg_content')
            # 如果是分享存在链接
            if old_msg['msg_type'] == "Sharing":
                msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')

            # 将撤回消息发送到文件助手
            itchat.send(msg_body, toUserName='filehelper')

            # 有文件的话也要将文件发送回去
            if old_msg["msg_type"] == "Picture" \
                    or old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = '@fil@%s' % (filename + old_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(filename + old_msg['msg_content'])

            # 删除字典旧消息
            msg_dict.pop(old_msg_id)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
