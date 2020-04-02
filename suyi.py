import websocket
import sql
import json
import util

try:
    import thread
except ImportError:
    import _thread as thread


class Msg:

    def __init__(self, js):
        self.js = json.loads(js)

    def getQQ(self):
        return self.js['fromQQ']

    def getMsgCont(self):
        return self.js['msg']

    def getGroup(self):
        try:
            return self.js['fromGroup']
        except Exception:
            return ''


def jsBuilder(map):
    s = '{'
    for key in map:
        s = s + '"' + str(key) + '":' + '"' + str(map[key]) + '",'
    s = s + '}'
    return s.replace(',}', '}')


'''{    "act": "106",    "QQID": "1234",    "msg": "我很好！"}
表示向qq号为1234的好友发送一条“我很好”的私聊消息。

act和各字段含义如下，注意区分大小写，可能包含中文的字段，比如msg应使用utf8编码，如有返回数据，也是utf8:

101, 发送群消息
groupid,msg'''
Qgroupid = 784604984  ###257909494


# Qgroupid = 257909494

def on_message(ws, message):
    print(message)
    myMsg = Msg(message)
    if '[CQ:' not in str(myMsg.getMsgCont()):
        sql.insert_msg(myMsg.getQQ(), myMsg.getMsgCont())
        if str(myMsg.getGroup()) == str(Qgroupid):
            do1(ws, message)
            do2(ws, message)



def check(msg):
    if msg.find('-1') != -1 or msg.find('减1') != -1 or msg.find('减一') != -1:
        return True
    else:
        return False


def do1(ws, message):
    myMsg = Msg(message)
    qq = myMsg.getQQ()
    mscontent = str(myMsg.getMsgCont())
    if qq == '675916756' or qq == '2233616017':
        if check(mscontent):
            nownum = str(sql.getStat())
            sql.mi1(int(nownum) - 1)
            msg = '燕老板地位减一！现在的地位是' + str(nownum)
            ma = {
                'act': '101',
                'groupid': Qgroupid,
                'msg': msg
            }
            data = jsBuilder(ma)
            ws.send(data)


def do2(ws, message):
    myMsg = Msg(message)
    qq = myMsg.getQQ()
    mscontent = str(myMsg.getMsgCont())
    if mscontent.startswith('tru'):
        ma = {
            'act': '101',
            'groupid': Qgroupid,
            'msg': 'http://www.honosayaka.xyz:8080/ninja.html'
        }
        data = jsBuilder(ma)
        ws.send(data)
    elif mscontent.startswith('jadd') and get_add_per(qq):
        uuid = mscontent.replace('jadd', '')
        if len(uuid) == 9:
            sql.add_uuid(uuid)
            msg = str(uuid) + '已经添加成功！'
            ma = {
                'act': '101',
                'groupid': Qgroupid,
                'msg': msg
            }
            data = jsBuilder(ma)
            ws.send(data)
    elif mscontent.startswith('g') and get_gf_per(qq):
        strs = ''
        lis = sql.get_uuids()
        code = mscontent.replace('g', '')
        res = ''
        for i in range(0, len(lis)):
            if lis[i] == '519509620':
                res = util.get_gift(lis[i], code)
                strs = strs + lis[i] + ','
                continue
            util.get_gift(lis[i], code)
            strs = strs + lis[i] + ','
        msg = strs + '已经成功兑换！' + '\n兑换结果:' + res
        ma = {
            'act': '101',
            'groupid': Qgroupid,
            'msg': msg
        }
        data = jsBuilder(ma)
        ws.send(data)


def get_add_per(qq):
    qqlist = ['675916756', '2233616017', '308445000']
    return qq in qqlist


def get_gf_per(qq):
    qqlist = ['675916756', '2233616017', '308445000', '1455518788']
    return qq in qqlist


def on_error(ws, error):
    print(error)


def on_close(ws):
    ma = {'act': '106', 'QQID': '675916756', 'msg': 'program hapben shut dwon! '}
    data = jsBuilder(ma)
    ws.send(data)
    ws.close()
    print("### closed ###")


def on_open(ws):
    def run(*args):
        print('have runed')

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://49.234.98.122:25303",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
