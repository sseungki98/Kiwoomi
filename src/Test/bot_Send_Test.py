import telegram
import argparse

def send_message(token, chat_id, message):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send Telegram Message')
    parser.add_argument('token', help='Telegram Bot Token')
    parser.add_argument('chat_id', help='Chat ID')
    parser.add_argument('message', help='Message to send')
    args = parser.parse_args()

    send_message(args.token, args.chat_id, args.message)