"""
@Time : 2021/6/12 11:36
@Author : 
"""
import os, time
import unittest
from unittestreport import ddt, list_data
from project_het.common.handler_excel import HandlerExcel
from project_het.common.handler_path import DATA_DIR
from project_het.common.handler_config import my_config
from project_het.common.tools import replace_excel_data
from project_het.common.handler_logs import my_log
from project_het.testcases.fixture import BaesTest


@ddt
class TestWeb(unittest.TestCase, BaesTest):
    # 创建excel对象
    excel = HandlerExcel(filename=os.path.join(DATA_DIR, "cases_data.xlsx"), sheetname="web")
    cases_data = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        # 继承前置接口,参数传递
        cls.web_login()
        cls.get_session_account()
        cls.select_role_list()
        cls.get_dept_list()
        cls.get_by_dempid()
        cls.mobile_phone()

    @list_data(cases_data)
    def test_web(self, item):
        # 测试数据（url，method，headers，params,expected）
        url = my_config.get("env_release", "base_url") + item["url"]
        method = item["method"].lower()
        headers = {"content-type": item["content-type"]}
        expected = eval(item["expected"])
        # excel格式化参数替换
        item["data"] = replace_excel_data(cases_data=item["data"], cls=TestWeb)
        params = eval(item["data"])

        # 判断入参关键字，获取测试结果
        if item["method"].lower() == "get" or item["method"].lower() is None:
            response = self.s.request(method=method, url=url, params=params, headers=headers)
        elif item["content-type"] == "application/json":
            response = self.s.request(method=method, url=url, json=params, headers=headers)
        else:
            response = self.s.request(method=method, url=url, data=params, headers=headers)
        res = response.json()

        # try断言
        try:
            self.assertEqual(expected["code"], res["code"])
        except AssertionError as e:
            my_log.error("---用例---【{}】---执行失败".format(item["title"]))
            my_log.exception(e)
            # 测试结果写入excel
            self.excel.write_excel(row=item["case_id"] + 1, column=9, value="失败")
            raise e
        else:
            my_log.info("---用例---【{}】---执行成功".format(item["title"]))
            self.excel.write_excel(row=item["case_id"] + 1, column=9, value="成功")
        finally:
            self.excel.write_excel(row=1, column=9, value="测试结果")


if __name__ == '__main__':
    unittest.main()
