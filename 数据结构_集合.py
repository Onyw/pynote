#副本是被忽略的
set1 = set([0,1,2,3,0,1,2,3,4,5])
print(set1)
set2 = set([0,1,2,3,4,5])
print(set2)
#集合元素的顺序是随意的
strs = set(['jeff','wong','cnblogs'])
print(strs)
#交集
set3=set([1,2,3])
set4=set([2,3,4])
set5=set3.union(set4)
set6=set3|set4
print(set5)
print(set6)
#add和remove
set7=set([1])
print(set7)
set7.add(4)
print(set7)
set7.remove(4)
print(set7)

import calendar
print(calendar.month(2018, 7))