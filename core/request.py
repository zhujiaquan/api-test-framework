#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：接口测试的封装

import requests
import json
import core.logging as log


logging = log.get_logger()


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
        if method == ("put" or "PUT"):
            results = requests.put(url, data, headers=headers)
        if method == ("patch" or "PATCH"):
            results = requests.patch(url, data, headers=headers)
        response = results.json()
        return response
    except Exception as e:
        logging.error("请求失败 %s" % e)        
        print("请求失败 %s" % e)


def content(method, url, data, headers):
    """
    请求response自己可以自定义检查结果
    :param method: 请求类型
    :param url: 请求地址
    :param data: 请求参数
    :param headers: 请求headers
    :return: message信息
    """
    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url, data, headers=headers)
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
        if method == ("put" or "PUT"):
            results = requests.put(url, data, headers=headers)
        if method == ("patch" or "PATCH"):
            results = requests.patch(url, data, headers=headers)
        response = results.json()
        return response
    except Exception as e:
        logging.error("请求失败 %s" % e)        
        print("请求失败 %s" % e)


def set_cookie_api(method, url, data, headers):
    """
    自定义一个登录接口测试的方法
    :param method: 请求类型
    :param url: 地址
    :param data: 数据
    :param headers: 请求头
    :return: success（bool)
    """
    global cookie
    try:
        if method == ("post" or "POST"):
            results = requests.post(url, data, headers=headers)
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
        if method == ("put" or "PUT"):
            results = requests.put(url, data, headers=headers)
        if method == ("patch" or "PATCH"):
            results = requests.patch(url, data, headers=headers)
        response = results.json()
        cookie = requests.utils.dict_from_cookiejar(results.cookies)
        return response
    except Exception as e:
        loggin.error("API请求失败", e)
        print("API请求失败", e)


