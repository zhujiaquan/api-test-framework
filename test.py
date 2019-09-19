#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import lib.config as conf

FILENAME = "case/user.ini"

if __name__ == "__main__":
    url ="ws://echo.websocket.org/"
    conf.get_config(FILENAME)
    print(conf.get_data('report', 'reportName'))
    print(url)
