str1 = 'hello world'
print(str1)
print(str1[1])
for c in str1:
    print(c)

str2 = "hello,%s" % 'world.'
print(str2)

str3=('Hello','world') #元组
str4='%s,%s' % str3
print(str4)

d={'h':'Hello','w':'World'} #字典
str5='%(h)s,%(w)s' % d
print(str5)

str6 = '%s%%' % 100
print(str6)

from math import pi
str7 = '%.2f' % pi
print(str7)

str8 = '%8f' % pi
print(str8)

str9 = '%12.10f' % pi
print(str9)

from string import Template
d1 = {'x':'hello','y':'world'}
str10 = Template('$x,$y!')
# str10 = str10.substitute(x='hello',y='world')
str10 = str10.substitute(d1)
print(str10)

