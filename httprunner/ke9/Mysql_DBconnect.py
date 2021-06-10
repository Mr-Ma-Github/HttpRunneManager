# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:02 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import pymysql

# 打开数据库连接
db = pymysql.connect(host='47.104.x.x',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='test')

# 使用 cursor() 方法创建一个游标对象cur
cur = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cur.execute("select name, psw from user")

# 使用 fetchall() 方法获取查询结果
data = cur.fetchall()

print(data)

# 关闭数据库连接
db.close()