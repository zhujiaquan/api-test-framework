#!/usr/bin/python
# -*- coding: UTF-8 -*-

import function.func as func
import constants as cs
import sys

FILENAME = "login.ini"

if __name__ == "__main__":
    """1.新建测试报告目录"""
    func.new_report_menu(filename=cs.CASE_PATH+FILENAME)

    """2.执行测试用例"""
    func.run_test(filename=cs.CASE_PATH+FILENAME)

    """3.统计测试报告结果"""
    #func.write_report_result()
