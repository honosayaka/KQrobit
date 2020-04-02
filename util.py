import requests

def get_gift(uuid, code):
    res = requests.get(url='http://statistics.pandadastudio.com/player/giftCode?uid='+uuid+'&code='+code)
    if uuid == '519509620':
        res.encoding = 'utf-8'
        js = res.json()
        return js['msg']



