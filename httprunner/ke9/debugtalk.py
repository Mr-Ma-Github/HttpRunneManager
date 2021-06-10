# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import pymysql
import os


def ENV(keyname):
    '''读取环境变量'''
    value = os.environ.get("keyname")
    return value

dbconf = { "host": "1.15.92.116",
           "user": "root",
           "passwd": "123456",
           "port": 3309}


class DbConnect():
    def __init__(self, db_conf=dbconf, database=""):
        self.db_cof = db_conf
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_conf)  # cursorclass目的是为了让其返回字典，默认返回元祖类型
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # sql查询语句
        # sql = "select * from employee"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

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
        self.db.close()

# 写两个函数用来调用查询和执行
def select_sql(sql):
    """执行查询"""
    db = DbConnect(database="hrun")
    results = db.select(sql)
    db.close()
    return results

def execute_sql(sql):
    """执行：新增、删除、修改"""
    db = DbConnect(database="hrun")
    results = db.execute(sql)
    db.close()


if __name__ == '__main__':
    # db = DbConnect(database="hrun")
    # sql = db.select("select * from UserInfo")
    # print(sql)

    res = select_sql("select * from UserInfo")
    print(res)

    # res = execute_sql("INSERT INTO `hrun`.`UserInfo`(`id`, `create_time`, `update_time`, `username`, `password`, `email`, `status`) VALUES (3, '2021-03-02 23:49:43.669098', '2021-03-02 23:49:43.669131', 'haiyu.ma', 'password.1', '123@163.com', 1)")



