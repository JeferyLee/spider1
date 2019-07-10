#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time : 2019/7/8 19:58
# @Author : Aries # @Site : 
# @File : douban1.py
# @Software: PyCharm

from urllib.request import urlopen

from bs4 import BeautifulSoup
import  pymysql
#
list_rank=[]  #用于存放排名
list_name=[]  #用于存放电影名
list_descrip=[]  #用于存放电影简介
list_site=[]  #用于存放电影网址
url="https://movie.douban.com/top250"
res=urlopen(url)
data=res.read().decode('utf-8')
bs1=BeautifulSoup(data,'lxml')
bs_ol=bs1.find('ol',class_='grid_view')
bs_hd=bs_ol.findAll('div',class_='hd')
for each in bs_hd:
    list_name.append(each.find('span',class_='title').text)
print(list_name)

bs_pic=bs_ol.findAll('div',class_='pic')
for each in bs_pic:
    list_rank.append(each.find('em').text)
print(list_rank)


#mysql


def create():
    db=pymysql.connect('localhost','root','123','testdb')
    cursor=db.cursor()
    cursor.execute("DROP TABLE IF EXISTS douban")
    cursor.execute('create table douban (id varchar(20) primary key, name varchar(20))')
    db.close()
    print('create table Successfully!')
def  insert(value):
    db=pymysql.connect('localhost','root','123','testdb')
    cursor=db.cursor()
    cursor.execute('insert into douban (id,name) values(%s,%s)',value)
    db.commit()
    db.close()
    print('ok')

create()
value=['a','b']
insert(value)
















