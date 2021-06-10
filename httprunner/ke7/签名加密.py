# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-11 22:27 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
加密：
import hashlib  # 由于MD5模块在python3中被移除 # 在python3中使用hashlib模块进行md5操作
# 创建md5对象
m = hashlib.md5()
# 待加密信息
str = 'this is a md5 test.'
# Tips
# 此处必须encode
# 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
# 因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)

# 另一种写法：b‘’前缀代表的就是bytes
str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
print('MD5加密后为 ：' + str_md5)
'''


def sign_body(body, apikey="12345678"):
    '''签名函数'''
    # sign：签名
    # apikey = "12345678"  # 验证秘钥，由开发提供
    # body = {"username": "haiyu.ma",
    #         "password": "password.1",
    #         "mail": "",
    #         "sign": "签名后的值"}
    # 列表生成式：生成keyvalue形式
    a = ["".join(i) for i in body.items() if i[0] != "sign" and i[1] != ""]
    # print(a)
    # 参数名ASII码从小到大排序
    b = "".join(sorted(a))  # sorted 排序
    # 在b后拼接上apikey
    strsigntemp = b+apikey
    # print(strsigntemp)
    # 将最后得到的字符串转换成纯小写：
    # strsigntemp.lower()
    # Python md5加密：
    def jiami_md5(s):
        m = hashlib.md5()
        s = 'this is a md5 test.'
        b = s.encode(encoding='utf-8')
        m.update(b)
        return m.hexdigest()
    # 签名加密后：
    #
    sign = jiami_md5(strsigntemp.lower())
    return sign

def setup_request(request):
    body = request.get("json")
    request["json"]["sign"] = sign_body(body, apikey="12345678")


if __name__ == '__main__':
    apikey = "12345678"  # 验证秘钥，由开发提供
    body = {"username": "haiyu.ma",
            "password": "password.1",
            "mail": "",
            "sign": "签名后的值"}
    print(sign_body(body, apikey))
