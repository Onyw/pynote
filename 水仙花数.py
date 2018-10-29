for x in range(100,1000):
    a=x/100
    "a算出来的数都为浮点数，三次方后会与x不等，需要转换成int类型"
    a=int(a)
    b=(x%100)/10
    "b算出来的数都为浮点数，三次方后会与x不等，需要转换成int类型"
    b=int(b)
    c=x%10
    c=int(c)
    if (a*a*a+b*b*b+c*c*c)==x:
             print(x)
      

