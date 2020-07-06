#selenium模拟登录石墨文档
#week02_02
#1期2班xuning

from selenium import webdriver
import time

driver = webdriver.Chrome('D:\chromedriver.exe')
driver.maximize_window()

with open('account.txt', 'r') as account:
    num = account.readline()
    password = account.readline()

# 登录shimo
def login(url):
    try:

        driver.get(url)
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="entries"]/a[2]/button').click()        #选择登录
        driver.find_element_by_xpath('//input[@type="text"]').send_keys(num)               #输入账号
        driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)      #输入密码
        driver.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()  #点击登录

    except Exception:
        return  None

if __name__:
    url = 'https://shimo.im/welcome'
    login(url)