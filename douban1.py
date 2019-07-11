#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time : 2019/7/8 19:58
# @Author : Aries # @Site : 
# @File : douban1.py
# @Software: PyCharm

from urllib.request import urlopen
from urllib import  request
from bs4 import BeautifulSoup
import  pymysql,time
#
list_rank=[]  #用于存放排名
list_name=[]  #用于存放电影名
list_quote=[]  #用于存放电影简介
list_site=[]  #用于存放电影网址

def getData(url):
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

    bs_quote=bs_ol.findAll('p',class_='quote')
    for each in bs_quote:
        list_quote.append(each.find('span',class_='inq').text)
    print(list_quote)


#mysql

def create():
    db=pymysql.connect('localhost','root','123','testdb')
    cursor=db.cursor()
    cursor.execute("DROP TABLE IF EXISTS douban")
    cursor.execute('create table douban (id int primary key, name varchar(20), quote varchar(200))      ')
    db.close()
    print('create table Successfully!')
def  insert(value):
    db=pymysql.connect('localhost','root','123','testdb')
    cursor=db.cursor()
    cursor.execute('insert into douban (id,name,quote) values(%s,%s,%s)',value)
    db.commit()
    db.close()
    print('ok')

# create()
# for i in range(len(list_name)):
#     value=(int(list_rank[i]),list_name[i],list_quote[i])
#     insert(value)
# print('ok..')


#一个函数，能够根据给定的页数获取对应的url，以及该url下的数据。

def returnData(pageNum):
    defaultUrl='https://movie.douban.com/top250'

    for i in range(0,pageNum):
            page=i*25
            url=defaultUrl+'?start='+str(page)+'&filter='
            print(url)

        #模拟浏览器
        # headers=('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        #                       '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        # opener=request.build_opener()
        # opener.addheaders=[headers]
        # data=opener.open(url).read().decode('utf-8')
        # print(data)

returnData(2)



    # url='https://movie.douban.com/top250'+'?start='+str(pageNum-1)
    # https://movie.douban.com/top250
    # https: // movie.douban.com / top250?start = 25 & filter =
    # https: // movie.douban.com / top250?start = 50 & filter =












