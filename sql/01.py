import pymysql

#连接数据库
db = pymysql.connect("localhost","root","Cyf@1985","testdb")

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM userinfo")

#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)

#关闭游标和数据库的连接
cursor.close()
db.close()

#运行结果
# ((1, 'frank', '123'), (2, 'rose', '321'), (3, 'jeff', '666'))