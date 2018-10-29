import re
while True:
    a=input("输入任意参数：")
    if len(re.findall(r'[0-9]',a))!=len(a):
        print("出错")
    else:
        a=int(a)
        sum=1
        for i in range(1,a+1):
            sum*=i
        print(sum)



      

