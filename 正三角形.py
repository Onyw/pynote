n=0
for i in range(100,1000):
    a=i/100
    a=int(a)
    b=(i%100)/10
    b=int(b)
    c=i%10
    if a==b==c:
            n=n+1
            print(i)
    elif a==b and a+b>c and c!=0:
            n=n+1
            print(i)
    elif a==c and a+c>b and b!=0:
            n=n+1
            print(i)
    elif b==c and b+c>a and a!=0:
            n=n+1
            print(i)
print(n)
