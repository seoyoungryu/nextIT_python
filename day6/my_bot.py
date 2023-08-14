# pip install python-telegram-bot==13.11
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext, CommandHandler
KEY="6118519466:AAGuZqCc2_LbthMcbxl4j9O5KaF6s-qY_MQ"
updater = Updater(token=KEY, use_context=True)
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text=user_text)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)

import os
img_dir = './images/'
file_dir = './files/'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
if not os.path.exists(file_dir):
    os.mkdir(file_dir)
import datetime
def get_photo(update, context:CallbackContext):
    print('get photo')
    # 현재 날짜와 시간
    now = datetime.datetime.now()
    now_yyyymmdd = now.strftime('%Y-%m-%d %H:%M:%S')
    file_path = os.path.join(img_dir, now_yyyymmdd +'.png')
    bot = context.bot
    photo = bot.getFile(update.message.photo[-1].file_id)
    photo.download(file_path)
    update.message.reply_text('photo saved:' + file_path)
photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

import random
def get_lotto(update, context):
    print('make lotto')
    user_id = update.effective_chat.id
    user_text = update.message.text
    cnt = int(user_text.replace('/lotto', '').strip())
    print(cnt, '개 생성')
    for i in range(int(cnt)):
        lotto = set()
        while len(lotto) < 6:
            lotto.add(random.randrange(1, 46))
        print(i + 1, "번 째 생성 번호 ", lotto)
        update.message.reply_text(str(lotto)) # 봇의 대답만 받을 경우
        #context.bot.send_message(chat_id=user_id, text=str(lotto)) # 특정 아이디를 가진 봇에서의 대답
lotto_handler = CommandHandler('lotto', get_lotto) # /lotto 3 이런식으로 텔레그램에 입력
updater.dispatcher.add_handler(lotto_handler)
def fn_diary(update, context):
    print('diary!!')
    file = 'diary.txt'
    f = open(file, 'a')  # a append, r read, w write
    user_id = update.effective_chat.id
    user_text = update.message.text
    input_text = user_text.replace('/diary', '').strip()
    f.write(input_text)
    f.writelines('\n')
    f.close()

diary_handler = CommandHandler('diary', fn_diary)
updater.dispatcher.add_handler(diary_handler)

def get_file(update, context:CallbackContext):
    message = update.effective_message
    bot = context.bot
    if message.document is not None:
        file_id_short = message.document.file_id
        file_url = os.path.join(file_dir, message.document.file_name)
        bot.getFile(file_id_short).download(file_url)
        message.reply_text('file save:' + file_url)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)


updater.start_polling()
updater.idle()