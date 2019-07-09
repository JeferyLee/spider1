#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time : 2019/7/8 19:58
# @Author : Aries # @Site : 
# @File : douban1.py
# @Software: PyCharm

from urllib.request import urlopen

from bs4 import BeautifulSoup

list_rank=[]  #用于存放排名
list_name=[]  #用于存放电影名
list_descrip=[]  #用于存放电影简介
list_site=[]  #用于存放电影网址
url="https://movie.douban.com/top250"
res=urlopen(url)
data=res.read().decode('utf-8')
bs1=BeautifulSoup(data,'lxml')
bs_ol=bs1.find('ol',class_='grid_view')




