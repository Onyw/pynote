import requests
import re

def getHTMLText(url):
    try:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ilt, html):
    try:
        plt = re.findall(r'"price":".*?"', html)
        tlt = re.findall(r'title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '手机'
    depth = 3
    start_url = 'https://s.taobao.com/search?q='+goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(i*44)
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodsList(infolist)

if __name__ == '__main__':
    main()
