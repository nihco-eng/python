import requests

url = 'https://ssl.pstatic.net/melona/libs/1544/1544585/93b5c12798eb3ead71d2_20250829114849965.jpg'
res = requests.get(url)

file_name = 'data/naver.jpg'
with open(file_name, 'wb') as file:
    file.write(res.content)
 