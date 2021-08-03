import requests
import json
import demjson
import base64
import re
import time
mydata = {
    "temperature": "36.7",
    "coordinates": "中国-湖南省-长沙市-林科大区",
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
    for user in tasks:
        i+=1
        res = login(user['username'],mybase64(user['pwd']))
        print(res)
        time.sleep(2)
         # 开始做事
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "authorization":"Bearer " + res["token"]
        }
        res = requests.post('https://xiaobei.yinghuaonline.com/prod-api/student/health/',data=json.dumps(mydata),headers=headers)
        print(demjson.decode(res.text))
        time.sleep(1)
    print("总共登陆了%s个账号"%i)


def start():
    alluser = []
    user1 = {
        "username":"你的账号",
        "pwd":"你的密码"
    }

    alluser.append(user1)
    _main(alluser)

start()