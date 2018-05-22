import requests
# import numpy
import random
from Authorizes.Taobao.CookieCollect import CookieCollect as tb_collect


import time
import datetime
import requests

cookies = ['enc=91dZLmC2JpB9Ohgr18nkZRfm4Aaga%2BUcKtpGsWae90cVhfCa%2FHeSTBAn5OCemO6%2FUpydrvXkuXhYy1OObT%2FFiw%3D%3D; t=3d9099091671b6aab37fcd686c6c0316; cookie2=3add3d4ae5fda5ce3294c3a0d40614d7; v=0; _tb_token_=e431335b74381; cna=9oiCEx3up1oCAQ4XbbqcZjZG; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci%3D-1_1'
           'enc=4bcwy45knc4ypYIoKtPMgYdyfrZO977jopu%2BwMifvxcFwiutYlOBo35%2Fe7rDem%2F5nbsjK4%2By%2BBXsKNjiGeHuYg%3D%3D; t=7efe796f21bc6892b1d037223fbef6cb; cookie2=35f5419dc9b6e30823e572865b9ddb03; v=0; _tb_token_=735e7651f75ee; cna=9oiCEx3up1oCAQ4XbbqcZjZG',
           'enc=HqqdBt1eZci8PcUClRkwEofZ4zBZPHcMYKyVAI34Fzomych1qQBX6EZ09vBjUL2XES6CYxSx%2FMKLlvAr1WXjBA%3D%3D; t=9674d32792c5e632cfd0fe85d134203e; cookie2=361633abe3b9b36dc4a80ad31379da56; v=0; _tb_token_=ed716e33b73eb; cna=9oiCEx3up1oCAQ4XbbqcZjZG',
           'enc=oajycM6cFp%2F2R9%2BwH8yMOfG%2F0bMWa%2BLK8cKDmvr10BVfIgi8upc%2FJCGX%2B6gaLcd7uBfswPTX7%2Fh8Yw6rGFz1Hw%3D%3D; t=56da14c07dbd9a672d2ef914ba78dc75; cookie2=35edfca4b5809463148acb961b0e1f29; v=0; _tb_token_=fe5387366b8e3; cna=9oiCEx3up1oCAQ4XbbqcZjZG',
          'enc=5rdTOvEr7yQBy39G4RQzno28C5qIyqHsUXQtHeDj8x6Y%2FRzgQPVS2b5lGSVZF5mKUlMo94qJHcqK2RUZyu%2F4Hw%3D%3D; t=c4747f827b162744fef2cc7306363cd5; cookie2=3adf2db21e5288c735733ad32521e0dd; v=0; _tb_token_=eb384d333eeee; cna=9oiCEx3up1oCAQ4XbbqcZjZG; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn'
                    ]

tb_col = tb_collect()
def get_item(url, referre):
    # url = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm"

    # querystring = {"itemId": "553630841371", "sellerId": "2367236799",
    #                "modules": "dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,amountRestriction,couponActivity,soldQuantity,originalPrice,tradeContract",
    #                "callback": "onSibRequestSuccess"}

    # payload = "changeView=card&queryStr=&userType=COMPANY"
    # cookie = "enc={};  cna=KmNXEwhxrXECAQ4Xbbo/UFMB; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; um=0712F33290AB8A6DEFEE1A1A906C492906B7DCB71F1F15A84472B336EA9F357C9ACF9B906BC4C5C2CD43AD3E795C914C0D6CFCF0003A01DD47239216BD848424; mt=ci=0_0; _cc_=W5iHLLyFfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=204873d5d1cb621fc3fee8d6418202e1; v=0; ".format(random.choice(enc_list))
    # isg = "isg=BGVlVl0UU5wuSLdooydq-dhOdyFfCidE5bsMrWdKIRyrfoXwL_IpBPM_DGII5THe; "
    # complate_cookie = "isg=" + tb_col.get_isg() + '; ' + random.choice(cookies)
    # print(url)

    headers = {
        'host': "detailskip.taobao.com",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
        'accept': "*/*",
        'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'accept-encoding': "gzip, deflate, br",
        'referer': referre,
        # 'cookie': complate_cookie,
        'connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, )
    # print(complate_cookie)
    # print(response.headers)
    print(response.text)
    # time.sleep(3)


tasks = {'task_name': '淘宝商品详情子数据商品分类及销售信息获取', 'task_id': '4', 'items': [{'itemurl': '//item.taobao.com/item.htm?id=561971548908&ns=1&abbucket=0#detail', 'nid': '561971548908', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561971548908&sellerId=702966125&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=27605716153&ns=1&abbucket=0#detail', 'nid': '27605716153', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=27605716153&sellerId=197146903&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=555690168958&ns=1&abbucket=0#detail', 'nid': '555690168958', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=555690168958&sellerId=60131294&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=563653870209&ns=1&abbucket=0#detail', 'nid': '563653870209', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=563653870209&sellerId=2857860605&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561668276542&ns=1&abbucket=0#detail', 'nid': '561668276542', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561668276542&sellerId=31820457&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=528850779934&ns=1&abbucket=0#detail', 'nid': '528850779934', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=528850779934&sellerId=741439442&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=550209605636&ns=1&abbucket=0#detail', 'nid': '550209605636', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=550209605636&sellerId=58247495&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=558001277826&ns=1&abbucket=0#detail', 'nid': '558001277826', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=558001277826&sellerId=96936597&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=537525433012&ns=1&abbucket=0#detail', 'nid': '537525433012', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=537525433012&sellerId=33166940&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=527433078289&ns=1&abbucket=0#detail', 'nid': '527433078289', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=527433078289&sellerId=2056127069&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=550590050649&ns=1&abbucket=0#detail', 'nid': '550590050649', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=550590050649&sellerId=849683336&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=555107118898&ns=1&abbucket=0#detail', 'nid': '555107118898', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=555107118898&sellerId=3257393267&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=552042450746&ns=1&abbucket=0#detail', 'nid': '552042450746', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=552042450746&sellerId=2530995558&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=558715208028&ns=1&abbucket=0#detail', 'nid': '558715208028', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=558715208028&sellerId=74528626&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=560480630997&ns=1&abbucket=0#detail', 'nid': '560480630997', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=560480630997&sellerId=3111393805&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=557137956529&ns=1&abbucket=0#detail', 'nid': '557137956529', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=557137956529&sellerId=355592377&modules=qrcode,viewer,price,duty,xmpPromotion,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=528904072717&ns=1&abbucket=0#detail', 'nid': '528904072717', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=528904072717&sellerId=26883383&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=521111464676&ns=1&abbucket=0#detail', 'nid': '521111464676', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=521111464676&sellerId=79294415&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=566314685719&ns=1&abbucket=0#detail', 'nid': '566314685719', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=566314685719&sellerId=3415496300&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561756303911&ns=1&abbucket=0#detail', 'nid': '561756303911', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561756303911&sellerId=1078288555&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=564753343644&ns=1&abbucket=0#detail', 'nid': '564753343644', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=564753343644&sellerId=23959687&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=546638706456&ns=1&abbucket=0#detail', 'nid': '546638706456', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=546638706456&sellerId=2946642479&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=542481726048&ns=1&abbucket=0#detail', 'nid': '542481726048', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=542481726048&sellerId=2976816923&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=40796296219&ns=1&abbucket=0#detail', 'nid': '40796296219', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=40796296219&sellerId=794260290&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561267708932&ns=1&abbucket=0#detail', 'nid': '561267708932', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561267708932&sellerId=1649031268&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=560805845482&ns=1&abbucket=0#detail', 'nid': '560805845482', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=560805845482&sellerId=378599934&modules=qrcode,viewer,price,duty,xmpPromotion,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=562493495701&ns=1&abbucket=0#detail', 'nid': '562493495701', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=562493495701&sellerId=2174796139&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=555497448063&ns=1&abbucket=0#detail', 'nid': '555497448063', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=555497448063&sellerId=2024065096&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=560866085717&ns=1&abbucket=0#detail', 'nid': '560866085717', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=560866085717&sellerId=238535446&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=541429934522&ns=1&abbucket=0#detail', 'nid': '541429934522', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=541429934522&sellerId=3018253719&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=556019002092&ns=1&abbucket=0#detail', 'nid': '556019002092', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=556019002092&sellerId=3347143923&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=559034256681&ns=1&abbucket=0#detail', 'nid': '559034256681', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=559034256681&sellerId=60894547&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=43571319090&ns=1&abbucket=0#detail', 'nid': '43571319090', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=43571319090&sellerId=35460069&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=566360600001&ns=1&abbucket=0#detail', 'nid': '566360600001', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=566360600001&sellerId=2180510959&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=554894745808&ns=1&abbucket=0#detail', 'nid': '554894745808', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=554894745808&sellerId=750059092&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=559155300270&ns=1&abbucket=0#detail', 'nid': '559155300270', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=559155300270&sellerId=3426939123&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=538202084544&ns=1&abbucket=0#detail', 'nid': '538202084544', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=538202084544&sellerId=868923155&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=563966666006&ns=1&abbucket=0#detail', 'nid': '563966666006', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=563966666006&sellerId=14820263&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561535476784&ns=1&abbucket=0#detail', 'nid': '561535476784', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561535476784&sellerId=31951073&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=3883950172&ns=1&abbucket=0#detail', 'nid': '3883950172', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=3883950172&sellerId=25676385&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=555076640552&ns=1&abbucket=0#detail', 'nid': '555076640552', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=555076640552&sellerId=215083418&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561634892777&ns=1&abbucket=0#detail', 'nid': '561634892777', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561634892777&sellerId=74810000&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=563256795963&ns=1&abbucket=0#detail', 'nid': '563256795963', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=563256795963&sellerId=249091719&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=554827295220&ns=1&abbucket=0#detail', 'nid': '554827295220', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=554827295220&sellerId=920072603&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=563708075899&ns=1&abbucket=0#detail', 'nid': '563708075899', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=563708075899&sellerId=2963474939&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=560151906639&ns=1&abbucket=0#detail', 'nid': '560151906639', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=560151906639&sellerId=1710168858&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=561037968923&ns=1&abbucket=0#detail', 'nid': '561037968923', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=561037968923&sellerId=849289987&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=16882559774&ns=1&abbucket=0#detail', 'nid': '16882559774', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=16882559774&sellerId=34060993&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=522915804347&ns=1&abbucket=0#detail', 'nid': '522915804347', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=522915804347&sellerId=1847721123&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}, {'itemurl': '//item.taobao.com/item.htm?id=19870344482&ns=1&abbucket=0#detail', 'nid': '19870344482', 'sibUrl': '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=19870344482&sellerId=3625&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract'}], 'task_nums': '50'}



items = tasks['items']

count = 0
now = lambda :datetime.datetime.now()
starttime = now()
while True:

    for item in items:
        count += 1
        print(count)
        url = 'https:' + item['sibUrl'] + '&callback=onSibRequestSuccess'

        referre = 'https:' + item['itemurl']

        get_item(url, referre)
    if count >= 30:
        # print()
        print('开始{}'.format(starttime))
        print('结束{}'.format(now()))
        # print(now())
        break
