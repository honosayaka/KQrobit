import requests
import threading
import schedule
import time
import suyi
import datetime


def get_gift(uuid, code):
    res = requests.get(
        url='http://statistics.pandadastudio.com/player/giftCode?uid='+uuid+'&code='+code)
    if uuid == '519509620':
        res.encoding = 'utf-8'
        js = res.json()
        return js['msg']


def get_chp():
    return requests.get(url='https://chp.shadiao.app/api.php').text




class myThread (threading.Thread):
    def __init__(self, ws):
        threading.Thread.__init__(self)
        self.ws = ws
        
    def run(self):
        #schedule.every().day.at(time_every_day_sign_in).do(job)
        print('my thread have run!!!!!!')
        schedule.every().saturday.at('12:00').do(self.send_tru)
        schedule.every().day.at('9:30').do(self.send_j)
        while True:
            schedule.run_pending()
            time.sleep(3)

    def send_tru(self):

        ma = {
            'act': '101',
            'groupid': suyi.Qgroupid,
            'msg': get_tru_str()
        }
        data = suyi.jsBuilder(ma)
        self.ws.send(data)


    def send_j(self):
        res = requests.get(url='https://api.timbrd.com/jkrb/total.php')
        js = res.json()
        ma = {
            'act': '101',
            'groupid': 687830669,
            'msg': js['content']
        }
        data = suyi.jsBuilder(ma)
        self.ws.send(data)


def get_tru_str():
    tru = [
        [
            ['银枭夜行服(80)', '五彩兵粮丸(80)', '风魔无骨油(150）'],
            ['龙血围巾(150)', '八寒灵镜(150)', '“雷神牌"砥石(150)']
        ],
        [
            ['龙鳞甲(80)', '风之戒(80)', '冰晶羽魄(150)'],
            ['水之手里剑(80)', '红莲花烬(150)', '南蛮技师(120)']
        ],
        [
            ['忍宗印法(120)', '火之戒(80)', '四象护符(80)'],
            ['超级充电宝(150)', '忍宗印法(100)', '青木之吻(150)']
        ],
        [
            ['雷龙之鞘(80)', '龙血围巾(150)', '青木之吻(150)'],
            ['风之手里剑(80)', '不动明王甲(150)', '无敌铁金刚(150)']
        ],
        [
            ['恶达摩(100)', '水之手里剑(80)', '食神的礼物(150)'],
            ['天狗之牙(150)', '炎魂战旗(50)', '四象护符(80)']
        ],
        [
            ['水之戒(80)', '天狗之牙(150)', '无敌铁金刚(150)'],
            ['火之手里剑(80)', '雷龙之鞘(100)', '冰晶羽魄(150)']
        ],
        [
            ['超级充电宝(150)', '雷之戒(80)', '南蛮技师(120)'],
            ['玉狐折扇(150)', '仁王笼手(150)', '食神的礼物(150)']
        ]
    ]

    week = datetime.datetime.now().isocalendar()[1] - 16
    next_week = '下周：s:%s %s %s;ss:%s %s %s' % (tru[week][0][0], tru[week][0][1], tru[week][0][2],
                                               tru[week][1][0], tru[week][1][1], tru[week][1][2])
    return next_week

