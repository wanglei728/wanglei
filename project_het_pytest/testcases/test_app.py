"""
@Time : 2021/6/19 14:32
@Author : 
"""
import os, time
import pytest
import requests
from project_het_pytest.common.handler_config import my_config
from project_het_pytest.common.handler_logs import my_log
from project_het_pytest.common.handler_excel import HandlerExcel
from project_het_pytest.common.handler_path import DATA_DIR
from project_het_pytest.common.tools import replace_excel_data


class TestApp:
    excel = HandlerExcel(filename=os.path.join(DATA_DIR, "cases_data2.xlsx"), sheetname="app")
    cases = excel.read_excel()

    @pytest.mark.parametrize("item", cases)
    def test_app(self, item, test_applogin):
        """
        :param item: pytest框架通过parametrize实现数据驱动
        :param test_applogin: pytest 框架调用前置方法
        """
        # 1.测试数据（url，method,headers,data,expected）
        url = my_config.get("env_release", "base_url") + item["url"]
        method = item["method"]
        headers = {"content-type": item["content-type"]}
        expected = eval(item["expected"])

        # 前置方法获取需要保存的参数，并设置为类属性，如accessToken
        accessToken = test_applogin
        setattr(TestApp, "accessToken", accessToken)
        # 参数化获取入参
        item["data"] = replace_excel_data(cases_data=item["data"], cls=TestApp)
        params = eval(item["data"])

        # 2、调用被测接口
        if item["method"].lower() == "get" or item["method"].lower() is None:
            response = requests.request(method=method, url=url, params=params, headers=headers)
        elif item["content-type"] == "application/json":
            response = requests.request(method=method, url=url, json=params, headers=headers)
        else:
            response = requests.request(method=method, url=url, data=params, headers=headers)
        res = response.json()

        # 3、断言
        try:
            assert(expected["code"], res["code"])
        except AssertionError as e:
            my_log.error("---用例---【{}】---执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("---用例---【{}】---执行成功".format(item["title"]))



