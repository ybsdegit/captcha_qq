#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/29 16:45
# @author: Paulson●Wier
# @file: anti.py
# @desc:
"""
有些网站对webdriver进行了识别，
window.navigator.webdriver true
所以你需要这么做：
在启动Chromedriver之前，为Chrome开启实验性功能参数excludeSwitches，它的值为['enable-automation']，完整代码如下：

"""
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
option.add_argument('--disable-extensions')
option.add_argument('--profile-directory=Default')
option.add_argument("--incognito")
option.add_argument("--disable-plugins-discovery")
option.add_argument("--start-maximized")
driver = Chrome(options=option)
driver.maximize_window()
driver.get("https://urlsec.qq.com/report.html")


# class Login(object):
#     """
#     腾讯防水墙滑动验证码破解
#     使用OpenCV库
#     成功率大概90%左右：在实际应用中，登录后可判断当前页面是否有登录成功才会出现的信息：比如用户名等。循环
#     https://open.captcha.qq.com/online.html
#     破解 腾讯滑动验证码
#     腾讯防水墙
#     python + seleniuum + cv2
#     """
