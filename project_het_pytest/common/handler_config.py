"""
@Time : 2021/6/19 14:36
@Author : 
"""
import os
from configparser import ConfigParser
from project_het_pytest.common.handler_path import CONFIG_DIR


class ReadConfig(ConfigParser):
    """封装读取配置文件"""

    def __init__(self, config_name):
        # 重写继承类的初始化方法
        super().__init__()
        self.config_name = config_name
        self.read(filenames=self.config_name, encoding="utf-8")


# 配置文件解释器对象
my_config = ReadConfig(config_name=os.path.join(CONFIG_DIR, "config.ini"))


if __name__ == '__main__':
    res = my_config.get("env_release", "username")
    print(res)
