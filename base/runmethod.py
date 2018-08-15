# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 12
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
            print res.status_code
        return res
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,encoding='utf-8',ensure_ascii=False,sort_keys=True,indent=2)
