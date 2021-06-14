"""
@Time : 2021/6/13 18:29
@Author : 
"""
import requests
# webhook地址
url = "https://oapi.dingtalk.com/robot/send?access_token=2116b4" \
      "cbd28465687dea22d4b533432ccd2cc70568ea4ee865cd8836775aade7"
# 发送的消息
data = {
    "msgtype": "text",
    "text": {
        "content": "自动化测试，测试一下，请忽略"
    },
    "at": {
        "atMobiles": [],
        "isAtAll": False
    }
}

# 发送请求获取结果
res = requests.post(url=url, json=data)
print(res.text)

