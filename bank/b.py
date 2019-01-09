#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

import re
s = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3".encode()
print(s)
temp = s.decode('utf-8')
pattern=r"[\u4e00-\u9fa5]+"#中文正则表达式

regex = re.findall(pattern,temp) #生成正则对象
# results =  regex.findall(temp)#匹配
# for result in results:#迭代遍历出内容
#     print (result) 
print(regex)