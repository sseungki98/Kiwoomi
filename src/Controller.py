import requests
from bs4 import BeautifulSoup
from pykiwoom.kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect()  # 키움 API 접속


def bring_info(name):
    code_list = kiwoom.GetCodeListByMarket('0')  # 전체 종목 코드 조회
    code_name = []
    for code in code_list:
        code_name.append(kiwoom.GetMasterCodeName(code))

    if name[0] in code_list: # name이 종목코드인 경우
        value_list = kiwoom.block_request("opt10001",
                                          종목코드=name[0],
                                          output="주식기본정보",
                                          next=0).to_dict(orient='records')
    else:
        index = code_name.index(name[0]) # name이 종목이름인 경우
        value_list = kiwoom.block_request("opt10001",
                                          종목코드=code_list[index],
                                          output="주식기본정보",
                                          next=0).to_dict(orient='records')
        print(value_list)
    return_text = ''
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


