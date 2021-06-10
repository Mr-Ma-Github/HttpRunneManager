# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-05 17:52 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# debugtalk.py 可以被同级、子级引用
import requests
host = "http://52.83.166.21:8092"

# 写公告函数
def get_token(username = "haiyu.ma",password = "password.1"):
    res = requests.post(url=host+"/api/authenticate",
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                                 "content-type": "application/json"},
                        json={"password": password, "username": username})
    try:
        # 提取token： extract
        token = res.json()["id_token"]
        print("登录获取到的token：", token)
        return token
    except KeyError:
        print("账号或密码不正确")

if __name__ == '__main__':
    # get_token("admin", "323")
    get_token()