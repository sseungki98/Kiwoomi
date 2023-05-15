import telegram
from telegram.ext import Updater, CommandHandler
import Controller

# 텔레그램 봇 토큰
TOKEN = 'YOUR_TOKEN_HERE'

# 메시지를 저장할 배열
messages = []

# /start 명령어 처리 함수
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='안녕하세요! 무엇을 도와드릴까요?')
#/help 명령어 처리 함수
def help(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='키우미 봇은 간단한 주식 도움 봇이에요 \n \
                             /info [주식명]= 주식의 현재 시세 및 관련 정보를 불러옵니다.\n \
                             /search [주식명][옵션]= 주식의 일봉,월봉,연봉 등 특정 정보를 불러옵니다.\n \
                             /alarm [주식명][가격]=주식이 특정 가격에 도달하였을 경우 봇을 통해 알려줍니다.\n \
                             /news [주식명]=해당 주식에 관련된 기사를 모으고 헤드라인 기사를 띄워줍니다. ')

# /info 명령어 처리 함수
def info(update, context):
    chat_id = update.effective_chat.id
    messages.append( context.args[0])
    # 메시지를 배열에 저장
    # Controller.py의 함수 호출
    Controller.bring_info(messages)

# /news 명령어 처리 함수
def news(update, context):
    chat_id = update.effective_chat.id
    # 메시지를 배열에 저장
    messages.append(context.args[0])
    # Controller.py의 함수 호출
    Controller.bring_News(messages)

# /alarm 명령어 처리 함수
def alarm(update, context):
    chat_id = update.effective_chat.id
    
    # 메시지를 배열에 저장
    messages.append(context.args[0])
    messages.append(context.args[1])
    # Controller.py의 함수 호출
    Controller.set_Alarm(messages)

# /search 명령어 처리 함수
def search(update, context):
    chat_id = update.effective_chat.id
     # 메시지를 배열에 저장
    messages.append(context.args[0])
    messages.append(context.args[1])
    # Controller.py의 함수 호출
    Controller.search_info(messages)

# 메시지를 받아들이고 명령어 처리 함수를 연결하는 Updater 객체 생성
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('info', info))
dispatcher.add_handler(CommandHandler('news', news))
dispatcher.add_handler(CommandHandler('alarm', alarm))
dispatcher.add_handler(CommandHandler('search', search))

# 텔레그램 봇 시작
updater.start_polling()
