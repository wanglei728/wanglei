"""
@Time : 2021/6/12 11:36
@Author :
"""
import time
import random
import requests
import jsonpath
from project_het.common.handler_config import my_config


# noinspection PyUnresolvedReferences
class BaesTest:
    """封装测试用例类前置接口,测试用例类继承获取类属性"""

    @classmethod
    def web_login(cls):
        """web登录接口前置"""
        # *登录接口用例执行前置方法获取登录cookie（Python中采用session会话对象获取session）
        cls.s = requests.session()

        # 第一步：测试数据准备（url，method，headers，params）
        url_login = "".join(
            (my_config.get("env_release", "base_url"), "/v4/web/exhibitionhall/common/admin/loginCheck"))
        headers = eval(my_config.get("env_release", "headers_login"))
        params = {
            "username": my_config.get("env_release", "username"),
            "password": my_config.get("env_release", "password"),
            "_": int(time.time() * 1000)
        }
        # 第二步：调用登录接口
        response = cls.s.post(url=url_login, headers=headers, data=params)
        res = response.json()
        # print(res)

        # 第三步：保存前置接口的参数为类属性，方便后续接口调用
        cls.account = jsonpath.jsonpath(res, "$..userName")[0]

    @classmethod
    def get_session_account(cls):
        """前置获取登录信息，提取保留字段tenantId"""
        # 调用登录信息接口
        url = my_config.get("env_release", "base_url") + "/v4/web/exhibitionhall/auth/account/getSessionAccount"
        # 调用接口获取返回数据
        response = cls.s.get(url=url)
        res = response.json()
        # print(res)
        # 提取参数tenantId
        cls.tenantId = jsonpath.jsonpath(res, "$..tenantId")[0]
        # print(cls.tenantId)

    @classmethod
    def select_role_list(cls):
        """获取角色获取roleId"""
        url = my_config.get("env_release", "base_url") + "/v4/web/exhibitionhall/role/selectRole"
        params = {
            "tenantId": cls.tenantId,
            "pageIndex": 1,
            "pageRows": 10
        }
        response = cls.s.get(url=url, params=params)
        res = response.json()
        # 提取参数roleId、roles、fkRoleId,
        cls.roleId = jsonpath.jsonpath(res, "$..list[?(@.roleName=='角色自动化测试')][roleId]")[0]
        cls.roles = jsonpath.jsonpath(res, "$..list[0][roleId]")[0]
        cls.fkRoleId = jsonpath.jsonpath(res, "$..list[?(@.roleName=='角色自动化测试')][roleId]")[0]
        # print(res)
        # print(cls.fkRoleId)

    @classmethod
    def get_dept_list(cls):
        """门店列表，获取想要的门店id"""
        url = my_config.get("env_release", "base_url") + "/v4/web/exhibitionhall/demp/getDeptList"
        params = {"tenantId": cls.tenantId}
        response = cls.s.get(url=url, params=params)
        res = response.json()
        # print(res)
        # 提取字段dempId
        cls.dempId = jsonpath.jsonpath(res, "$..dempList[?(@.dempName=='美容院测试门店账户')][dempId]")[0]
        # print(cls.dempId)

    @classmethod
    def get_by_dempid(cls):
        """门店获取用户列表，获取用户id"""
        url = my_config.get("env_release", "base_url") + "/v4/web/exhibitionhall/user/getByDeptId"
        params = {
            "tenantId": cls.tenantId,
            "pageIndex": 1,
            "pageRows": 10,
            "orderBy": 1}
        response = cls.s.get(url=url, params=params)
        res = response.json()
        # 提取字段userId,
        cls.userId = jsonpath.jsonpath(res, "$..list[?(@.userName=='王雷自动化调试')][userId]")[0]
        cls.ids = jsonpath.jsonpath(res, "$..list[?(@.userName=='王雷自动化调试')][userId]")[0]

    @classmethod
    def mobile_phone(cls):
        """创建一个随机生成手机号的方法"""
        cls.userLogin = "159"
        for i in range(8):
            j = str(random.randint(0, 9))
            cls.userLogin += j
        return cls.userLogin

    # --------app测试前置接口获取参数-----------
    @classmethod
    def app_login(cls):
        """app登录接口前置"""
        # 1、测试数据准备（url，method，headers，params）
        url_login = my_config.get("env_release", "base_urlapp") + "/v1/account/login"
        headers = eval(my_config.get("env_release", "headers_login"))
        params = {
            "account": my_config.getint("env_release", "account"),
            "password": my_config.get("env_release", "password"),
            "appId": my_config.get("env_release", "appId"),
            "timestamp": 1623655964583,
            "sign": "dbfccc6a503144ec54649ad5bf3b1bae"
        }

        # 2、调用登录
        response = requests.request(method="post", url=url_login, headers=headers, data=params)
        res = response.json()
        print(url_login)
        print(response.request.headers)
        print(response.request.body)
        print(res)


if __name__ == '__main__':
    a = BaesTest()
    # a.web_login()
    # a.get_session_account()
    # a.select_role_list()
    # a.get_dept_list()
    # a.get_by_dempid()
    a.app_login()
    # print(a.mobile_phone())
    # print(BaesTest.__dict__)
