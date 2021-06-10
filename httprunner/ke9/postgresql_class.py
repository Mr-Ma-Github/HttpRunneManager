# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import psycopg2

# # 打开数据库连接
# db = psycopg2.connect(database="clinical_repository",
#                         user='postgres',
#                         password='postgres',
#                         host='10.10.10.181',
#                         port='5432')
# cur = db.cursor()
# cur.execute("SELECT * FROM cr_user")
# data = cur.fetchall()
# print(data)
# db.commit()
# cur.close()
# db.close()
# --------------------------------------------------------------------------------------------------------
import psycopg2

dbconf = { "host": "10.10.10.181",
           "user": "postgres",
           "password": "postgres",
           "port": 5432}

class DbConnect():
    def __init__(self, db_conf=dbconf, database=""):
        self.db_cof = db_conf
        # 打开数据库连接
        self.db = psycopg2.connect(database=database, **db_conf)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # sql查询语句
        self.cursor.execute(sql)
        # 使用列表推到的形式简洁直观
        coloumns = [row[0] for row in self.cursor.description]
        result = [[str(item) for item in row] for row in self.cursor.fetchall()]
        dict_result = [dict(zip(coloumns, row)) for row in result]
        return dict_result

    def execute(self, sql):
        # sql删除、提交、修改语句
        # sql = "delete form employee where age > 20"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.cursor.close()
        self.db.close()

# 写两个函数用来调用查询和执行
def select_sql(sql):
    """执行查询"""
    db = DbConnect(database="clinical_repository")
    results = db.select(sql)
    db.close()
    return results

def execute_sql(sql):
    """执行：新增、删除、修改"""
    db = DbConnect(database="clinical_repository")
    results = db.execute(sql)
    db.close()


if __name__ == '__main__':
    res = select_sql("select * from cr_user")
    print(res)




