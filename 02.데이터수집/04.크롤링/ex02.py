from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

broswer = webdriver.Chrome()
broswer.get ('http://naver.com')


btn = broswer.find_element(By.CLASS_NAME, 'MyView-module__my_login___tOTgr')
btn.click()

time.sleep(2)

id = broswer.find_element(By.ID, 'id')
id.send_keys('hd9536')
pw = broswer.find_element(By.ID, 'pw')
pw.send_keys('')
time.sleep(2)

login = broswer.find_element(By.ID, 'log.login')
login.click()
time.sleep(100)