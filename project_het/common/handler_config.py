"""
@Time : 2021/6/10 14:50
@Author : 
"""
import os
from configparser import ConfigParser
from project_het.common.handler_path import CONFIG_DIR


class ReadConfig(ConfigParser):
    """封装读取配置文件"""

    def __init__(self, config_name):
        # 继承类ConfigParser初始化方法重写
        super().__init__()
        self.config_name = config_name
        # 读取配置文件
        self.read(filenames=self.config_name, encoding="utf-8")


# 创建文件解释器对象
my_config = ReadConfig(config_name=os.path.join(CONFIG_DIR, "config.ini"))


if __name__ == '__main__':
    res = my_config.get("env_release", "username")
    print(res)


