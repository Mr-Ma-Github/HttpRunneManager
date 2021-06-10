# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-18 23:14 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import requests

url = "http://52.83.166.21:8091/api/authenticate"

with open("user_pwd.txt", "r", encoding="utf-8") as file:
    data = {}
    list1 = file.readlines()
    for i in list1:
        a = i.strip("\n").split(",")
        data[a[0]] = a[1]
    print(data)
for k, v in data.items():
    body = {"username": k, "password": v}
    # print(body, type(body))
    try:
        res = requests.post(url, json=body)
        print(res.json())
        token = res.json()["id_token"]
        with open("token_user.txt", "a")as fp:
            fp.write("{0},Bearer {1}\n".format(k, token))
    except:
        msg = res.json()["AuthenticationException"]
        with open("token_user.txt", "a")as fp:
            fp.write("{0},{1}\n".format(k, msg))

