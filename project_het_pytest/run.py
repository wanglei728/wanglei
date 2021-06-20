"""
@Time : 2021/6/19 16:00
@Author : 
"""
import pytest

# 1、通过html HTMLTestRunne生成报告
# pytest.main(["test_demo04_pytest数据驱动.py", "--html=reports/1.html"])

# 2、log 文本
# pytest.main(["test_demo04_pytest数据驱动.py", "--resultlog=reports/2.txt"])

# 3、xml文件
# pytest.main(["test_demo04_pytest数据驱动.py", "--junitxml=reports/3.xml"])

# ----上述三种不推荐，推荐allure


# pytest框架运行程序,通过allure生成报告
pytest.main(["--alluredir=allure_reports"])
