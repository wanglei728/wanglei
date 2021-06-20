"""
@Time : 2021/6/13 15:11
@Author : 
"""
import unittest
from unittestreport import TestRunner
from project_het.common.handler_path import REPORT_DIR, CASES_DIR
from unittestreport.core.sendEmail import SendEmail


class RunTest:
    """测试用例执行启动入口"""

    def main_test(self):
        # 收集测试用例到套件
        suite = unittest.defaultTestLoader.discover(CASES_DIR)
        runner = TestRunner(suite, title="美业项目api测试报告", report_dir=REPORT_DIR, tester="test",
                            desc="美业三位一体项目",
                            filename="beautiful_report.html")
        # 执行用例
        runner.run()

        # 1、推送结果到钉钉群
        url = 'https://oapi.dingtalk.com/robot/send?access_token=2116b4cbd28465687dea22d4b533432' \
              'ccd2cc70568ea4ee865cd8836775aade7'
        runner.dingtalk_notice(url=url, key="测试")

        # # 2、通过runner对象中的send_email方法发送邮件
        # runner.send_email(host="smtp.qq.com", port=465, user="654101307@qq.com", password="snxfcjmkifvubfih",
        #                   to_addrs=["654101307@qq.com", "15921089253@163.com"],
        #                   is_file=True)

        # 3、通过SendEmail类发送邮件
        # email = SendEmail(host="smtp.qq.com", port=465, user="654101307@qq.com", password="snxfcjmkifvubfih")
        # email.send_email(subject="美业项目测试报告", content="详细报告内容请参考附件",
        #                  to_addrs=["654101307@qq.com", "15921089253@163.com"],
        #                  filename=r"D:\PyCharm\hetproject\project_het\allure_reports\beautiful_report.html")


if __name__ == '__main__':
    test = RunTest()
    test.main_test()
