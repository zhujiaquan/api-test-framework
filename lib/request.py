#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：接口测试的封装

import requests
import json


def change_type(value):
    """
    对dict类型进行中文识别
    :param value: 传的数据值
    :return: 转码后的值
    """
    result = eval(json.dumps(value, ensure_ascii=False, encoding="UTF-8"))
    return result


def api(method, url, data, headers):
    """
    定义一个请求接口的方法和需要的参数
    :param method: 请求类型
    :param url: 请求地址
    :param data: 请求参数
    :param headers: 请求headers
    :return: code码
    """
    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url, data, headers=headers)
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
        response = results.json()
        code = response.get("code")
        return code
    except Exception, e:
        print ("请求失败 %s" % e)

