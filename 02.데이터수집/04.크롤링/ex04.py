from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('widow-size=1920x1080')

broswer = webdriver.Chrome(options=options)
url = 'https://flight.naver.com'
broswer.get(url)

broswer.get_screenshot_as_file('data/flight3.png')