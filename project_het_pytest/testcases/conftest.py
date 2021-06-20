"""
@Time : 2021/6/19 16:31
@Author : 
"""
import time
import jsonpath
import pytest
import requests
from project_het_pytest.common.handler_config import my_config
from project_het_pytest.common.handler_sign import HandlerSign


@pytest.fixture(scope="class")
def test_applogin():
    """登录接口类级别前置"""
    # 1、测试数据（url,method,headers,params）
    url_login = my_config.get("env_release", "base_url") + "/v1/account/login"
    headers = eval(my_config.get("env_release", "headers_login"))
    params = {
        "account": my_config.getint("env_release", "account"),
        "password": my_config.get("env_release", "password_app"),
        "appId": my_config.get("env_release", "appId")}
    sign = HandlerSign(method="POST",
                       url=url_login,
                       data={"account": my_config.getint("env_release", "account"),
                             "appId": my_config.get("env_release", "appId"),
                             "password": my_config.get("env_release", "password_app"),
                             "timestamp": int(time.time() * 1000)},
                       appsecret=my_config.get("env_release", "appsecret"))
    params.update(sign.md5_sign())
    # 2、app登录
    response = requests.request(method="post", url=url_login, data=params, headers=headers)
    res = response.json()
    # print(res)
    # 3、获取token,通过全局变量
    global accessToken
    accessToken = jsonpath.jsonpath(res, "$..accessToken")[0]
    yield accessToken


if __name__ == '__main__':
    a = test_applogin()
    print(a)

