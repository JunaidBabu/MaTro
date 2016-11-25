import facebook
import telegram
import requests
import time, threading
import calendar

from secrets import *
import json
# secrets.py:
# bot_token = ''
# fb_app_id = ""
# fb_app_secret = ""

bot = telegram.Bot(bot_token)
def putpoint(data, fb_id):
    bla = {'data': data, '1':0, '2': 0, '4': 0, '6': 0}
    return json.dumps(bla)





token = facebook.GraphAPI().get_app_access_token(app_id=fb_app_id, app_secret=fb_app_secret)
pages = ['632474226810626', '441269415895560', '181750138656093','301036620082727']


def some_action(post):
    print(post['id'])
    reply_markup = {"inline_keyboard": [
        # [{"text": "👍","callback_data": putpoint(1, post['id'])},
        # {"text": "😒","callback_data": putpoint(2, post['id'])}],
        # [{"text": "😆","callback_data": putpoint(4, post['id'])},
        # {"text": "😡","callback_data": putpoint(6, post['id'])}],
        []
        ]}
    reply_markup['inline_keyboard'][0]=[{"text": "Original link","url": "http://facebook.com/"+post['id']}]
    try:
        bot.sendPhoto(chat_id = "-1001080424959", photo = "http://graph.facebook.com/"+post['id'].split('_', 1)[1]+"/picture?type=normal", caption = post['message']+'\n\n@MalluTrollz', reply_markup=reply_markup)
    except Exception as e: print (str(e))


def verum_post(posts):
    while True:
        try:
            [some_action(post=post) for post in reversed(posts['data'])]
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            return


a = 1
def foo():
    global a
    print ("Loop: " + str(a))
    file = open('time.scroll', 'r')
    time_n = file.read()
    file.close()
    graph = facebook.GraphAPI(access_token=token, version='2.7')
    for page in pages:
        posts = graph.get_connections(page, 'feed', since=time_n.strip())
        verum_post(posts)

    a = a + 1

    file = open('time.scroll', 'w')
    file.write(str(int(time.time())))
    file.close()
    threading.Timer(300, foo).start()


foo()
