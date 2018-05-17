import requests

while True:
    url = "https://log.mmstat.com/eg.js"

    headers = {
        'host': "log.mmstat.com",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
        'accept': "*/*",
        'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'accept-encoding': "gzip, deflate, br",
        'referer': "https://item.taobao.com/item.htm?id=561952364548&ns=1&abbucket=20",
        'cookie': "cna=666",
        'connection': "keep-alive",
        'pragma': "no-cache",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    print(response.headers)