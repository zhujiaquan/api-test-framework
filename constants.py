#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 脚本功能：全部变量

import sys
import time
import os

DOMAIN = 'http://192.168.1.103'

REPORT_NAME = 'Test Report'
TITLE = 'All Data prepare the SQL'

METHOD = 'method'
URL = 'url'
DATA = 'data'
NAME = 'name'
NUMBER = 'number'
CODE = 'code'
HEADERS = 'headers'
REPORT = 'report'
R_NAME = 'reportName'
LOGIN='login'

REPORT_PATH = "./report/docs/"
YML_REPORT = "./report/mkdocs.yml"

CASE_PATH = "./case/"


#测试报告内容
API_TEST_FAIL = """
```
%s: Case Fail
 Number: %s
 Method: %s
 Url: %s
 Headers:
 %s
 Data : 
 %s
 Response : 
 %s
 Expect : %s
 Actual : %s
```
"""

API_TEST_SUCCESS = """
```
%s: Case Pass
 Number: %s
 Method: %s
 Url: %s
 Headers:
 %s
 Data : 
 %s
 Response : 
 %s
 Expect : %s
 Actual : %s
```
"""

#报告结果统计
RESULT_CONTENT = """
<p>Result：</p>
<table border="3" width="500px">
  <tr>
    <th style="color: #787878">All</th>
    <th style="color: #3cc8b4">Pass</th>
    <th style="color: #FFB5C5">Fail</th>
  </tr>
  <tr>
    <th style="color: #787878">%s</th>
    <th style="color: #3cc8b4">%s</th>
    <th style="color: #FFB5C5">%s</th>
  </tr>
</table>
"""

NOW = '_' + time.strftime('%Y%m%d', time.localtime(time.time())) + '.md'
PROJECT_TIME = time.strftime('%Y%m%d', time.localtime(time.time()))
