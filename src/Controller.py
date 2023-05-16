import requests
from bs4 import BeautifulSoup
import KiwoomConnector as kiwoom

def bring_info(messages):
    return texts

def bring_News(messages):

    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+messages[0];
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    titles = soup.select('a.news_tit')
    summarys = soup.select('a.api_txt_lines')
    texts = ''
    for i in range(len(titles)):
        texts += titles[i].text + '\n'
        texts += summarys[i].text + '\n'
        texts += titles[i].get('href') + '\n'

    return texts

def set_Alarm(messages):
    return True

def search_info(messages):

    return texts


