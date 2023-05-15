import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import subprocess

# 봇 토큰을 입력하세요.
TOKEN = '6068822535:AAEdX6RZ9_7N85NtDsyYornSU5LeoH9tEdI'
# 텔레그램 봇 객체 생성
bot = telegram.Bot(token=TOKEN)

#Start 명령어에 대한 메세지전송
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='안녕하세요! 키우미를 시작합니다.')

#메세지를 받아 이를 그대로 재전송
def echo(update, context):
    text = update.message.text
    chat_id=update.message.chat_id
    print('Message received from {chat_id}: {text}')
    #subprocess를 통하여 bot_send_Test.py를 호출
    subprocess.run(['python', 'bot_Send_Test.py', TOKEN,chat_id, text])

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()