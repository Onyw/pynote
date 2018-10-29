import re
def wordcount(file):
    with open(file) as file:
       lst=file.read()
    n=re.findall(r'\w+',lst)
    m=set(n)
    a=list(m)
    for x in range(len(a)):
        sum=0
        for y in range(len(n)):
            if a[x]==n[y]:
                sum+=1
        print("%s出现：%d次" %(a[x],sum))
wordcount('f:/python代码/需要的文件/test.txt')
