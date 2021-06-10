# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import psycopg2

# 打开数据库连接
db = psycopg2.connect(database="clinical_repository",
                        user='postgres',
                        password='postgres',
                        host='10.10.10.181',
                        port='5432')
# 方式一：
# cur = db.cursor()
# cur.execute("SELECT * FROM cr_user")
# data = cur.fetchall()
# print(data)
# db.commit()
# cur.close()
# db.close()

# 方式二：
# 以列表嵌套字典的方式返回数据
cursor = db.cursor()
cursor.execute("SELECT * FROM cr_user")
#使用列表推到的形式简洁直观
coloumns = [row[0] for row in cursor.description]
result = [[str(item) for item in row] for row in cursor.fetchall()]
dict_result = [dict(zip(coloumns, row)) for row in result]
print(dict_result)
cursor.close()
db.close()