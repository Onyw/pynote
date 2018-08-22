from itertools import combinations
a = int(input())
b = input().split()
c = int(input())
word_list2 = combinations(b,c)
sum = 0
sum2 = 0
for i in word_list2:
    sum2 += 1
    if 'a' in i:
       sum += 1
print("%.4f" % (sum / sum2))

#input:
#9
#a b c a d b z e o
#4
#output:
#0.7222

通过itertools模块下的combinations方法
将字符串：abcadbzeo 按4个组合  求包含a的占全部的比例。
('a', 'b', 'c', 'a')
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'b')
('a', 'b', 'c', 'z')
('a', 'b', 'c', 'e')
('a', 'b', 'c', 'o')
('a', 'b', 'a', 'd')
('a', 'b', 'a', 'b')
('a', 'b', 'a', 'z')
('a', 'b', 'a', 'e')
('a', 'b', 'a', 'o')
('a', 'b', 'd', 'b')
('a', 'b', 'd', 'z')
('a', 'b', 'd', 'e')
('a', 'b', 'd', 'o')
('a', 'b', 'b', 'z')
('a', 'b', 'b', 'e')
('a', 'b', 'b', 'o')
('a', 'b', 'z', 'e')
('a', 'b', 'z', 'o')
('a', 'b', 'e', 'o')
('a', 'c', 'a', 'd')
('a', 'c', 'a', 'b')
('a', 'c', 'a', 'z')
('a', 'c', 'a', 'e')
('a', 'c', 'a', 'o')
('a', 'c', 'd', 'b')
('a', 'c', 'd', 'z')
('a', 'c', 'd', 'e')
('a', 'c', 'd', 'o')
('a', 'c', 'b', 'z')
('a', 'c', 'b', 'e')
('a', 'c', 'b', 'o')
('a', 'c', 'z', 'e')
('a', 'c', 'z', 'o')
('a', 'c', 'e', 'o')
('a', 'a', 'd', 'b')
('a', 'a', 'd', 'z')
('a', 'a', 'd', 'e')
('a', 'a', 'd', 'o')
('a', 'a', 'b', 'z')
('a', 'a', 'b', 'e')
('a', 'a', 'b', 'o')
('a', 'a', 'z', 'e')
('a', 'a', 'z', 'o')
('a', 'a', 'e', 'o')
('a', 'd', 'b', 'z')
('a', 'd', 'b', 'e')
('a', 'd', 'b', 'o')
('a', 'd', 'z', 'e')
('a', 'd', 'z', 'o')
('a', 'd', 'e', 'o')
('a', 'b', 'z', 'e')
('a', 'b', 'z', 'o')
('a', 'b', 'e', 'o')
('a', 'z', 'e', 'o')
('b', 'c', 'a', 'd')
('b', 'c', 'a', 'b')
('b', 'c', 'a', 'z')
('b', 'c', 'a', 'e')
('b', 'c', 'a', 'o')
('b', 'c', 'd', 'b')
('b', 'c', 'd', 'z')
('b', 'c', 'd', 'e')
('b', 'c', 'd', 'o')
('b', 'c', 'b', 'z')
('b', 'c', 'b', 'e')
('b', 'c', 'b', 'o')
('b', 'c', 'z', 'e')
('b', 'c', 'z', 'o')
('b', 'c', 'e', 'o')
('b', 'a', 'd', 'b')
('b', 'a', 'd', 'z')
('b', 'a', 'd', 'e')
('b', 'a', 'd', 'o')
('b', 'a', 'b', 'z')
('b', 'a', 'b', 'e')
('b', 'a', 'b', 'o')
('b', 'a', 'z', 'e')
('b', 'a', 'z', 'o')
('b', 'a', 'e', 'o')
('b', 'd', 'b', 'z')
('b', 'd', 'b', 'e')
('b', 'd', 'b', 'o')
('b', 'd', 'z', 'e')
('b', 'd', 'z', 'o')
('b', 'd', 'e', 'o')
('b', 'b', 'z', 'e')
('b', 'b', 'z', 'o')
('b', 'b', 'e', 'o')
('b', 'z', 'e', 'o')
('c', 'a', 'd', 'b')
('c', 'a', 'd', 'z')
('c', 'a', 'd', 'e')
('c', 'a', 'd', 'o')
('c', 'a', 'b', 'z')
('c', 'a', 'b', 'e')
('c', 'a', 'b', 'o')
('c', 'a', 'z', 'e')
('c', 'a', 'z', 'o')
('c', 'a', 'e', 'o')
('c', 'd', 'b', 'z')
('c', 'd', 'b', 'e')
('c', 'd', 'b', 'o')
('c', 'd', 'z', 'e')
('c', 'd', 'z', 'o')
('c', 'd', 'e', 'o')
('c', 'b', 'z', 'e')
('c', 'b', 'z', 'o')
('c', 'b', 'e', 'o')
('c', 'z', 'e', 'o')
('a', 'd', 'b', 'z')
('a', 'd', 'b', 'e')
('a', 'd', 'b', 'o')
('a', 'd', 'z', 'e')
('a', 'd', 'z', 'o')
('a', 'd', 'e', 'o')
('a', 'b', 'z', 'e')
('a', 'b', 'z', 'o')
('a', 'b', 'e', 'o')
('a', 'z', 'e', 'o')
('d', 'b', 'z', 'e')
('d', 'b', 'z', 'o')
('d', 'b', 'e', 'o')
('d', 'z', 'e', 'o')
('b', 'z', 'e', 'o')
