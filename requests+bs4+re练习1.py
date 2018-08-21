import requests
from bs4 import BeautifulSoup
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

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href))
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        try:
            url = stockURL + stock[0] + ".html"
            print(url)
            html = getHTMLText(url)
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'lxml')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            stockInfo = BeautifulSoup(str(stockInfo), 'lxml')
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count  = count + 1
                print('\r当前速度:{:.2f}%'.format(count*100/len(lst)), end='')
        except:
            count = count + 1
            print('\r当前速度:{:.2f}%'.format(count * 100 / len(lst)), end='')
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_info = 'E://python代码//天道酬勤//BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_info)

if __name__ == '__main__':
    main()