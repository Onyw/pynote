import re
a = u'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
b = "^(http|https).*(?=\?)"
c =  re.match(b,a)
print(c.group())

#将str1中匹配的match传入函数中
def addl(match):
    val = match.group()
    num = int(val) + 1
    return str(num)
str1 = '共有：999'
print(re.sub(r'\d+',addl,str1))
