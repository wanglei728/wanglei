# date:2021/6/15 10:57
import hashlib, time

"""
签名sign规则：
1. 将请求方法+请求地址+所有参数按照参数名的字母顺序升序（ASCII）排序后拼接+appSecret
    a、请求方法为GET或POST，注意大写
    b、参数拼接，按照参数名的字母顺序升序排序后进行组成完整的拼接
    eg：GEThttps://api.clife.cn/v1/account/loginaccount=xxx&appId=xxx&password=xxx&timestamp=xxxx&appSecret
2. 将第1步的结果MD5后生成签名参数sign
3. 登录接口timestamp需要和签名生成机制的timestamp保持一致
"""


class HandlerSign:

    def __init__(self, method, url, data, appsecret):
        setattr(HandlerSign, "method", method)
        setattr(HandlerSign, "url", url)
        setattr(HandlerSign, "data", data)
        setattr(HandlerSign, "appsecret", appsecret)

    @classmethod
    def data_process(cls):
        """方法+请求地址+所有参数按照参数名的字母顺序升序+appSecret"""
        data_list = []
        for k in sorted(cls.data.keys(), reverse=False):
            data_list.append("{}={}".format(k, cls.data[k]))
        data_list.append(cls.appsecret)
        params = "&".join(data_list)
        result = "".join((cls.method, cls.url, params))
        # 拼接结果设置为类属性
        setattr(HandlerSign, "result", result)
        # print(result)
        return result

    @classmethod
    def md5_sign(cls):
        res = cls.data_process()
        timestamp = int(time.time() * 1000)
        md5 = hashlib.md5()
        md5.update(res.encode("utf-8"))
        sign = md5.hexdigest()
        return {"sign": sign, "timestamp": timestamp}


if __name__ == '__main__':
    sign = HandlerSign(method="POST",
                       url="https://api.clife.cn/v1/account/login",
                       data={"account": 15921089253, "appId": 31417, "password": "fcf718b46ece081ba9fd4ecdf868826a",
                             "timestamp": int(time.time() * 1000)},
                       appsecret="b0327d0855c045eea23ae5ccaed5ed25")
    a = sign.md5_sign()
    print(a)
    # print(HandlerSign.__dict__)
