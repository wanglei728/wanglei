"""
@Time : 2021/6/14 13:59
@Author : 
"""
import hashlib
import secrets


def md5_encode(param):
    """
    md5加密方式
    :param param:待加密字符串或者字节
    :return return：密文
    """
    client_secret='F0897E16-5D1E-4A31-9644-BBF974E2DD88'       #此为加密的秘钥,开发算法提供
    sign=param+client_secret
    m = hashlib.md5(sign.encode(encoding='utf-8'))
    return m.hexdigest().lower()

