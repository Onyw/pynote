# coding=gbk
import os
import re


def wordcount(file):
    with open(file) as file:
        lst = file.read()
        n = re.findall(r'\w+', lst)
        m = set(n)
        a = list(m)
        for x in range(len(a)):
            sum = 0
            for y in range(len(n)):
                if a[x] == n[y]:
                    sum += 1
            print("%s���֣�%d��" % (a[x], sum))


os.chdir("F:\\python����\\��Ҫ���ļ�\\")
filenames = os.listdir("F:\\python����\\��Ҫ���ļ�\\")
f=open('result.txt','w')
for filename in filenames:
    filepath = os.path.abspath(filename)
    if os.path.splitext(filepath)[1] == '.txt':
      for line in open(filepath):
          f.writelines(line)
      f.write('\n')
f.close()
wordcount('result.txt')
