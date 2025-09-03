import requests
from bs4 import BeautifulSoup

def weather(city):
    url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={city}날씨&oquery=%EB%82%A0%EC%94%A8&tqi=j7PKqsqVOZCssaT3e7GssssssgV-210727&ackey=p65k8ynu'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    summary = soup.find('p', attrs={'class':'summary'}).getText()
    # print(summary)

    #현재 온도
    temp = soup.find('div', attrs={'class':'temperature_text'}).strong.contents[1]
    # print(temp)

    #최저 온도
    lowest = soup.find('span', attrs={'class':'lowest'}).contents[1].replace('°', '')
    # print(lowest)

    #최고 온도
    highest = soup.find('span', attrs={'class':'highest'}).contents[1].replace('°', '')
    # print(highest)

    print('[오늘날씨]')
    print('-' *50)
    print(summary)
    print(f'현재온도 : {temp}도 (최저:{lowest}도)/ (최고:{highest}도)')
    print('-'*50)

if __name__=='__main__':
    while True:
        city = input('지역명>')
        if city == '' : break
        weather(city)