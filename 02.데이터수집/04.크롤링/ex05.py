#[쿠팡]-[검색어]-[노트북] 1페이지 결과 상품이름, 상품가격 etc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
broswer = webdriver.Chrome(options=options)
broswer.maximize_window()

keyword = '노트북'
url = f'https://www.gmarket.co.kr/n/search?keyword={keyword}'
broswer.get(url)

broswer.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(broswer.page_source, 'lxml')

items = soup.find_all("div", attrs={'class':'box__item-container'})
cnt = 0
list = []
for idx, item in enumerate(items):
    title = item.find('span', {'class':'text__item'}).getText()
    price = item.find('strong', {'class':'text text__value'}).getText()
    image = 'https:' + item.find('img', {'class':'image__item'})['src']
    ul = item.find('ul', {'class':'list__score'}).getText()
    pay_count = item.find('li', attrs={'class':re.compile('list-item__pay-count$')})
    link = item.a['href']
    if pay_count:
       pay_count = re.sub('구매|건|,', '', pay_count.getText()).strip()
       pay_count = int(pay_count)
    else:
       pay_count = 0
    
    if pay_count >= 100:
        cnt += 1
        print(cnt, title, price, image, pay_count)
        data = {'no':cnt, 'title':title, 'price':price, 'count':pay_count, 'image':image, 'link':link}
        list.append(data)

import json

with open('data/gmarket.json', 'w', encoding='utf8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

broswer.quit()
print('프로그램종료!')