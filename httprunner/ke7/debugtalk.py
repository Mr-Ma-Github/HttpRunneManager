# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-10 19:59 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import hashlib
host = "http://52.83.166.21:8091"

def hook_up():
    '''前置操作'''
    print("前置操作：setup")

def hook_down():
    '''后置操作'''
    print("后置操作：teardown")


def sign_body(body, apikey="12345678"):
    '''签名函数'''
    a = ["".join(i) for i in body.items() if i[0] != "sign" and i[1] != ""]
    b = "".join(sorted(a))  # sorted 排序 # 在b后拼接上apikey
    strsigntemp = b+apikey  # print(strsigntemp)
    # Python md5加密：
    def jiami_md5(s):
        m = hashlib.md5()
        s = 'this is a md5 test.'
        b = s.encode(encoding='utf-8')
        m.update(b)
        return m.hexdigest()
    # 签名加密后：
    sign = jiami_md5(strsigntemp.lower())
    return sign

def setup_request(request):
    body = request.get("json")
    request["json"]["sign"] = sign_body(body, apikey="12345678")


# 加密解密：
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json

'''
AES/CBC/PKCS7Padding 加密解密
环境需求:
pip  install  cryptography
pip3 install pycryptodome
'''

class PrpCrypt(object):

    def __init__(self, key='0000000000000000'):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.iv = b'0102030405060708'
        # block_size 128位

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16但是不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        text = text.encode('utf-8')
        # 这里密钥key 长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        text=self.pkcs7_padding(text)
        self.ciphertext = cryptor.encrypt(text)

        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext).decode().upper()

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    @staticmethod
    def pkcs7_unpadding(padded_data):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data)
        try:
            uppadded_data = data + unpadder.finalize()
        except ValueError:
            raise Exception('无效的加密信息!')
        else:
            return uppadded_data

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        #  偏移量'iv'
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip("\x01").\
            rstrip("\x02").rstrip("\x03").rstrip("\x04").rstrip("\x05").\
            rstrip("\x06").rstrip("\x07").rstrip("\x08").rstrip("\x09").\
            rstrip("\x0a").rstrip("\x0b").rstrip("\x0c").rstrip("\x0d").\
            rstrip("\x0e").rstrip("\x0f").rstrip("\x10")

    def dict_json(self, d):
        '''python字典转json字符串, 去掉一些空格'''
        j = json.dumps(d).replace('": ', '":').replace(', "', ',"').replace(", {", ",{")
        return j

def setup_jiami_request(request):
    '''加密body'''
    body = request.get("json").get("params")
    pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')  # 初始化密钥
    request["json"]["params"] = pc.encrypt(json.dumps(body))

def teardown_jiemi_response(response):
    '''解密response'''
    # 需解密的datas
    res_body = json.loads(response.content) # byte类型转换成字典
    print(res_body["datas"] )
    # 解密：
    pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')  # 初始化密钥
    datas_de = json.loads(pc.decrypt(res_body["datas"]))
    res_body["datas"] = datas_de  # dict类型
    # 转换成byte类型的content对象
    cont = bytes(json.dumps(res_body),encoding="utf-8")
    response.text = cont
    response.json = cont
    response.body = cont

if __name__ == '__main__':
    # 签名调用：
    # apikey = "12345678"  # 验证秘钥，由开发提供
    # body = {"username": "haiyu.ma",
    #         "password": "password.1",
    #         "mail": "",
    #         "sign": "签名后的值"}
    # print(sign_body(body, apikey))
    # -----------------------------------------------------------------------
    # 加密调用：
    import json
    pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')  # 初始化密钥
    # a = "1"
    # print("加密前：%s" % a)
    # b = pc.encrypt(a)
    # print("加密后：%s" % b)
    # print("大写变小写：%s" % b.lower())
    # # 解密：
    # d = 'b59227d86200d7fedfb8418a59a8eea9'
    # print("解密后：%s"%pc.decrypt(d))

    # 案例二：加密
    body = {"username": "haiyu.ma",
            "password": "password.1"}
    c = pc.encrypt(json.dumps(body))  # 把字典转换成字符串
    print(c)
    # 解密：
    print("解密后：%s" % pc.decrypt(c))
    print(type(pc.decrypt(c)))  # <class 'str'>
    print(json.loads(pc.decrypt(c)))
    print(type(json.loads(pc.decrypt(c))))  # <class 'dict'>

