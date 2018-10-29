def s(m,n):
    m=int(m)
    n=int(n)
    sum=0
    for i in range(m,n):
        a=i/100
        a=int(a)
        b=(i%100)/10
        b=int(b)
        c=i%10
        if (a*a*a+b*b*b+c*c*c)==i:
                 print(i)
        else :
            sum=sum+1
    if sum==n-m:
        print('no')
s(300,380)
s(100,120)