l = {}
d = {}
d[1] = 1
l[1] = 1
print(d)
print(l)
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
#键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。
print(len(d))
print(str(d))
#dict.clear()
#清洗
#dict.copy()
#字典浅复制
#dict.fromkeys(seq=, value=)
#创建一个字典，以序列seq中元素做字典的键。val为字典所有键对应的初始值
#dict.get(key,default=)
#返回指定键的值，如果值不在字典中返回default值
#dict.items()
#以列表返回可遍历的（键，值）元组数组
#dict.keys()
#以列表返回一个字典所有的键
#dict.values()
#以列表返回字典中的所有值
