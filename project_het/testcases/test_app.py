"""
@Time : 2021/6/15 22:26
@Author : 
"""
import os, time
import unittest
import requests
from unittestreport import ddt, list_data
from project_het.common.handler_excel import HandlerExcel
from project_het.common.handler_logs import my_log
from project_het.common.handler_path import DATA_DIR
from project_het.testcases.fixture import BaesTest
from project_het.common.handler_config import my_config
from project_het.common.tools import replace_excel_data


@ddt
class TestApp(unittest.TestCase, BaesTest):
    # 创建excel对象
    excel = HandlerExcel(filename=os.path.join(DATA_DIR, "cases_data.xlsx"), sheetname="app")
    cases_data = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.app_login()

    @list_data(cases_data)
    def test_app(self, item):
        # 测试数据（url，method，headers，params,expected）
        url = my_config.get("env_release", "base_urlapp") + item["url"]
        method = item["method"].lower()
        headers = {"content-type": item["content-type"]}
        expected = eval(item["expected"])
        # excel格式化参数替换
        item["data"] = replace_excel_data(item["data"], TestApp)
        params = eval(item["data"])

        # 调用被测接口
        if item["method"].lower() == "get" or item["method"].lower() is None:
            response = requests.request(method=method, url=url, params=params, headers=headers)
        elif item["content-type"] == "application/json":
            response = requests.request(method=method, url=url, json=params, headers=headers)
        else:
            response = requests.request(method=method, url=url, data=params, headers=headers)
        res = response.json()

        # try断言
        try:
            self.assertEqual(expected["code"], res["code"])
        except AssertionError as e:
            my_log.error("---用例---【{}】---执行失败".format(item["title"]))
            my_log.exception(e)
            # 测试结果写入excel
            # self.excel.write_excel(row=item["case_id"] + 1, column=9, value="失败")
            raise e
        else:
            my_log.info("---用例---【{}】---执行成功".format(item["title"]))
            # self.excel.write_excel(row=item["case_id"] + 1, column=9, value="成功")


if __name__ == '__main__':
    unittest.main()
