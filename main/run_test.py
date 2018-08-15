# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 12
import sys
sys.path.append('/Users/apple/PyCharm/autoIntergace')
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_uitl import CommonUitl
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_uitl = CommonUitl()

    #程序执行的主入口
    def go_on_run(self):
        res = None
        #获取excel行数 即case个数
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            #预期结果值
            except_data = self.data.get_except_data(i)
            #header = self.data.is_header(i)
            if is_run:
                #method,url,data=None,header=None 顺序不能错
                res = self.run_method.run_main(method,url,data)
                print res
                if self.com_uitl.is_contain(except_data,res):
                    #print "测试通过"
                    self.data.write_data(i,"pass")
                else:
                    #print "测试失败"
                    self.data.write_data(i,"fail")

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()