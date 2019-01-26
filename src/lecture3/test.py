import urllib2
import json
import itertools



url = 'https://signup.live.com/API/CheckAvailableSigninNames?uaid=283e90e8505846bfa14e3819881bdc1d&lic=1'
headers = {'x-ms-apiVersion':2,'hpgid':'Signup_MemberNamePage_Client','Accept':'Application/json','Cache-Control':'no-cache','Referer':'https://signup.live.com/?uaid=283e90e8505846bfa14e3819881bdc1d&lic=1','uiflvr':'1001','scid':'100118','Connection':'keep-alive','x-ms-apiTransport':'xhr','Pragma':'no-cache','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36','X-Requested-With':'XMLHttpRequest','tcxt':'8hcBLcqxnoqzFFuDq+ppAyj726fYFB3Faov7iNTYB6EbDEqbl3HJ0pPzerZjV0mkRYEJISX6G9AvRAmVmau1gj/ghCBVpw5zQ/yfkfbJqn3uEpR8BQAXqEnKkoA4evtLkwT/s1hYlGB/YNS6mnkImmhtUpWBrLVaDk2AVMtq/xBDTQGNV5NqS2oOBXYzDaNFvkiaMtpr26r4KiCx5TE+MCsZW/gO92t/DRfcYNJbbBpbwiuC4X2n3I7pT+AQuiABy1SW6Z8WDirLRSLBOO0eur+tGJVPr9uylOk0yb2QlPWhTu6/OY1/dufRyv+NQ8jKJDBn65CF2W/6wFxm3t79VY2VENownI8Fc3o6GyDqpci37d4Z1ciFonyY20/7Sfp0ehKnAqFSiWZEOhGPPVAz4g==:2:3','canary':'BQeOxsYFOnCPJrH4O353UB99o5W7AygqPuYXNLLEKoQgGdHIVkhlbkh4OtjPKmvTdf5ATbokXRToD7al/mU+qP33PUL6mKSOXCU/ekLDuETsZtd4bks3jSwNVpHRyBSUhrbgHKdNabGodtilL088ZvDpceF5c7+sp7ehD8gpLix2LmWUen3uUt9g/mptwx26zjOVh6uc7PxpO3m0QXGNnoLnKke6C5KOueImSOt4iAD9TE+5xkeLZCUqOApehwsZ:2:3c','Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7','Accept-Encoding':'gzip, deflate, br','Origin':'https://signup.live.com','uaid':'283e90e8505846bfa14e3819881bdc1d','Cookie': 'logonLatency=LGN01=636685387473791670; amsc=C1m34fcFeD8WPJhYA9rUGwhiWTJbi6kvxtiUaViajz+fOb3Yhz5NLu+cLDV8uBG/Cy83ce1A/2/pLIeDzX6H0rhzajsJgv/4NlMp+hsaWFFwA35G1liJNjpI0ZT/K7BNjyX1oCeANK1ht17HbfaEwTSv/0Ai3XcDPKs4Q/ktzcmdx9ab6T1HPJ+LBMSYqqBi2n0BfGshqz9hWTdPwkRSmjsN0nAJ2ubKyLQ+pgLRMK2Xlx7y4ALuXJt5sAIAhFBM:2:3c'}
for i in itertools.permutations('abcdefghijklmnopqrstuvwxyz', 2):
    address = ''.join(i)+'@outlook.lv'
    data = '{"signInName":"' + address + '","uaid":"283e90e8505846bfa14e3819881bdc1d","includeSuggestions":true,"uiflvr":1001,"scid":100118,"hpgid":"Signup_MemberNamePage_Client"}'
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    for x in f:
        print(x)
        if json.loads(x)["isAvailable"]:
            print(address)
    f.close()



