"""
@Time : 2021/6/6 17:15
@Author : wanglei
"""
import re, jsonpath
# -------------练习：通过正则表达式获取接口字段-----------


res = {'code': 0,
       'msg': 'OK',
       'data':
           {'id': 1234576136, 'amount': 42363.88, 'mobile_phone': '15921089253', 'name': '王雷',
            'reg_time': '2021-05-26 20:11:16.0', 'type': 1,
            'token_info':
                {'token_type': 'fksdjf', 'expires_in': '2020-05-16 15:51:46',
                 'token': 'wNn58888887MAhvie5JprQDsD_iIvU5RP77zaNi5SYFT10EQ'}}
       }

# 1、正则获取token(注意json返回的字典格式中存在空格，匹配时去空格)
p1 = re.findall(r"'token': '(.+?)'", str(res))
p2 = re.findall(r"'token':\s'(.+?)'", str(res))[0]
print(p1, p2, sep="\n")

# 2、正则获取mobile_phone
p3 = re.findall(r"'mobile_phone': '(\d{11})'", str(res))[0]
print(p3)

# 3、正则获取id
p4 = re.findall(r"'id':\s(\d+)", str(res))[0]
print(p4)

# 4、通过jsonpath获取token
print(jsonpath.jsonpath(res, "$..token")[0])



