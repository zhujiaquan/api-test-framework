#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：日志服务

import logging
import constants as cs
import logging.handlers


def get_logger(name='report'):
    FORMAT = '%(message)s'
    filename = cs.REPORT_PATH + name + cs.NOW
    logging.basicConfig(level=logging.WARNING, format=FORMAT,
                       filename=filename, filemode='w')
    return logging
