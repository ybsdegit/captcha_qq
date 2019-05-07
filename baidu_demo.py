#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/7 10:57
# @author: Paulson●Wier
# @file: baidu_demo.py
# @desc:

# C:\Users\adm|in\AppData\Local\Google\Chrome\User Data\Default
from time import sleep

from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver import ChromeOptions

profile_directory  = r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data'
option = webdriver.ChromeOptions()
option.add_argument(profile_directory)
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.jianshu.com/')
sleep(3)