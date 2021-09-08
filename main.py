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
    data = {
        "code": "RL4W",
        "password": pwd,
        "username": username,
        "uuid": "d0a4a39c6e3a4c0ea0c009c550936ad5"
    }
    headers = {
            "content-type": "application/json;charset=UTF-8",
    }
    res = demjson.decode(requests.post('https://xiaobei.yinghuaonline.com/prod-api/login',data=json.dumps(data),headers=headers).text)
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
            "content-type": "application/json;charset=UTF-8",
            "authorization":"Bearer " + res["token"]
        }
        mydata = {
            "temperature": "36."+time.strftime("%d",time.localtime()),
            "coordinates": "中国-湖南省-长沙市-望城区",
            "location": "112.91107231689452,26.43942138671875",
            "healthState": "1",
            "dangerousRegion": "2",
            "dangerousRegionRemark": "",
            "contactSituation": "2",
            "goOut": "1",
            "goOutRemark": "",
            "remark": "",
            "familySituation": "1"
        }
        res = requests.post('https://xiaobei.yinghuaonline.com/prod-api/student/health/',data=json.dumps(mydata),headers=headers)
        allres.append(demjson.decode(res.text))
        time.sleep(1)
    print("总共登陆了%s个账号"%i)
    return allres


def start(a=1,b=2):
    alluser = []
    user1 = {
        "username":"431103200009260311",
        "pwd":"260311"
    }
    user2 = {
        "username":"43070320000508165X",
        "pwd":"20188592"
    }
    user3 = {
        "username":"431022199903046799",
        "pwd":"046799",
    }

    alluser.append(user1)
    for _ in range(1):
        alluser.append(user2)
        alluser.append(user3)
    return _main(alluser)
