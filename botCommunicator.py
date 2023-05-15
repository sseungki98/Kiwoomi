import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
from pykiwoom.kiwoom import Kiwoom

commands = ['/info', '/alarm', '/news', '/search']
token = '6068822535:AAEdX6RZ9_7N85NtDsyYornSU5LeoH9tEdI'

bot = telegram.Bot(token=token) # 토큰으로 봇 생성
updater = Updater(token=token, use_context=True) # 업데이터 생성
dispatcher = updater.dispatcher # 디스패처 객체 생성

updater.start_polling() # 지속적으로 값 받아옴(polling 시작)

kiwoom = Kiwoom()
kiwoom.CommConnect()  # 키움 API 접속

code_list = kiwoom.GetCodeListByMarket('0')  # 전체 종목 코드 조회
code_name = []
for code in code_list:
    code_name.append(kiwoom.GetMasterCodeName(code))

def handler(update, context):
    user_text = list(update.message.text.split()) # 데이터가 입력되면 메세지에서 text 값을 파싱하여 가져옴
    user_id = update.message.chat.id # 마찬가지로 id값 가져옴
    print(user_text)
    if user_text[0] == '/info': # 명령어 검증
        if len(user_text) == 1:
            bot.sendMessage(chat_id=user_id, text='주식명 혹은 주식 코드를 입력해주세요.')
        else:
            bot.sendMessage(chat_id=user_id, text=user_text[1] + '에 관한 정보입니다.')
            if user_text[1] in code_list:
                bot.sendMessage(chat_id=user_id, text=get_info(user_text[1]))
            elif user_text[1] in code_name:
                bot.sendMessage(chat_id=user_id, text=get_info(user_text[1]))
            else:
                bot.sendMessage(chat_id=user_id, text='존재하지 않는 주식입니다.')

    else:
        bot.sendMessage(chat_id=user_id, text="유효한 명령어가 아닙니다.\n 명령어 리스트: '/info', '/alarm', '/news', '/search'")

    if user_text[0] == '/news':
        if len(user_text) == 1:
            bot.sendMessage(chat_id=user_id, text='주식명 혹은 주식 코드를 입력해주세요.')
        else:
            bot.sendMessage(chat_id=user_id, text=user_text[1] + '에 관한 뉴스입니다.')
            bot.sendMessage(chat_id=user_id, text=get_news(user_text[1]))
    else:
        bot.sendMessage(chat_id=user_id, text="유효한 명령어가 아닙니다.\n 명령어 리스트: '/info', '/alarm', '/news', '/search'")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler) # 디스패쳐에 핸들러 드록


def get_news(name):
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+ name
    news_response = requests.get(url)
    soup = BeautifulSoup(news_response.text, 'html.parser')

    titles = soup.select('a.news_tit')
    summarys = soup.select('a.api_txt_lines')
    texts = ''
    for i in range(len(titles)):
        texts += titles[i].text + '\n'
        texts += summarys[i].text + '\n'
        texts += titles[i].get('href') + '\n'

    return texts

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
