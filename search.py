import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
from pykiwoom.kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect()  # 키움 API 접속

code_list = kiwoom.GetCodeListByMarket('0')  # 전체 종목 코드 조회
code_name = []
for code in code_list:
    code_name.append(kiwoom.GetMasterCodeName(code))

print(code_list)
print(code_name)
def get_info(name):
    if name in code_list:
        value_list = kiwoom.block_request("opt10001",
                                      종목코드=name,
                                      output="주식기본정보",
                                      next=0).to_dict(orient='records')
    else:
        index = code_name.index(name)
        value_list = kiwoom.block_request("opt10001",
                                          종목코드=code_list[index],
                                          output="주식기본정보",
                                          next=0).to_dict(orient='records')
    return_text = ''
    for item in value_list[0].items():
        return_text += item[0] + ' : ' + item[1] + '\n'

    return return_text

print(get_info('삼성전자'))