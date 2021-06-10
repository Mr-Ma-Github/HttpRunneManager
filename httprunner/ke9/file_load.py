# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-04-01 15:19 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# order上传文件
import requests  # 3
import os  # 3

base_url = "http://52.83.166.21:8091"
username = "haiyu.ma"
password = "password.1"

## 1.登录操作
def get_token(base_url=base_url,username=username,password=password):
    res = requests.post(url=base_url+"/api/authenticate",
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

def upload_file(file_name, base_url=base_url, file_path='D:/'):
    _file = os.path.join(file_path, file_name)
    files = {'file': (file_name, open(_file, "rb"), "image/jpg")}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
              # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryk95Gu2v20sOlwcO0',----上传文件时，header中不能增加此项
              'Authorization': 'Bearer '+get_token()}
    try:
        #使用requests 的post方法提交数据
        res = requests.post(url=base_url+"/api/static/file-create?folderPath=orders/", files=files, headers=header)
        print(res.text)
        return res.text
    except Exception as e:
        print("请求有问题!请检查代码")
        raise e


if __name__ == '__main__':
    upload_file('Lighthouse.jpg')