"""
@Time : 2021/6/19 14:43
@Author : 
"""
import logging
import os
from project_het_pytest.common.handler_path import LOG_DIR
from project_het_pytest.common.handler_config import my_config


def create_logs(name, log_level, sh_level, fh_filename, fh_level):
    """
    :param name:日志收集器对象名称
    :param log_level:日志收集等级
    :param sh_level:控制台输出日志等级
    :param fh_filename:日志输出到文件名称
    :param fh_level:文件输出日志等级
    :return:
    """
    # 1、log收集器及等级
    log = logging.getLogger(name=name)
    log.setLevel(level=log_level)

    # 2、日志输输出渠道
    sh = logging.StreamHandler()
    sh.setLevel(level=sh_level)

    fh = logging.FileHandler(filename=fh_filename, encoding="utf-8")
    fh.setLevel(fh_level)

    # 3、日志收集器绑定输出渠道
    log.addHandler(sh)
    log.addHandler(fh)

    # 4、日志输出格式
    log_format = logging.Formatter("%(asctime)s---%(filename)s---%(lineno)d--- %(levelname)s:%(message)s")
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    return log


my_log = create_logs(
    name=my_config.get("logging", "name"),
    log_level=my_config.get("logging", "log_level"),
    sh_level=my_config.get("logging", "sh_level"),
    fh_level=my_config.get("logging", "fh_level"),
    fh_filename=os.path.join(LOG_DIR, my_config.get("logging", "fh_filename"))
)


if __name__ == '__main__':
    my_log.info("这是一条测试日志")
    my_log.error("这是一条错误日志")




