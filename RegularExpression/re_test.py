# -*- coding:utf-8 -*-
# Time: 2019-05-02 12:10:20
# Auther: ZhangJunFeng

import re

# 在字符串中匹配字符
pattern1 = 'yue'  # 原子
string = "http://yum.iqianyue.com"
result1 = re.search(pattern1, string)  # 在字符串中寻找原子
print(result1)

pattern2 = "\n"
string2 = '''http://yum.iqianyue.com
http://baidu.com'''
result2 = re.search(pattern2, string2)
print(result2)

pattern3 = "\\w\\dpython\\w"
string3 = "abcdfphp355pythony_asidis"
result3 = re.search(pattern3, string3)
print(result3, "\n")

pattern4 = "\\w\\dpython[xyz]\\w"
pattern5 = "\\w\\dpython[^xyz]\\w"
pattern6 = "\\w\\dpython[xyz]\\W"
string4 = "abcdfphp355pythony_asidis"
result4 = re.search(pattern4, string4)
result5 = re.search(pattern5, string4)
result6 = re.search(pattern6, string4)
print(result4)
print(result5)
print(result6)

pattern7 = ".python..."
string7 = "abcdfphp355pythony_asidis"
result7 = re.search(pattern7, string7)
print(result7, "\n")

pattern8 = "^abd"
pattern9 = "^abc"
pattern10 = "py$"
pattern11 = "ay$"
string8 = "abcdfphp355pythony_asidpy"
result8 = re.search(pattern8, string8)
result9 = re.search(pattern9, string8)
result10 = re.search(pattern10, string8)
result11 = re.search(pattern11, string8)
print(result8)
print(result9)
print(result10)
print(result11)
print("\n")

pattern12 = "py.*n"
pattern13 = "cd{2}"
pattern14 = "cd{3}"
pattern15 = "cd{2,}"
string9 = "abcdddfphp345pythony_py"
result12 = re.search(pattern12, string9)
result13 = re.search(pattern13, string9)
result14 = re.search(pattern14, string9)
result15 = re.search(pattern15, string9)
print(result12)
print(result13)
print(result14)
print(result15)
print("\n")

pattern16 = "python|php"        # 二选一匹配
string16 = "abcdddfphp345pythony_py"
result16 = re.search(pattern16, string16)
print(result16)
print("\n")

pattern17 = "\\d+(?=\\.)"
pattern18 = "\\d+(?!\\.)"
string17 = "4563.141"
result17 = re.search(pattern17, string17)
result18 = re.search(pattern18, string17)
print(result17)
print(result18, "\n")

pattern19 = "p.*y"      # 贪婪模式
pattern20 = "p.*?y"     # 非贪婪模式
string18 = "abcdddfphp345pythony_py"
result19 = re.search(pattern19, string18)
result20 = re.search(pattern20, string18)
print(result19)
print(result20)