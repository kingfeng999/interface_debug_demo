# coding=utf-8
#!/usr/bin/python3
# @Time: 2021-09-02 15:58
# @Author: qinzhifeng
# @File: login.py
# @Software: PyCharm

import requests

url = "https://api3.kouling.cn:14000/ringle/onekey/100/"
headers = {'Content-Type': 'application/json', 'device': '1', 'version':'2.28.0'}
json = {
    "code": "112334",
    "sign": "5199addf8b86a861c3b47335c7b1864c",
    "tel": "13802282483",
    "timestamp": 1611127922,
    "hwid": "53691be5167946f8a6624e3d1f1ffc6f",
    "device": "1",
    "devname": "HONOR HWYAL",
    "ver": "2.28.0"
}

resp = requests.post(url, json = json, headers = headers)
r = resp.json()
print("返回文本：",resp.text)
print("返回请求url：",resp.url)
print("返回请求头：",resp.request.headers)
print("返回响应状态码：",resp.status_code)
print("响应内容格式：",resp.encoding)
print("返回 json 格式数据：",r)
print(r["ok"])
data = r["data"]
for i in data:
    token = i["token"]
    uid = i["uid"]
print(f"token：{token} ------ uid: {uid}")


