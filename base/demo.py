# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 10
import requests
import json
class Run_Main:
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def send_get(self,url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self,url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res
if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': 'xxbing',
        'password': '111111'
    }
    run = Run_Main(url,'POST',data)
    print run.res