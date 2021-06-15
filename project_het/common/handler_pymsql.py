"""
@Time : 2021/6/5 13:03
@Author : wanglei
"""
import pymysql
from project_het.common.handler_config import my_config


class HandlerDB:

    def __init__(self, host, port, user, password):
        # 1、初始化方法封装连接数据库对象
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connect = pymysql.connect(host=self.host, port=self.port,
                                       user=self.user, password=self.password, charset="utf8")

    def find_one(self, sql):
        """封装查询第一条数据的方法"""
        with self.connect as cur:
            cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result

    def find_all(self, sql):
        """查询sql所有返回结果方法"""
        with self.connect as cur:
            cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    def find_count(self, sql):
        """sql执行完成之后，范湖数据条数"""
        with self.connect as cur:
            result = cur.execute(sql)
        cur.close()
        return result

    def connect_close(self):
        self.connect.close()


if __name__ == '__main__':
    data_base = HandlerDB(
        host=my_config.get("mysql", "host"),
        port=my_config.getint("mysql", "port"),
        user=my_config.get("mysql", "user"),
        password=my_config.get("mysql", "password")
    )
    res = data_base.find_all(sql="select * from futureloan.member limit 5")
    print(res)
    res1 = data_base.find_count(sql="select * from futureloan.member where mobile_phone = 15921089253")
    print(res1)
