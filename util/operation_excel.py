# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 11
import xlrd
from  xlutils.copy import copy


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            self.data = self.get_data(file_name,sheet_id)
        else:
            self.file_name = '../dataconfig/case.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取某个单元格的内容
    def get_call_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        #复制数据到write_data
        write_data = copy(read_data)
        #获取excel的数据
        sheee_data = write_data.get_sheet(0)
        sheee_data.write(row,col,value)
        #保存数据
        write_data.save(self.file_name)



if __name__ == '__main__':
    opers = OperationExcel()
    print opers.get_data().nrows
    print opers.get_lines()
    print opers.get_call_value(2,3).encode('utf-8')
