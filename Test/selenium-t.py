import requests
# import numpy
import random

enc_list = [
    # "3WVezeyJntt3KPpWtw2a%2FQIoD91mJcwMWaS434Aj0WNLEKrbry%2FmhMquAgSTLcO1X%2FmtdLq8bxsFjRqZpM7HPA%3D%3D",
# "HL0c9zI4uiXaRLdSIiatLOZC4%2FpbU2d4nDnKjsUy4lejmUhL%2B5xOTDQduVbjZsXhrLnXVKzbLNyi98teCyvhAA%3D%3D",
# "qOZ8jr0iE2FFx%2BFaUrK%2FOz%2BJYfHNU7TIQTssXsVywO9TvORc8LjviivH0Vr0WWjO5GVgQE8MQ%2BEgHKcudWthJg%3D%3D",
#     "BCYmhW5DQEmQ3xTFNOK5DJdjdJxor1SxuqZvABDPMckkk8ateJe60QxB7w8fIGLZ"
"EIAl85TRxn2TXNmchsOU+GW5O0l7jHuvzJT84i3gWQ8DyUdag2DFWv+HMoXg4UJKaALO03w+JEuhYcKfQ+Is8w=="
            ]
def test():
    while True:
        import requests

        url = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm"
}
        querystring = {"itemId": "553630841371", "sellerId": "2367236799",
                       "modules": "dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,amountRestriction,couponActivity,soldQuantity,originalPrice,tradeContract",
                       "callback": "onSibRequestSuccess"}

        payload = "changeView=card&queryStr=&userType=COMPANY"
        cookie = "enc={};  cna=KmNXEwhxrXECAQ4Xbbo/UFMB; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; um=0712F33290AB8A6DEFEE1A1A906C492906B7DCB71F1F15A84472B336EA9F357C9ACF9B906BC4C5C2CD43AD3E795C914C0D6CFCF0003A01DD47239216BD848424; mt=ci=0_0; _cc_=W5iHLLyFfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=204873d5d1cb621fc3fee8d6418202e1; v=0; ".format(random.choice(enc_list))
        isg = "isg=BGVlVl0UU5wuSLdooydq-dhOdyFfCidE5bsMrWdKIRyrfoXwL_IpBPM_DGII5THe; "
        complate_cookie = isg + cookie
        headers = {
            'host': "detailskip.taobao.com",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
            'accept': "*/*",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'accept-encoding': "gzip, deflate, br",
            'referer': "https://item.taobao.com/item.htm?spm=2013.1.0.0.576a5a6b30Odyh&id=553630841371&scm=1007.12144.81309.42296_42296&pvid=c10fec0f-29e6-4d17-8658-384050e2344a&utparam=%7B%22x_object_type%22%3A%22item%22%2C%22x_hestia_source%22%3A%2242296%22%2C%22x_object_id%22%3A553630841371%7D&utparam=%7B%22x_object_type%22%3A%22item%22%2C%22x_hestia_source%22%3A%2242296%22%2C%22x_object_id%22%3A553630841371%7D",
            'cookie': complate_cookie,
            'connection': "keep-alive",
            'cache-control': "no-cache",
            'postman-token': "7ac3f9a1-bcc4-85f4-617f-9ad5b75c56a9"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        print(response.text)
        import time
        time.sleep(5)
test()