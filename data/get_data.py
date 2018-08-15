# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 11
from util.operation_excel import OperationExcel
import data_config
from util.operation_json import OperationJson
class GetData:
    def __init__(self):
        self.opra_excel = OperationExcel()
        self.opra_json = OperationJson()

    #获取excel的行数，也就是我们case的个数
    def get_case_lines(self):
        return self.opra_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opra_excel.get_call_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #是否有header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opra_excel.get_call_value(row,col)
        if header == 'yes':
            return header
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opra_excel.get_call_value(row,col)
        return request_method

    #获取url
    def get_url(self,row):
        col = int(data_config.get_url())
        url = self.opra_excel.get_call_value(row,col)
        return url

    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.opra_excel.get_call_value(row,col)
        if data == '':
            return None
        else:
            return data

    #获取预期结果
    def get_except_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opra_excel.get_call_value(row,col)
        if expect == '':
            return None
        return expect

    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        request_data =self.opra_json.get_data(self.get_request_data(row))
        return request_data

    #获取实际结果
    def write_data(self,row,value):
        col = int(data_config.get_result())
        self.opra_excel.write_value(row,col,value)
