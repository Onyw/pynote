def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
#isinstance(x, str) 可以判断变量 x 是否是字符串
print(toUppers(['Hello', 'world', 101]))