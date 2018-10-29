import requests
from bs4 import BeautifulSoup
import pymysql
import os
import re
import json
import threading

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
               'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               'Accept-Encoding':'gzip,deflate',
               'Host':'music.163.com',
               'Referer':'http://nmusic.163.com',
               'Origin':'http: // music.163.com'}

#通过歌手id得到热门50首歌的歌名及其听歌网址到文档中
def music(singer_id):
    names = []
    urls = []
    title = []
    num = 0
    server = 'http://music.163.com/'
    target = 'http://music.163.com/artist?id='+singer_id
    req = requests.get(url=target,headers=headers)
    req.encoding='utf-8'
    html = req.text
    bf = BeautifulSoup(html, "lxml")
    mus = bf.find('ul',class_='f-hide')
    mus2 = bf.find('div',class_='btm')
    a = mus.find_all('a')
    b = mus2.find_all('h2')
    nums = len(a)
    for each in b:
         title.append(each.string.replace(' ',''))
    for each in a:
         names.append(each.string.replace(' ',''))
    for each in a:
         urls.append(server+each.get('href'))

    #通过得到的歌手名创建该歌手的歌曲表
    connect = pymysql.Connect(
         host='127.0.0.1',
         port=3306,
         user='root',
         passwd='970320',
         db='网易云音乐',
         charset='utf8')
    cursor = connect.cursor()
    cursor.execute('create table if not exists %s(歌名 longtext,网址 longtext)' % title[0])
    connect.commit()
    connect.close()
    for i in range(0,nums):
         a=names[i]
         b=urls[i]

         #将得到的歌名及其网址存放到表中
         connect = pymysql.Connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='970320',
                db='网易云音乐',
                charset='utf8')
         cursor = connect.cursor()
         cursor.execute('insert into %s values(%r,%r)' %(title[0],a,b))
         connect.commit()
         connect.close()

#根据歌曲id下载歌词
def download_by_music_id(music_id):
    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(music_id)+ '&lv=1&kv=1&tv=-1'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip,deflate',
        'Host': 'music.163.com',
        'Referer': 'http://nmusic.163.com',
        'Origin': 'http: // music.163.com'}
    r = requests.get(url=url,headers=headers)
    json_obj = r.text
    j = json.loads(json_obj)
    try:
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')
        lrc = re.sub(pat,"",lrc)

        #删除空白符
        lrc = lrc.strip()
        return lrc
    except KeyError as e:
        pass

#通过一个歌手id得到这个歌手的热门歌曲id
def get_music_ids_by_artist_id(singer_id):
    singer_url = 'http://music.163.com/artist?'+ 'id='+str(singer_id)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip,deflate',
        'Host': 'music.163.com',
        'Referer': 'http://nmusic.163.com',
        'Origin': 'http: // music.163.com'}
    r = requests.get(url=singer_url, headers=headers).text
    soupObj = BeautifulSoup(r, 'lxml')
    song_ids = soupObj.find('textarea')
    song_ids = song_ids.string
    jobj = json.loads(song_ids)
    ids = {}
    for item in jobj:
        ids[item['name']] = item['id']
    return ids

#下载歌词到文档中
def download_lyric(uid):
    title  = []
    singer_url = 'http://music.163.com/artist?'+ 'id='+str(uid)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip,deflate',
        'Host': 'music.163.com',
        'Referer': 'http://nmusic.163.com',
        'Origin': 'http: // music.163.com'}
    r = requests.get(url=singer_url,headers=headers).text
    soupObj = BeautifulSoup(r,'lxml')
    mus2 = soupObj.find('div', class_='btm')
    b = mus2.find_all('h2')
    for each in b:
        title.append(each.string)

        #将爬到的歌词放入文档中
        os.mkdir('F:/python代码/网易云音乐/' + title[0])
        os.chdir('F:/python代码/网易云音乐/' + title[0])
        music_ids = get_music_ids_by_artist_id(uid)
        a = 1
        for key in music_ids:
            text = download_by_music_id(music_ids[key])
            p =  re.sub('[/:*?"<>|]',' ',key)
            file = open(str(a)+'.'+ p + '.txt', 'a', encoding='utf-8')
            try:
                file.write(key + '\n')
                file.write(text)
                file.close()
            except TypeError as e2:
                file.write('空')
            a += 1

#多线程爬取歌词
class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        lock.acquire()
        download_lyric(self.id)
        lock.release()

#王菲、孙燕姿、莫文蔚、张靓颖
artist = ['9621','9272','8926','10561']
lock = threading.Lock()
threads = []
for i in range(4):
    name=artist[i]
    thread = MyThread(name)
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()

#调用函数获取热门50首歌及其网址
for i in range(4):
    name=artist[i]
    music(name)