# -*- coding:utf-8 -*-
import sys
import random
import datetime,time





# redis operation key or values
GET_ACCOUNTS = 'accounts'
SEND_COOKIE = 'send_cookie'
EXPIRY_TIME = 'expiry_time'



#key
DONE_TIME = 'done_time'
START_CRAWL_TIME = 'start_crawl_time'
ACCOUNT_STATUS = 'status'
TOTALNUM = 'totalnum'               #实际总数量
DOWNLOAD_NUM    ='actual_download_num'
STARTSTAMP = 'startStamp'
ENDSTAMP = 'endStamp'
INDEX = 'index'
PAGEOFFSET = 'pageOffset'
LASTREQUESTPAGE = 'lastRequestPage'
DONEMESSAGE = 'doneMessage'


#value
STATUS_NEW = 'new'
STATUS_DONE = 'done'                #目前失败也当做是done
STATUS_DOWNLOADING = 'downloading'



# Thread management key or value
## 给客户资料爬虫端使用
CRAWL_THREADING = 'CRAWL_THREADING'
CRAWL_STATUS = 'CRAWL_STATUS'
CRAWL_DOWNING = 'CRAWL_DOWNING'
CRAWL_DONE = 'CRAWL_DONE'
CRAWL_NEW = 'CRAWL_NEW'


#Data Tranfer
DATA_TRANSFER_STATUS = 'DATA_TRANSFER_STATUS'
TRANSFER_NOT_TRANSFER = 'TRANSFER_NOT_TRANSFER'
TRANSFER_TRANSFERRING = 'TRANSFER_TRANSFERRING'
TRANSFER_DONE = 'TRANSFER_DONE'
TRANSFER_ERROR = 'TRANSFER_ERROR'
TRANSFER_TIME = 'TRANSFER_TIME'

### Information corresponding to QQ number
BELONG_INFO = 'belong_info'
OPENSEA_INFO = 'opensea_info'
CHAT_INFO = 'chat_info'
CUSTOMER_DETAIL_INFO = 'customer_detail_info'
LAST_CRAWL_PARM = 'last_crawl_parm'

#mongodb operation type
TYPE_BELONG = 'TYPE_BELONG'
TYPE_OPENSEA = 'TYPE_OPENSEA'
TYPE_CHAT_LOG = 'TYPE_CHAT_LOG'
TYPE_CUSTOMER_DETAIL = 'TYPE_CUSTOMER_DETAIL'

# 客户详情结构:
# customer_detail_info :{
#     status :   "done",
# "start_crawl_time":  "2018-01-31 11:50:10",
# }

# bl_op_eg = '''{
#     "status":  "done",
#      "start_crawl_time":  "2018-01-31 11:50:10",
#      "crawl_info":  {
#       "doneMessage":  [
#         "(Belong)",
#          "账号资料下载完毕，或者因为其他原因终止下载数据"
#       ],
#        "actual_download_num":  15950,
#        "done_time":  "2018-01-31 11:54:56",
#        "totalnum":  15908
#     },
#      "last_crawl_parm":  {
#       "index":  319,
#        "pageOffset":  1,
#        "startStamp":  "58966",
#        "endStamp":  "76558",
#        "lastRequestPage":  319
#     }'''


# Common constant
DELAY_TIME = 1.5
MAX_DOWNLOADER = 5      #最大线程数量
MAX_ERROR_NUM = 15      #当有验证码时 允许尝试登录最多的次数
#----------------------------------------------------------------------登陆端
LAST_LOGIN_TIME = 'LAST_LOGIN_TIME'
LAST_REFRESH_TIME = 'LAST_REFRESH_TIME'
DRIVER = 'DRIVER'
DRIVER_STATUS = 'DRIVER_STATUS'
RUNNING_STATUS_NO_COOKIES = 'RUNNING_STATUS_NO_COOKIES'         #获取浏览器后，进行登陆期间
RUNNING_STATUS_COOKIES = 'RUNNING_STATUS_COOKIES'               #登陆成功之后，获取到cookie
PAUSE_STATUS = 'PAUSE_STATUS'


# 账号有效时间
ACCOUNT_EXPIRETIME =  0.5 * 60  #min  （现在下载速度 每个小时2W客户）
# ACCOUNT_EXPIRETIME =  60*1.5   #min  聊天记录的下载时间
# ACCOUNT_EXPIRETIME =  1.2  #min  test

# WebDriverManager event
G_DS = "G_DS"    #getDrivers
G_C = "G_C"      #count
G_D_S = "G_D_S"  #getDriverStatus
G_D_L_T = "G_D_L_T"  #getDriverLastloginTime
G_D_R_T = "G_D_R_T"  #getDriverLastRfreshTime
I_W = 'I_W'          #is_Working

def refreshUrl():
    urlList = ["https://admin.qidian.qq.com/", "https://admin.qidian.qq.com/mp/imgTxtMaterial",
               "https://admin.qidian.qq.com/tp/wpa", "https://admin.qidian.qq.com/cl/CustomerClone",
               "https://admin.qidian.qq.com/mng/org", "https://admin.qidian.qq.com/ea/mails/list",
               "https://admin.qidian.qq.com/", "https://admin.qidian.qq.com/tp/wpa",
               "https://admin.qidian.qq.com/tp/RepRule", "https://admin.qidian.qq.com/tp/IMAccessSet",
               "https://admin.qidian.qq.com/tp/invitation", "https://admin.qidian.qq.com/ea/visitAnalysis/ov",
               "https://admin.qidian.qq.com/ea/wts/session/ov", "https://admin.qidian.qq.com/ea/evaluate/index",
               "https://admin.qidian.qq.com#", "https://admin.qidian.qq.com/ea/visitAnalysis/reception?type=receppage",
               "https://admin.qidian.qq.com/ea/visitAnalysis/reception?type=visitpage",
               "https://admin.qidian.qq.com/ea/visitAnalysis/page?type=title",
               "https://admin.qidian.qq.com/ea/visitAnalysis/funnel",
               "https://admin.qidian.qq.com/ea/visitAnalysis/reception?type=receppage",
               "https://admin.qidian.qq.com/ea/visitAnalysis/reception?type=visitpage",
               "https://admin.qidian.qq.com/ea/visitAnalysis/page?type=title"]

    def getURL():
        return urlList[random.randint(0, urlList.__len__() - 1)]
    return getURL

# if __name__ == '__main__':
#     print datetime.datetime.date()
#     print time.time()-(60 * 60 * 24 * 90)
#     print timeStampToTime(time.time()-(60 * 60 * 24 * (6*30)))