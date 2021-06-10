# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------

import psycopg2
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    # 指定ssh登录的跳转机的address
    ssh_address_or_host=('52.83.166.21', 22),
    ssh_username='centos',
    # 设置密钥
    ssh_pkey='M:\My\工作\数据库私钥\pre-portal.pem',
    ssh_private_key_password='123456',

    # 设置数据库服务地址及端口
    remote_bind_address=('52.83.166.21', 5432))
server.start()
conn = psycopg2.connect(database='clinical_release',
                        user='postgres',
                        password='postgresm93wcf',
                        host='127.0.0.1',  # host、port 固定
                        port=server.local_bind_port)
# 方式一：
# # 使用 cursor() 方法创建一个游标对象cur
# cur = conn.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cur.execute('select * from cr_patient where id = 7666;')
# # 使用 fetchall() 方法获取查询结果
# data = cur.fetchall()
# print(data)
# # 关闭数据库连接
# conn.close()
# server.close()

# 方式二：
# 以列表嵌套字典的方式返回数据
cursor = conn.cursor()
cursor.execute("SELECT * FROM cr_user")
#使用列表推到的形式简洁直观
coloumns = [row[0] for row in cursor.description]
result = [[str(item) for item in row] for row in cursor.fetchall()]
dict_result = [dict(zip(coloumns, row)) for row in result]
print(dict_result)
cursor.close()
conn.close()
server.close()