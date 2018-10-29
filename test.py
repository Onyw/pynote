# if __name__ == '__main__':
#     doc = []
#     doc2 = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         doc.append([name, score])
#     temp = 100
#     bignum = 100
#     for i in range(len(doc)):
#         if bignum > doc[i][1]:
#             bignum = doc[i][1]
#     for i in range(len(doc)):
#         if temp > doc[i][1] and doc[i][1] != bignum:
#             temp = doc[i][1]
#     for i in doc:
#         if i[1] == temp:
#             doc2.append(i[0])
#     doc2 = sorted(doc2)
#     for i in doc2:
#         print(i)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     score_list = student_marks[query_name]
#     score_all = sum(score_list)
#     print("%.2f" % (score_all / 3))

# if __name__ == '__main__':
#     char = input()
#     a = char[0]
#     sum = 0
#     for i in range(len(char)):
#         if a == char[i]:
#             sum += 1
#         else:
#             print((sum,int(a)), end=' ')
#             a = char[i]
#             sum = 1
#     print((sum,int(a)))

# from itertools import groupby
# for k, g in groupby(input()):
#     print("({}, {})".format(len(list(g)), k), end=" ")
# 1222311

# from itertools import combinations
# a = int(input())
# b = input().split()
# c = int(input())
# word_list2 = combinations(b,c)
# sum = 0
# sum2 = 0
# for i in word_list2:
#     sum2 += 1
#     if 'a' in i:
#        sum += 1
# print("%.4f" % (sum / sum2))

# n = int(input())
# l = []
# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print(l)

# import urllib.request
#
# url = 'http://student.kaikeba.com/ucenter/course'
#
# headers = {
# "Cookie": "UM_distinctid=164a136fb3f0-0e87992bfc7ed6-7d113948-1fa400-164a136fb4157f; zg_did=%7B%22did%22%3A%20%22164b25a085b361-04596fc848b8ff-47e1039-1fa400-164b25a085d9bf%22%7D; gr_user_id=38ed40a0-96c7-419c-8aac-13f7b396e397; grwng_uid=18887743-afb4-4f10-927d-317dccec7a50; zg_9c90a84d308048688daeea828b2158aa=%7B%22sid%22%3A%201534938864782%2C%22updated%22%3A%201534938864801%2C%22info%22%3A%201534417763623%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.kaikeba.com%2F%22%7D; Hm_lvt_9a1843872729d95c5d7acbea784c51b2=1534647638,1534678002,1534818544,1534938865; user=%7B%22keep7day%22%3Afalse%2C%22qq%22%3A%22805690075%22%2C%22true_name%22%3A%22%E9%87%91%E5%87%A1%E5%8D%9A%22%2C%22mobile%22%3A%2217745162715%22%2C%22name%22%3A%22%E9%87%91%E5%87%A1%E5%8D%9A%22%2C%22id%22%3A80807%2C%22is_paid%22%3A1%2C%22avatar%22%3A%22http%3A%2F%2Fi.kaikeba.com%2F15320003411133990.jpg-100x100%3Fimageslim%22%2C%22token%22%3A%2243d4c49731dc439d84823242ed52b3c0%22%7D; current=%7B%22name%22%3A%22Python%E7%88%AC%E8%99%AB%E5%95%86%E4%B8%9A%E9%A1%B9%E7%9B%AE%E7%8F%AD%20001%E6%9C%9F%22%2C%22courseid%22%3A89%7D; CNZZDATA1258741995=2016355411-1531995432-http%253A%252F%252Fwww.kaikeba.com%252F%7C1534940494; Hm_lpvt_9a1843872729d95c5d7acbea784c51b2=1534943509; zg_7c9bcf6917804ce5ad8448db3cbe3fb3=%7B%22sid%22%3A%201534943508.852%2C%22updated%22%3A%201534943508.858%2C%22info%22%3A%201534417768706%2C%22cuid%22%3A%20%22%22%7D; responseTimeline=39",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
#     # 浏览器 请求
# }
#
# # 创建请求对象
# request = urllib.request.Request(url, headers=headers)
#
# response = urllib.request.urlopen(request)
# data = response.read().decode('utf-8')
# with open('kaikeba.html', 'w', encoding='utf-8') as f:
#     f.write(data)

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print(hash(integer_list))

# def swap_case(s):
#     s2 = ''
#     for i in range(len(s)):
#         if 'a' <= s[i] <= 'z':
#             s2 += s[i].upper()
#         elif 'A' <= s[i] <= 'Z':
#             s2 += s[i].lower()
#         else:
#             s2 += s[i]
#     return s2
# a = 'laskfjio as;lskdfj;LSKDFlsdfj;L'
# print(swap_case(a))

# def count_substring(string, sub_string):
#     counter=0
#     i=0
#     while i<len(string):
#         if string.find(sub_string,i)>=0:
#             i=string.find(sub_string,i)+1
#             counter+=1
#         else: break
#     return counter
# print(count_substring('asbsberts', 't'))

# n = int(input())
# lst = list(map(int, input().split()))
# min = 10000
# length = len(lst)
# for i in range(0, length):
#     for j in range(i+1, length):
#         a = abs(lst[i] - lst[j])
#         if a < min :
#             min = a
# print(min)

# lst = list(map(int, input().split()))
# flag = 1
# sum = 0
# for i in range(35):
#     if lst[i] != 0:
#         if lst[i] == 1:
#             sum += 1
#             flag = 1
#         elif lst[i] == 2:
#             sum += flag * 2
#             flag += 1
#     elif lst [i] == 0:
#         break
# print(sum)

# def count_substring(string, sub_string):
#     count = 0
#     lenString = len(string)
#     lenSub_string = len(sub_string)
#     for i in range(0, lenString-lenSub_string+1):
#         if string[i:len(sub_string)+i] == sub_string:
#             count += 1
#     return count
#
# print(count_substring('ABCDCDC', 'CDC'))

# from __future__ import print_function
# def print_formatted(n):
# # your code goes here
#     for i in range(1, n+1):
#         print (
#                '   ' +
#                (str(i).rjust(len(str(i))).rjust((len(str(n))), '   ')) +
#                (str(oct(i))[2:].rjust(len(str(bin(n))[2:])+1)) +
#                ((str(hex(i))[2:].upper()).rjust(len(str(bin(n))[2:])+1)) +
#                (str(bin(i))[2:].upper().rjust(len(str(bin(n))[2:])+1))
#               )
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# import requests
# from lxml import etree
#
# url = 'http://8btc.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
#
# data = requests.get(url, headers=headers).content.decode('gbk')
#
# parse_data = etree.HTML(data)
#
# title = parse_data.xpath('//a[@class="s xst"]/text()')
#
# print(title)
# print(len(title))

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     print(" ".join(map(str, arr[::-1])))

# import urllib.request
#
# from bs4 import BeautifulSoup
#
# def a():
#     url = 'http://8btc.com/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    # }

# import requests
# from lxml import etree
#
#
# class CarSpider(object):
#     def __init__(self):
#         self.url = "https://k.autohome.com.cn/detail/view_01cpc7nmfk68rked9n64s00000.html?st=1&piap=0|835|0|0|1|0|0|0|0|0|1#pvareaid=2112108"
#         self.headers = {
#             "Cookie": "__ah_uuid=6CCC98AA-7E4C-4D73-8B24-F49140DB7A2A; fvlid=1536145873941Xv9lcLlop9; sessionip=222.171.151.227; sessionid=48A72157-526C-4478-8C6D-E0E3D88BD4D2%7C%7C2018-09-05+19%3A11%3A14.035%7C%7Ccn.bing.com; sessionvid=58A4E956-7F1A-4F17-B427-AB60D67CFFDC; area=230103; ahpau=1; sessionuid=48A72157-526C-4478-8C6D-E0E3D88BD4D2%7C%7C2018-09-05+19%3A11%3A14.035%7C%7Ccn.bing.com; guidance=true; ASP.NET_SessionId=5whki222eqvxn0o2b5bxvxuj; ahpvno=69; ahrlid=1536157886260aBEJgkCLvU-1536157886744; _fmdata=mZsrcn0OnkGB4HonuDz4pd7kWyo2dE%2BWp6f0fMvzS5wUtTHMBywgJ0svFAt7Pyy%2FsWrBPwQR96XJLpqgZ3cvD%2FjkXIL8HeeIFqAt1d70eqU%3D; pvidchain=103600,2112108,2112108,103600,2112108,103600,2112108,2112108,2112108,2112108; ref=cn.bing.com%7C0%7C0%7C0%7C2018-09-05+22%3A31%3A28.825%7C2018-09-05+19%3A11%3A14.035",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
#         }
#
#     #获取页面html
#     def get_html(self, url):
#         response = requests.get(url, headers=self.headers)
#         html = response.text
#         return html
#
#     def get_span(self, html):
#         html_1 = etree.HTML(html)
#         html_2 = html_1.xpath('/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/span[1]/text()')
#         # html_2 = html_1.xpath('/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/span[1]')
#         print(html_2)
#
#     def run(self):
#         html = self.get_html(self.url)
#         print(html)
#         self.get_span(html)
#
# a = CarSpider()
# a.run()

# i = 1
# try:
#     i+=1
# except:
#     i+=1
# else:
#     i+=1
# finally:
#     i+=1
# print(i)

# import redis
# try:
#     client = redis.StrictRedis()
# except  as e:
#     print(e)

# def qc_list(a):
#     temp = a[0]
#     a_len = len(a)
#     flag = True
#     sum = 0
#     while flag:
#         sum += 1
#         a.pop(0)
#         if temp not in a:
#             a.append(temp)
#         temp = a[0]
#         if sum == a_len:
#             flag = False
#     return a
# a = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]
# print(a)
# print(id(a))
# print(qc_list(a))
# print(id(qc_list(a)))

# import re
# cookie = 'zg_did=%7B%22did%22%3A%20%2216575b51037130-0a928fa5af2eef-47e1039-1fa400-16575b51038769%22%7D; UM_distinctid=1657615bbcb49e-0d6024e6dbca81-47e1039-1fa400-1657615bbcc435; Hm_lvt_9a1843872729d95c5d7acbea784c51b2=1537677271,1538999813,1539171577,1539343764; user=%7B%22keep7day%22%3Afalse%2C%22qq%22%3A%22805690075%22%2C%22true_name%22%3A%22%E9%87%91%E5%87%A1%E5%8D%9A%22%2C%22mobile%22%3A%2217745162715%22%2C%22name%22%3A%22%E9%87%91%E5%87%A1%E5%8D%9A%22%2C%22id%22%3A80807%2C%22is_paid%22%3A1%2C%22avatar%22%3A%22http%3A%2F%2Fi.kaikeba.com%2F15320003411133990.jpg-100x100%3Fimageslim%22%2C%22token%22%3A%22d6f3f508fa024ef6bb71abff570eca74%22%7D; current=%7B%22name%22%3A%22Python%E7%88%AC%E8%99%AB%E5%95%86%E4%B8%9A%E9%A1%B9%E7%9B%AE%E7%8F%AD%20001%E6%9C%9F%22%2C%22courseid%22%3A89%7D; zg_9c90a84d308048688daeea828b2158aa=%7B%22sid%22%3A%201539352135514%2C%22updated%22%3A%201539352135514%2C%22info%22%3A%201538999813940%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.kaikeba.com%2F%22%7D; CNZZDATA1258741995=2128189677-1535281350-%7C1539349063; Hm_lpvt_9a1843872729d95c5d7acbea784c51b2=1539352136; zg_7c9bcf6917804ce5ad8448db3cbe3fb3=%7B%22sid%22%3A%201539352136.116%2C%22updated%22%3A%201539352136.123%2C%22info%22%3A%201539171588016%2C%22cuid%22%3A%20%22%22%7D; responseTimeline=153'
# cookie = cookie.split('; ')
# dit = {}
# for i in cookie:
#     result = re.search('(.*?)=(.*)', i)
#     dit[result.group(1)] = result.group(2)
# print(dit)

# select name, salary, dname from person , dept where salary = (select max(salary) from person) and did = (select dept_id from person where salary = (select max(salary) from person));

# 查询平均年龄大于20岁的部门名
# 一、
#-> select did, dname from dept as p1,
#-> (select dept_id , avg(age) as ava from person group by dept_id) as p2
#-> where p1.did = p2.dept_id and p2.ava > 20;
# 二、
# select dname from dept where did in (select dept_id from person group by dept_id having avg(age) > 20 );

import requests
import re
import xlsxwriter
from bs4 import BeautifulSoup
from datetime import datetime
import codecs
import threading
# 下载图片
def download_img(imageurl, image_dir, imageName="xxx.jpg"):
    rsp = requests.get(imageurl, stream=True)
    image = rsp.content
    path = image_dir + imageName + '.jpg'
    with open(path, 'wb') as file:
        file.write(image)


def crawler(s, i, url, header, image_dir, worksheet, txtfile):
    postData = {"start": i}  # post数据
    res = s.post(url, data=postData, headers=header)  # post
    soup = BeautifulSoup(res.content.decode(), "html.parser")  # BeautifulSoup解析
    table = soup.findAll('table', {"width": "100%"})  # 找到所有图书信息的table
    sz = len(table)  # sz = 25,每页列出25篇文章
    for j in range(1, sz + 1):  # j = 1~25
        sp = BeautifulSoup(str(table[j - 1]), "html.parser")  # 解析每本图书的信息

        imageurl = sp.img['src']  # 找图片链接
        bookurl = sp.a['href']  # 找图书链接
        bookName = sp.div.a['title']
        nickname = sp.div.span  # 找别名
        if (nickname):  # 如果有别名则存储别名否则存’无‘
            nickname = nickname.string.strip()
        else:
            nickname = ""

        notion = str(sp.find('p', {"class": "pl"}).string)  # 抓取出版信息,注意里面的.string还不是真的str类型
        rating = str(sp.find('span', {"class": "rating_nums"}).string)  # 抓取平分数据
        nums = sp.find('span', {"class": "pl"}).string  # 抓取评分人数
        nums = nums.replace('(', '').replace(')', '').replace('\n', '').strip()
        nums = re.findall('(\d+)人评价', nums)[0]
        download_img(imageurl, bookName)  # 下载图片
        book = requests.get(bookurl)  # 打开该图书的网页
        sp3 = BeautifulSoup(book.content, "html.parser")  # 解析
        taglist = sp3.find_all('a', {"class": "  tag"})  # 找标签信息
        tag = ""
        lis = []
        for tagurl in taglist:
            sp4 = BeautifulSoup(str(tagurl), "html.parser")  # 解析每个标签
            lis.append(str(sp4.a.string))

        tag = ','.join(lis)  # 加逗号
        the_img = "I:\\douban\\image\\" + bookName + ".jpg"
        writelist = [i + j, bookName, nickname, rating, nums, the_img, bookurl, notion, tag]
        for k in range(0, 9):
            if k == 5:
                worksheet.insert_image(i + j, k, the_img)
            else:
                worksheet.write(i + j, k, writelist[k])
            txtfile.write(str(writelist[k]))
            txtfile.write('\t')
        txtfile.write(u'\r\n')


def main():
    now = datetime.now()  # 开始计时
    print(now)

    txtfile = codecs.open("top2501.txt", 'w', 'utf-8')
    url = "http://book.douban.com/top250?"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36",
        "Referer": "http://book.douban.com/"
        }

    image_dir = "I:\\douban\\image\\"
    # 建立Excel
    workbookx = xlsxwriter.Workbook('I:\\douban\\booktop250.xlsx')
    worksheet = workbookx.add_worksheet()
    format = workbookx.add_format()
    # format.set_align('justify')
    format.set_align('center')
    # format.set_align('vjustify')
    format.set_align('vcenter')
    format.set_text_wrap()

    worksheet.set_row(0, 12, format)
    for i in range(1, 251):
        worksheet.set_row(i, 70)
    worksheet.set_column('A:A', 3, format)
    worksheet.set_column('B:C', 17, format)
    worksheet.set_column('D:D', 4, format)
    worksheet.set_column('E:E', 7, format)
    worksheet.set_column('F:F', 10, format)
    worksheet.set_column('G:G', 19, format)
    worksheet.set_column('H:I', 40, format)

    item = ['书名', '别称', '评分', '评价人数', '封面', '图书链接', '出版信息', '标签']
    for i in range(1, 9):
        worksheet.write(0, i, item[i - 1])

    s = requests.Session()  # 建立会话
    s.get(url, headers=header)

    thread = []

    for i in range(0, 250, 25):
        geturl = url + "/start=" + str(i)  # 要获取的页面地址
        print("Now to get " + geturl)
        t = threading.Thread(target=crawler,
                             args=(s, i, url, header, image_dir, worksheet, txtfile))
        thread.append(t)

    for i in range(0, 10):
        thread[i].start()

    for i in range(0, 10):
        thread[i].join()

    end = datetime.now()  # 结束计时
    print(end)
    print("程序耗时： " + str(end - now))
    txtfile.close()
    workbookx.close()


if __name__ == '__main__':
    main()