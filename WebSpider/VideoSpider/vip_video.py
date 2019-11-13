# -*- coding:utf-8 -*-
# Time: 2019-05-07 18:48:44
# Auther: ZhangJunFeng

import requests
import time

print("开始下载")
url = 'http://lmsjy.qq.com/www/y0030qi20vs.mp4?vkey=' \
      '348424080BEA1DD3AF4352A63E884D6B51E772A8F825449700983D102AA44AF37247D460C766777A351D29815' \
      'E828A52651111E8DB43FFC8C464EC8CD4E0F3D9B3CE74F3EA17A3F1B197B6367D3DCE1E6B2E70414A2D2F51FED6B70944D'
r = requests.get(url, stream=True)
video_size = int(r.headers['Content-Length'])
temp_size = 0

filename = "video\\speed&&love.mp4"
time1 = time.time()
with open(filename, "wb") as mp4:
    mp4.write(r.content)
time2 = time.time()
print("下载结束, 用时：" + str(time2 - time1) + "'s")

