import requests
from bs4 import BeautifulSoup
import pymysql
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.27 Safari/537.36"
}

def sql(a,b,c):
    connect = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='970320',
        db='豆瓣小说',
        charset='utf8')
    cursor = connect.cursor()
    cursor.execute('insert into 小说 values(%r,%r,%r)' % (a, b, c))
    connect.commit()
    connect.close()

def urllist(url):
    page = []
    url1 = []
    print("爬取："+url)
    req = requests.get(url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    htmlnem = BeautifulSoup(html, "lxml")
    a = htmlnem.find('ul', class_= 'subject-list')
    a_bf = BeautifulSoup(str(a), "lxml")
    b = a_bf.find_all('li', class_='subject-item')
    b_bf = BeautifulSoup(str(b), "lxml")
    c = b_bf.find_all('div', class_='pic')
    c_bf = BeautifulSoup(str(c), 'lxml')
    d = c_bf.find_all('a')
    for each in d:
        url1.append(each.get('href'))
    for each in url1:
        msg(each)
        time.sleep(1)
    e = htmlnem.find('div', class_='paginator')
    e_bf = BeautifulSoup(str(e), "lxml")
    f = e_bf.find_all('span', class_='next')
    f_bf =  BeautifulSoup(str(f), "lxml")
    g = f_bf.find_all('a')
    for each in g:
        page.append(each.get('href'))
    if page[0]:
        g = 'https://book.douban.com' + page[0]
        urllist(g)

def msg(url):
    title = []
    pingfen = []
    pinglun = []
    req = requests.get(url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    htmlnem = BeautifulSoup(html,"lxml")
    a = htmlnem.find('div', id = 'wrapper')
    a_bf = BeautifulSoup(str(a), "lxml")
    b = a_bf.find_all('h1')
    b_bf = BeautifulSoup(str(b), "lxml")
    c = b_bf.find_all('span')
    for each in c:
        title.append(each.string)
    d = a_bf.find_all('div', class_='rating_self clearfix')
    d_bf = BeautifulSoup(str(d), "lxml")
    e = d_bf.find_all('strong')
    for each in e:
        pingfen.append(each.string)
    f = d_bf.find_all('div', class_='rating_sum')
    f_bf = BeautifulSoup(str(f), "lxml")
    g = f_bf.find_all('a')
    g_bf = BeautifulSoup(str(g), "lxml")
    h = g_bf.find_all("span")
    for each in h:
        pinglun.append(each.string)
    sql(title[0], pingfen[0], pinglun[0])

urllist('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')
# msg('https://book.douban.com/subject/4908885/')