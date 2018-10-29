import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pyecharts import Bar

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=2307b65a62cf6c799f9ee8ddf0892fce'

headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
   'Referer':'http://music.163.com/song?id=551816010',
   'Origin':'http://music.163.com',
   'Host':'music.163.com'
}

user_data = {
   'params': 'uSSJK1rOndOX4fcJnuPawblXH7Fe+UzIEUEUZjmDFVm3pM5o6X7ZNOXPI5jTHxTsJtsjic7TR/w2B/qxao6ridNsPPMLreC/DCwGtxwjPH7mbfBTZziheKGubDIMsFeapUGkcWRHUTgGmcpMT5upLX8MAu+oHAPsQEYzrtE0xqx3cV110feg6VZf2Ffl9lkq',
   'encSecKey': '9da2de283b4651a99e9bf341dbd59564d4485cc5f8d1925fed03decaf7d3e00dbcb1dae972a17f35e578daef42ab9576e15021347a4c8ff185e8c86a17bc9e265844491f3c7c928d79904acdbb74be36f6ef8bf9380458e96af3a46ebf0b8c98f1f4888b6d0de11999b0fc08c0d265c244f97ce1ede9c427edd24e0212132ddd'
}

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
   item = {
       'nickname':hotcommment['user']['nickname'],
       'content':hotcommment['content'],
       'likedCount':hotcommment['likedCount']
   }
   hotcomments.append(item)

#获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

print(content_list)
print(nickname)
print(liked_count)


bar = Bar("热评中点赞数示例图")
bar.add( "点赞数",nickname, liked_count, is_stack=True,mark_line=["min", "max"],mark_point=["average"])
bar.render(r'F:\python代码\1.html')


content_text = " ".join(content_list)
wordcloud = WordCloud(font_path=r"F:\python代码\simhei.ttf",max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()