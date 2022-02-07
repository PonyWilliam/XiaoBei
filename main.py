# encoding: utf-8
import requests
import json
import demjson
import base64
import re
import time
import random
import io
import sys
from urllib.request import urlopen
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def mybase64(mystr):
    bytesStr = mystr.encode(encoding='utf-8')
    temp = str(base64.b64encode(bytesStr))
    pattren = re.compile("'(.*)'")
    return pattren.findall(temp)[0]
def login(username,pwd):
    # 登陆
    headers = {
        "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app"
    }
    requests.post("https://xiaobei.yinghuaonline.com/xiaobei-api/captchaImage",headers=headers)
    data = {
        "code": "M26J",
        "password": pwd,
        "username": username,
        "code": "SJCA",
        "uuid": "bd5ed14985394a04a076d79d27a266f7",
        "appUuid": "392D3E41-2BC4-41F6-A127-CBD91F00418F"
    }
    headers = {
            "content-type": "application/json;",
            "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app",
    }
    temp_res = requests.post('https://xiaobei.yinghuaonline.com/xiaobei-api/login',data=json.dumps(data),headers=headers).text
    res = demjson.decode(temp_res)
    return res


def _main(tasks):
    i = 0
    allres = []
    for user in tasks:
        i+=1
        res = login(user['username'],mybase64(user['pwd']))
        print(res)
         # 开始做事
        headers = {
            "content-type": "application/json",
            "authorization":"Bearer " + res["token"],
            "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app"
        }
        mydata = {
            "temperature": "36.5",
            "coordinates": "undefined-湖南省-永州市-冷水滩区",
            "location": "111.6186691623264,26.43941731770833",
            "healthState": "1",
            "dangerousRegion": "2",
            "dangerousRegionRemark": "",
            "contactSituation": "2",
            "goOut": "1",
            "goOutRemark": "",
            "remark": "",
            "familySituation": "1"
        }
        res = requests.post('https://xiaobei.yinghuaonline.com/xiaobei-api/student/health',data=json.dumps(mydata),headers=headers)
        allres.append(demjson.decode(res.text))
        time.sleep(1)
    print("总共登陆了%s个账号"%i)
    print(allres)
    return allres


def start(a=1,b=2):
    alluser = []
    user1 = {
        "username":"666",# 学号
        "pwd":"666" # 密码
    }
    alluser.append(user1)
    return _main(alluser)

start()