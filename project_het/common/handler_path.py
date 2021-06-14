"""
@Time : 2021/6/10 14:27
"""
import os

# 项目根目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
CONFIG_DIR = os.path.join(BASE_DIR, "config")

# 测试用例数据文件路径
DATA_DIR = os.path.join(BASE_DIR, "datas")

# 日志文件存储路径
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 报告存储所在根目录
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 测试用例类模块路径
CASES_DIR = os.path.join(BASE_DIR, "testcases")

