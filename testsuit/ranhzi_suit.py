#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:11  
# @Author  : chenhao  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : ranhzi_suit.py  
# @Software: PyCharm

import unittest

from test_case.test_historyweather import testHistoryWeather

if __name__ == '__main__':
    suite = unittest.TestSuite()


    tests = [testHistoryWeather("test_get_provicels"),testHistoryWeather("test_get_cityid"),
             testHistoryWeather("test_get_historyweathe")]
    suite.addTests(tests)


