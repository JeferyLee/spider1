#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time : 2019/7/8 20:32
# @Author : Aries # @Site : 
# @File : 1.py
# @Software: PyCharm


import re
str1=" <span class title>肖申克的救赎</span>"

pat=r'^>(.*)<$'
print(re.match(pat,str1))
