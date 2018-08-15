# coding:utf-8
# author:xuxiubing
# @Time: 2018 08 13

#判断实际结果是否和预期结果一致
class CommonUitl:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另外一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        :return:
        '''
        flag = None
        #判断字符串的类型
        if isinstance(str_one,unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
