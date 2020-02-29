import requests


def get_gift(uuid, code):
    requests.get(url='http://statistics.pandadastudio.com/player/giftCode?uid='+uuid+'&code='+code)


