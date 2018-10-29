import os
from collections import Counter
with open('F:\python代码\公司名称.txt', 'r') as f:
    text = f.read()
    lst = text.split(',')
    print(Counter(lst))