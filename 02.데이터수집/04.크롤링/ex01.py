from selenium import webdriver
from selenium.webdriver.common.by import By
import time

broswer = webdriver.Chrome()
broswer.get ('http://naver.com')


btn = broswer.find_element(By.CLASS_NAME, 'MyView-module__my_login___tOTgr')
btn.click()
time.sleep(3)

broswer.back()
broswer.forward()
broswer.refresh()

time.sleep(10)