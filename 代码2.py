from collections import defaultdict
d=defaultdict(list)
#list append
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
#set add
e=defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(e)

price={
    'acme':45.23,
    'aapl':612.78,
    'ibm':205.55,
    'hpq':37.20,
    'fb':10.75,
    'ffb':10.75,
    'if':205.55
}
min_price=min(zip(price.values(),price.keys()))
print(min_price)
max_price=max(zip(price.values(),price.keys()))
print(max_price)
price_sorted=sorted(zip(price.values(),price.keys()))
print(price_sorted)
print(price.items())

a=[1,2,5,6,5,2,2,5,4,2,1,9,8,5]
def clean(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
print(list(clean(a)))

#序列出现次数最多的元素
from collections import Counter
#通过一个或多个字典中的值来对列表排序
from operator import itemgetter
#分组
from itertools import groupby
row=[
    {'job':111,'data':'07/01/2012'},
    {'job':211,'data':'09/01/2012'},
    {'job':311,'data':'08/01/2012'},
    {'job':411,'data':'07/01/2012'},
    {'job':511,'data':'09/01/2012'},
]
row.sort(key=itemgetter('data'))
for data,items in groupby(row,key=itemgetter('data')):
    print(data)
    for i in items :
        print(' ',i)
#返回满足布尔值为true的相应元素
from itertools import compress
address=[
    '5412 a clark',
    '5421 b asdf'
]
counts=[0,1]
a=[n==1 for n in counts]
print(list(compress(address,a)))

#多个映射或字典中合并为一个单独的映射并进行查找和检查建是否存在
from collections import ChainMap
a={'x':1,'z':4}
b={'y':2,'z':3}
c=ChainMap(a,b)
print(c['x'],end=' ')
print(c['y'],end=' ')
print(c['z'],end='')

