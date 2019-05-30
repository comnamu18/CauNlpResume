# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:46:00 2019

@author: joonoh oh
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import csv

import time
import random

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

my_id = driver.find_element_by_id("id")      
my_pw = driver.find_element_by_id("inputPwd") 
login_button = driver.find_element_by_id("loginBtn")

if login_button.is_displayed():
    my_id.clear()
    my_id.send_keys("your_daum_id")
    my_pw.clear()
    my_pw.send_keys("your_daum_pwd")
    login_button.click()

crawl_size = 7884  #7884 is maximum size now
idx = 1

for i in range(7000, crawl_size):
    time.sleep(1)
    cafe_url = 'http://cafe.daum.net/breakjob/p8R/' + str(i)
    driver.get(cafe_url)
    
    time.sleep(1)
    driver.switch_to_frame("down")
    
    try:
        content = driver.find_element_by_id("user_contents").text
        #print(content)
        f = open('./corpus/resume' + str(idx) + '.txt', mode='wt', encoding='utf-8')
        f.write(content)
        f.close()
        idx += 1
    except:
        continue
    





