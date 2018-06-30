#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:41  
# @Author  : chenhao  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_historyweather.py  
# @Software: PyCharm
import requests
from config import config
import unittest
import ddt
from lib import until

@ddt.ddt
class testHistoryWeather(unittest.TestCase):
    def setUp(self):
        self.key = config.key
        self.provice_url =config.host +"province"
        self.city_url = config.host + "citys"
        self.weather_url =config.host + "weather"
        self.provice_id = 1


        pass
    def tearDown(self):
        pass
    def test_01get_provicelst(self):
        param = "key=" + self.key
        res = requests.get(self.provice_url,param)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"),"查询成功")
        result = jsonRes.get("result")
        for i in range(len(result)):
            province = result[i].get('province')
            if "广东" == province:
                self.provice_id = result[i].get('id')
        pass

    def test_02get_cityid(self):
        payload = {"key":self.key,"province_id":self.provice_id}
        res = requests.post(self.city_url,data=payload)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")

        pass
    @ddt.data(*until.get_testdata("../testdata/weather_parame.txt"))
    @ddt.unpack
    def test_03get_historyweather(self,city_id,weather_data):
        payload = {"key":self.key,"city_id":city_id,"weather_data":weather_data}
        res = requests.post(self.city_url, data=payload)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")

        pass
if __name__=="__main":
    unittest.main()