import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

commands = ['/info', '/alarm', '/news', '/search']
token = '6068822535:AAEdX6RZ9_7N85NtDsyYornSU5LeoH9tEdI'

bot = telegram.Bot(token=token) # 토큰으로 봇 생성
updater = Updater(token=token, use_context=True) # 업데이터 생성
dispatcher = updater.dispatcher # 디스패처 객체 생성

updater.start_polling() # 지속적으로 값 받아옴(polling 시작)


def handler(update, context):
    user_text = list(update.message.text.split()) # 데이터가 입력되면 메세지에서 text 값을 파싱하여 가져옴
    user_id = update.message.chat.id # 마찬가지로 id값 가져옴
    print(user_text)
    if user_text[0] == '/info': # 명령어 검증
        if len(user_text) == 1:
            bot.sendMessage(chat_id=user_id, text='주식명 혹은 주식 코드를 입력해주세요.')
        else:
            bot.sendMessage(chat_id=user_id, text=user_text[1] + '에 관한 정보입니다.')
    else:
        bot.sendMessage(chat_id=user_id, text="유효한 명령어가 아닙니다.\n 명령어 리스트: '/info', '/alarm', '/news', '/search'")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler) # 디스패쳐에 핸들러 드록

