import time
import requests
import aiohttp
import asyncio
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import logging
from selenium import webdriver
import pickle
from selenium import webdriver
from pyppeteer.launcher import launch
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



browser = webdriver.Chrome()
browser = browser.get("https://www.similartech.com/account/login")
browser.find_element_by_name('UserName').send_keys('wangjiah_7144@qq.com') #输入用户名
time.sleep(2)
browser.find_element_by_name('Password').send_keys('775773312') #输入密码
time.sleep(3)
browser.find_element_by_xpath('css=.input-group>.ladda-button').click() #点击登陆
pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)


data=[]
t1=time.time()
companies = ['topshop.com', 'zara.com']
'''
for company in companies:
        url="https://www.similartech.com/websites/"+company
        browser.get(url)
        html= browser.page_source
        print(html)
        soup = BeautifulSoup(html, "html.parser")
        category_list = soup.find_all(name='div', attrs={"class": 'row cmp '})
        for category in category_list:
            category_name = category.find(name='div', attrs={"class": 'row cmp-header sub'})
            print("category_name: " + category_name)
            technologies = category.find_all(name='a', attrs={"class": 'tech-name'})
            for name in technologies:
                technology_name = name.find('a').string
                technology_link = name.find('a')['href']
                print(technology_name)
                print(technology_link)
                #data.append([company['ID'], company['Client name'], company['Domain'], company['Parent Account'], company['Status'], category_name, technology_name, technology_link])



'''
