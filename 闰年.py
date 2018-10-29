while True:
    a=input('输入四位整数:')
    a=int(a)
    if a%400==0:
        print('此年为闰年!')
    elif a%4==0 and a%100!=0:
        print('此年为闰年!')
    else:
        print('此年不是闰年!')
