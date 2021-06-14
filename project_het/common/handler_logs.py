"""
@Time : 2021/6/10 15:03
@Author : 
"""
import logging
import os
from project_het.common.handler_config import my_config
from project_het.common.handler_path import LOG_DIR


# 封装日志收集器方法
def create_logs(name, log_level, sh_level, fh_filename, fh_level):
    """
    :param name:日志收集器对象名称
    :param log_level:日志收集等级
    :param sh_level:控制台输出日志等级
    :param fh_filename:日志输出到文件名称
    :param fh_level:文件输出日志等级
    :return:
    """
    # 第一步：创建日志收集器并设置收集等级
    log = logging.getLogger(name=name)
    log.setLevel(level=log_level)

    # 第二步：创建日志输出渠道，设置收集等级
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    fh = logging.FileHandler(filename=fh_filename, encoding="utf-8")
    fh.setLevel(fh_level)

    # 第三步：日志收集器绑定输出渠道
    log.addHandler(sh)
    log.addHandler(fh)

    # 第四步：设置日志输出格式进行绑定日志输出渠道
    log_format = logging.Formatter("%(asctime)s---%(filename)s---%(lineno)d--- %(levelname)s:%(message)s")
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    return log


# 调用方法生成日志收集器
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
