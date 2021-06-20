"""
@Time : 2021/6/19 14:56
@Author : 
"""
import random, re
from project_het_pytest.common.handler_config import my_config


def replace_excel_data(cases_data, cls):
    """创建替换excel用例字段数据方法"""
    while re.search("#(.+?)#", cases_data):
        res = re.search("#(.+?)#", cases_data)
        item = res.group()
        attr = res.group(1)
        try:
            value = getattr(cls, attr)
        except AttributeError:
            value = my_config.get("env_release", attr)
        cases_data = cases_data.replace(item, str(value))
    return cases_data


def add_phone():
    """随机生成手机号方法"""
    phone = "159"
    for i in range(8):
        p = str(random.randint(1, 9))
        phone += p
    return phone


if __name__ == '__main__':
    phone_x = add_phone()
    print(phone_x)


    class Testdatas:
        id = "123"
        name = "wanglei"
        data = "cases"
        title = "测试"
    s = '{"id"：“#id#”, "name":"#name#", "data":"#data#","title","#title#"}'
    # 调用方法
    a = replace_excel_data(cases_data=s, cls=Testdatas)
    print(a)
