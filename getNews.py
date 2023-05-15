import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=삼성전자'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


titles = soup.select('a.news_tit')
summarys = soup.select('a.api_txt_lines')
for i in range(len(titles)):
    print(titles[i].text)
    print(summarys[i].text)
    print(titles[i].get('href'))

