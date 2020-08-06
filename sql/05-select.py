#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "Cyf@1985", "testdb", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# SQL 查询语句
sql = "select * from employee \
      where income > %s" % (1000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   results = cursor.fetchall()
   for row in results:
       fname = row[0]
       lname = row[1]
       age = row[2]
       sex = row[3]
       income = row[4]
       # 打印结果
       print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
except:
   # Rollback in case there is any error
   print("Error: unable to fecth data")
# 关闭数据库连接
db.close()
