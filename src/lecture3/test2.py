# import uncurl
import urllib2
import itertools
import json

url = 'https://signup.live.com/API/CheckAvailableSigninNames?wa=wsignin1.0&rpsnv=13&rver=6.7.6643.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2flv-lv%2f&id=74335&aadredir=1&contextid=5B4B28B87EBD61AF&bk=1532961102&uiflavor=web&uaid=7c15a66975c24cbaafcbd2c3cd9498cd&mkt=LV-LV&lc=1062&lic=1'

headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://signup.live.com",
        "Pragma": "no-cache",
        "Referer": "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=6.7.6643.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2flv-lv%2f&id=74335&aadredir=1&contextid=5B4B28B87EBD61AF&bk=1532961102&uiflavor=web&uaid=7c15a66975c24cbaafcbd2c3cd9498cd&mkt=LV-LV&lc=1062&lic=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "canary": "peL3sVS30xmEjMy4fY5mUjbqo8lnq2DqJpcmyRRFUadZVg8zuCc6jNF98dah5x7e3XsqaYWh/HOd2v/w35O6/fJql2AmwraFBDGd+gfIECI+pkuzj3xeza3Bcfl3M7fhcmMhL36rdRblyOcQDka0nYxTNLkA5Il0rwcXpPf/iDK+1xK015oby/TZEPg9XICIEqYY5z/McairQoplWFfAGb3vgB3T/7EhW3hZI9ejkcqcmsbwmoSIbo+7PwyamHLe:2:3c",
        "hpgid": "Signup_MemberNamePage_Client",
        "scid": "100118",
        "tcxt": "gUehSQQi98Dk2d9yKk0H8tJjG74sKvb3BajIdIBDBkSFb7gigOIThxBK/HlYqmEvhSbJVEhE0w+TGxrTtg2ctwTSDvly9ErRIpecNxfbqYfQkhppD1xiBorUw9ZHlSQXpxifm3oOAQejZmjwu7AYOn1jtjT1K0uGd2WoEa4eQ3yqJ+BRdc/3GWhmBv+7+g49nnppKmoDMsYPPygt3B5EdGIHD+HV1Z6+pMYvaiv/tVtDmq4iYrrC2FecCer4haGaH0cFlD4BZ58mGxbRt22vFas+/SUNaw5QAhlPrlg8HrzO8/lzeF1GCBycQepu8h6ZdpbpAwBdhT79Uwzw3+LzrnWz0e6HhxQZAnxEOGk2zwBWsl2jwN5UEJxD7hH1oCFM3edmWajLNWesRu3c38UAq+0tQNzxrOjIFr5oXhxmy5Y=:2:3",
        "uaid": "7c15a66975c24cbaafcbd2c3cd9498cd",
        "uiflvr": "1001",
        "x-ms-apiTransport": "xhr",
        "x-ms-apiVersion": "2",
        "Cookie": "MUID=07462D7D021E6D2B18BF2144061E6E38; TOptOut=1; MH=MSFT; NAP=V=1.9&E=1525&C=7yMc-uCo047W3S3BLmiNpriVI_hfBlT0wUHkr73I4HQa354JnoWw4Q&W=1; ANON=A=A763F5D630B2CF5815F936DEFFFFFFFF&E=157f&W=1; wlidperf=FR=L&ST=1532941029690; mkt=en-US; amsc=z4M+A5/mYR7I02SEkYkLGzp4us/T6qSYd33Td7pVPbcI7g+EbuhCxA4qc0LtfRwyg44Bq7R7YFUySGlLez9EU19PTKaS7nuCeAKoImWedtqEvTN14xv8FGenuI9y8IWhCZruCgyPMuXnWuxgkfR8GHZeCn2n8TjjalQMnsiJ+lT67QGa7MPBoAUoKYZRiV1DotpetwpF+vMDj9stiNLpSZ79L2/r90kfO3yPR+T/8a06jUdm5Zjwm8eIbHz/Ijsy:2:3c; mkt1=lv-LV; MSCC=1532961114"
    }
for i in itertools.permutations('abcdefghijklmnopqrstuvwxyz', 1):
    address = ''.join(i)+'@outlook.lv'
    data = '{"signInName":"'+address+'","uaid":"7c15a66975c24cbaafcbd2c3cd9498cd","includeSuggestions":true,"uiflvr":1001,"scid":100118,"hpgid":"Signup_MemberNamePage_Client"}'
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    for x in f:
        print(x)
        if json.loads(x)["isAvailable"]:
            print(address)
    f.close()