"""
@Time : 2021/6/10 15:28
@Author : 
"""
import random
import re
from project_het.common.handler_config import my_config


# 通过正则定义替换测试用例入参数据方法


def replace_excel_data(cases_data, cls):
    """创建替换excel用例字段数据方法"""
    while re.search("#(.+?)#", cases_data):  # while循环控制查找excel测试用例数据有多少##格式字段
        res = re.search("#(.+?)#", cases_data)  # 获取一个该正则格式的字段
        item = res.group()  # 获取被替换字段格式：#字段名#
        attr = res.group(1)  # 获取被替换字段名：字段名
        # try语句判断字段是在类属性 or 配置文件
        try:
            value = getattr(cls, attr)
        except AttributeError:
            value = my_config.get("env_release", attr)
        # 数据替换
        cases_data = cases_data.replace(item, str(value))
    return cases_data


def mobile_phone():
    """创建一个随机生成手机号的方法"""
    phone = "159"
    for i in range(8):
        v = str(random.randint(0, 9))
        phone += v
    return phone


if __name__ == '__main__':
    class Testdatas:
        id = "123"
        name = "wanglei"
        data = "cases"
        title = "测试"


    s = '{"id"：“#id#”, "name":"#name#", "data":"#data#","title","#title#"}'
    # 调用方法
    a = replace_excel_data(cases_data=s, cls=Testdatas)
    print(a)

    phone_x = mobile_phone()
    print(phone_x)
