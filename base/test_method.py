# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 11
import unittest
from demo import Run_Main
import HTMLTestRunner
import json
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run=Run_Main()
    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        res = self.run.run_main(url,'POST',data)
        self.assertEqual(res['erroeCode',1001,'测试通过'])
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        res = self.run.run_main(url,'POST',data)

        print res
if __name__ == '__main__':
    filepath = '../report/htmlreport.html'
    fp = file(filepath,'wb')
    #unittest.main
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告')
    runner.run(unittest.main)