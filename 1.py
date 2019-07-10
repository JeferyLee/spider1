#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time : 2019/7/8 20:32
# @Author : Aries # @Site : 
# @File : 1.py
# @Software: PyCharm
import pymysql

db = pymysql.connect('localhost', 'root', '123', 'testdb')

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS douban")
# cursor.execute('create table douban (id int primary key auto_increment, name varchar(20),rank varchar(20)')
cursor.execute('create table douban      (    id INT primary key, name varchar(20)    )    ' )
print('ok~')
cursor.execute('insert into douban (id,name) values(%s,%s)',[1,'2'])
cursor.execute('insert into douban (id,name) values(%s,%s)',[2,'3'])
cursor.execute('insert into douban (id,name) values(%s,%s)',[7,'3'])
cursor.execute('insert into douban (id,name) values(%s,%s)',[3,'3'])
# cursor.execute('insert into douban (id,name) values(%s,%s)',[7,'3'])
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Michael'])

db.commit()

cursor.close()
print('ok~~')





