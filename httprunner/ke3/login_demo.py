# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-03 22:51 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import requests
url = "http://52.83.166.21:8092/api/authenticate"
res = requests.post(url,
                   headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                                "content-type": "application/json"},
                   json={"password": "password.1",
                         "username": "haiyu.ma"})
# print(res.text)

# 提取token： extract
token = res.json()["id_token"]
print(token)

print(res.content)  # 返回结果是byte类型
# print(list(dict(res.json()).keys())[0])
# assert list(dict(res.json()).keys())[0] == "id_token"

# 断言校验：validate
assert res.status_code == 200
assert(len(res.json()["id_token"])) == 1895

# num_set = [i * 2 for i in range(1,10)]
# print(num_set)
#
# num_set = []
# for i in range(1,10):
#     num_set.append(i*2)
# print(num_set)