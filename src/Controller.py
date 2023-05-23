import requests
from bs4 import BeautifulSoup
from pykiwoom.kiwoom import Kiwoom
import KiwoomConnector
import os,json

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)  # 키움 API 접속


def bring_info(name):
    if not (os.path.exists('stock_data.json')):
        KiwoomConnector.get_codes()
    
    with open('stock_data.json','r') as file:
        stock_dict=json.load(file)
        stock_code=stock_dict.get(name)
    
    if stock_code is None:
        return("존재하지 않는 주식명 입니다. 확인후 다시 시도해주세요")
    
    value_list = kiwoom.block_request("opt10001",
                                      종목코드=stock_code,
                                      output="주식기본정보",
                                      next=0).to_dict(orient='records')
    
    print(value_list)
    return_text = ''
    print(return_text)
    for item in value_list[0].items():
        return_text += item[0] + ' : ' + item[1] + '\n'

    return return_text

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

    return True


