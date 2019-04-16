import time
import pickle
from selenium import webdriver
from config import USERNAME, PASSWORD
# from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.similartech.com/websites/topshop.com")

time.sleep(1)

button1 = browser.find_element_by_id('topLoginBtn')
button1.click()

time.sleep(1)

username = browser.find_element_by_name('UserName')
username.send_keys(USERNAME)

time.sleep(1)
password = browser.find_element_by_name('Password')
password.send_keys(PASSWORD)

rememberme = browser.find_element_by_name('RememberMe')
rememberme.click()

time.sleep(1)

login = browser.find_element_by_xpath('//*[@id="nav"]/div/div[3]/div[2]/div[2]/div/div/form/div[3]/div/div/button')
login.click()

# pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     browser.add_cookie(cookie)


# data=[]
# t1=time.time()
# companies = ['topshop.com', 'zara.com']

# for company in companies:
#         url="https://www.similartech.com/websites/"+company
#         browser.get(url)
#         html= browser.page_source
#         print(html)
#         soup = BeautifulSoup(html, "html.parser")
#         category_list = soup.find_all(name='div', attrs={"class": 'row cmp '})
#         for category in category_list:
#             category_name = category.find(name='div', attrs={"class": 'row cmp-header sub'})
#             print("category_name: " + category_name)
#             technologies = category.find_all(name='a', attrs={"class": 'tech-name'})
#             for name in technologies:
#                 technology_name = name.find('a').string
#                 technology_link = name.find('a')['href']
#                 print(technology_name)
#                 print(technology_link)
#                 #data.append([company['ID'], company['Client name'], company['Domain'], company['Parent Account'], company['Status'], category_name, technology_name, technology_link])

