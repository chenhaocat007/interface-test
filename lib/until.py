#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 17:23  
# @Author  : chenhao  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : until.py  
# @Software: PyCharm

def get_testdata(file_path):
    data4ddt=[]
    with open(file_path,encoding='utf-8') as f:
        dataset = f.readlines()
        for data in dataset:
            data4ddt.append(data.strip().split("|"))
    return data4ddt

# def get_testdata(path):
#     data4ddt = []
#     with open(path, encoding='utf-8') as f:
#         dataset = f.readlines()
#         for data in dataset:
#             data4ddt.append(data.strip().split("|"))
#
#     return data4ddt

