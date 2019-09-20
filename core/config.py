#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：配置服务

import configparser

config = configparser.ConfigParser()


def get_config(filename):
    """
    获取文件配置
    :param filename: 配置文件名
    :return: None
    """
    global config
    try:
        config.read(filename)
        return True
    except Exception as e:
        print ("读取配置失败 %s" % e)


def get_data(title, key):
    """
    参数配置
    :param title: 配置文件的头信息
    :param key: 配置文件的key值
    :return: 配置文件的value
    """
    try:
        value = config.get(title, key)
        return value
    except Exception as e:
        print ("获取参数失败 %s" % e)


def get_title_list():
    """
    获取所有title
    :return: title list
    """
    try:
        title = config.sections()
        return str(title)
    except Exception as e:
        print ("获取title信息失败 %s", e)

