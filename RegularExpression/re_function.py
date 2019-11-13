# -*- coding:utf-8 -*-
# Time: 2019-05-02 14:26:38
# Auther: ZhangJunFeng

import re
string = "hellomypythonhispythonoutpythonend"
pattern_1 = re.compile(".python.")    # 预编译
result_1 = pattern_1.findall(string)
print(result_1)

pattern_2 = ".python."
result_2 = re.compile(pattern_2).findall(string)
print(result_2, "\n")

pattern_3 = "python."
result_3 = re.sub(pattern_3, "AAA", string)
result_4 = re.sub(pattern_3, "AAA", string, count=2)
print(result_3)
print(result_4)