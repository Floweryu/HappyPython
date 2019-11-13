# -*- coding:utf-8 -*-
# Time: 2019-05-02 15:06:57
# Auther: ZhangJunFeng

import re

# 匹配网站地址
pattern_1 = "[a-zA-Z]+://[^\\s]*[.com|.cn]"
string_1 = "<a href='http://www.baidu.com'>百度首页</a>"
result_1 = re.search(pattern_1, string_1)
print(result_1)

# 匹配电话号码
pattern_2 = r"\d{4}-\d{7}|\d{3}-\d{8}"
string_2 = "021-6728263653682382265236"
result_2 = re.search(pattern_2, string_2)
print(result_2)

# 匹配邮箱地址
pattern_3 = r"\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string_3 = "<a href='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>"
result_3 = re.search(pattern_3, string_3)
print(result_3)
