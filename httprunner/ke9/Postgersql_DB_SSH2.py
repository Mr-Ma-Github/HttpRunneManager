# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-15 22:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------

import psycopg2
from sshtunnel import SSHTunnelForwarder

SSHconf = {"ssh_address_or_host": ('52.83.166.21', 22),  # 指定ssh登录的跳转机的address
            "ssh_username": 'centos',
            "ssh_pkey": "M:\My\工作\数据库私钥\pre-portal.pem",  # 设置密钥
            "ssh_private_key_password": "123456",
            "remote_bind_address": ('52.83.166.21', 5432)}  # 设置数据库服务地址及端口
DBconf = {"database": "clinical_release",
           "user": "postgres",
           "password": "postgresm93wcf",
           "host": "127.0.0.1"  # host、port 固定
           }
class DbConnect():
    def __init__(self, ssh_conf=SSHconf, db_conf=DBconf):
        self.ssh_conf = ssh_conf
        self.db_cof = db_conf
        self.server = SSHTunnelForwarder(**ssh_conf)
        self.server.start()
        # 打开数据库连接
        self.conn = psycopg2.connect(port=self.server.local_bind_port, **db_conf)
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()

    def select(self, sql):
        # sql查询语句
        self.cursor.execute(sql)
        print('执行',sql)
        # 使用列表推到的形式简洁直观
        coloumns = [row[0] for row in self.cursor.description]
        result = [[str(item) for item in row] for row in self.cursor.fetchall()]
        dict_result = [dict(zip(coloumns, row)) for row in result]
        return dict_result

    def execute(self, sql):
        # sql删除、提交、修改语句
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交修改
            self.conn.commit()
            print("sql执行成功", sql)
        except Exception as e:
            print('sql执行失败', sql)
            # 发生错误时回滚
            self.conn.rollback()
            raise e

    def close(self):
        # 关闭连接
        self.cursor.close()
        self.conn.close()
        self.server.close()

# 写两个函数用来调用查询和执行
def select_sql(sql):
    """执行查询"""
    db = DbConnect()
    results = db.select(sql)
    db.close()
    return results

def execute_sql(sql):
    """执行：新增、删除、修改"""
    db = DbConnect()
    results = db.execute(sql)
    db.close()

if __name__ == '__main__':
    # sql = '''INSERT INTO "public"."cr_patient"("id", "code", "name", "gender", "customer_code", "birth_date", "cellphone", "email", "cert_type",
    #              "cert_id", "note", "deleted", "patient_type_id", "created_by", "created_date", "last_modified_by",
    #              "last_modified_date", "doctor_id", "sale_id", "disease_course_audit_status",
    #              "disease_course_audit_reject_reason", "approved_disease_to_transfer_id", "cellphone2", "cellphone3",
    #              "birth_date_na", "patient_external_code", "external_institution_name", "sampling_employee_id",
    #              "disease_course_review_status", "count_for_material_complete_statistic", "has_icf")
    #         VALUES(7666, 'A00000', 'DELETE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'f', NULL, 'system',
    #              '2019-03-04 00:00:00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'f', NULL, NULL, NULL, 'f', 't',
    #              NULL);'''
    # sql = "select * from cr_patient where customer_code = 'X30000';"
    # sql = "delete from cr_patient WHERE customer_code = 'X30000';"
    # res = select_sql(sql)
    # print(res)
    # res = execute_sql(sql)

    res = execute_sql("""update cr_patient set note = '123' where id = 2546854;""")

