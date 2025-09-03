from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #브라우저창이 항상 오픈
broswer = webdriver.Chrome(options=options)

broswer.maximize_window()

url = 'https://flight.naver.com'
broswer.get(url)

broswer.get_screenshot_as_file('data/flight.png') #화면을 캡쳐해서 파일로 저장
broswer.quit()