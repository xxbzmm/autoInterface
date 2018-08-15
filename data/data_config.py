# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 11
class global_var:
    #case_id
    Id = '0'
    #名称
    request_name = '1'
    #url
    url = '2'
    #是否执行
    run = '3'
    #请求方式
    request_way = '4'
    #header
    header = '5'
    #依赖case
    case_depend = '6'
    #数据依赖
    data_depend = '7'
    #
    field_depend = '8'
    #请求数据
    data = '9'
    #预期结果
    expect = '10'
    #实际结果
    result= '11'
#获取case id
def get_id():
    return global_var.Id
#获取url
def get_url():
    return global_var.url
#获取是否执行
def get_run():
    return global_var.run
#获取请求方式
def get_run_way():
    return global_var.request_way
#获取header
def get_header():
    return global_var.header
#获取依赖case
def get_case_depend():
	return global_var.case_depend
#获取数据依赖
def get_data_depend():
	return global_var.data_depend
#获取
def get_field_depend():
	return global_var.field_depend
#获取请求数据
def get_data():
	return global_var.data
#获取预期结果
def get_expect():
	return global_var.expect
#获取实际结果
def get_result():
	return global_var.result