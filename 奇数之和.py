while True:
   a=input("输出一个数：")
   a=int(a)
   sum=0
   for i in range(1,a+1):
       if i%2!=0:
           sum+=i
   print(sum)


