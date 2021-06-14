"""
@Time : 2021/6/12 22:39
@Author : 
"""
import time
import requests

s = requests.session()

# 第一步：测试数据准备（url，method，headers，params）
url_login = "https://cms.clife.cn/v4/web/exhibitionhall/common/admin/loginCheck"
params = {
    "username": 15921089253,
    "password": "ZGM0ODNlODBhN2EwYmQ5ZWY3MWQ4Y2Y5NzM2NzM5MjQ=",
    "_": int(time.time() * 1000)
}

response = s.post(url=url_login, data=params)
print(response.request.headers)
print(response.request.body)
print(response.json())

url = "https://cms.clife.cn/v4/web/exhibitionhall/user/add"
params1 = {"dempId": 265, "userName": "王雷自动化调试", "userLogin": 15917074416, "tenantId": 13, "status": 1, "roleId": 31}

response1 = s.post(url=url, json=params1)
# print(response1.request.headers)
# print(response1.request.body)
# print(response1.json())

