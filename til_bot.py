import urllib.request
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
import schedule

jh = []
sh = []

def job():
    datetime.today()
    date = datetime.today().strftime("%Y-%m-%d.md")
    date = date[2:]
    week = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']
    day = week[datetime.today().weekday()]
    # 현재 날짜와 시간을 변수들에 저장한다.

    url = "https://github.com/jeonjeunghoon/TIL/tree/master"
    web = urllib.request.urlopen(url)
    res = web.read()
    soup = BeautifulSoup(res, 'html.parser')
    keywords = soup.find_all('a', class_='js-navigation-open link-gray-dark')
    keywords = [each_line.get_text().strip() for each_line in keywords[:10000000]]
    if date in keywords:
        date = date[:8]
        jh_res = date + day + ": O"
        jh.append(jh_res)
    else:
        date = date[:8]
        jh_res = date + day + ": X"
        jh.append(jh_res)

    url = ""
    web = urllib.request.urlopen(url)
    res = web.read()
    soup = BeautifulSoup(res, 'html.parser')
    keywords = soup.find_all('a', class_='js-navigation-open link-gray-dark')
    keywords = [each_line.get_text().strip() for each_line in keywords[:10000000]]
    if date in keywords:
        date = date[:8]
        sh_res = date + day + ": O"
        sh.append(sh_res)
    else:
        date = date[:8]
        sh_res = date + day + ": X"
        sh.append(sh_res)
    # 크롤링 코드

    import telegram

    token = '1629335207:AAEgc2pO4-xVY1L_gJjAhlCubrdGOzo7xjs'
    bot = telegram.Bot(token=token)
    chat_id = "-1001353446448"
    jh_text = "증훈의 기록\n" + jh_res
    bot.sendMessage(chat_id = chat_id , text=jh_text)
    sh_text = "세환의 기록\n" + sh_res
    bot.sendMessage(chat_id = chat_id , text=sh_text)
    # 텔레그램 봇과 연동하는 코드

schedule.every().day.at("23:59").do(job)
# 매일 23:59 마다 코드 실행

while True:
    schedule.run_pending()
    time.sleep(1)
# 파이썬 스케쥴