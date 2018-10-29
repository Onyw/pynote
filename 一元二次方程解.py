import re
import math
def YYEC(a,b,c):
    if len(re.findall(r'^-[0-9]+$',a))!=1 and len(re.findall(r'[0-9]',a))!=len(a):
              print("出错")
    elif len(re.findall(r'^-[0-9]+$',b))!=1 and len(re.findall(r'[0-9]',b))!=len(b):
          print("出错")
    elif len(re.findall(r'^-[0-9]+$',c))!=1 and len(re.findall(r'[0-9]',c))!=len(c):
          print("出错")
    else:
          a=int(a)
          b=int(b)
          c=int(c)
          m=b*b-4*a*c
          if m<0:
               print("无解")
          else:
               x=(-b+math.sqrt(m))/(2*a)
               y=(-b-math.sqrt(m))/(2*a)
               print(x)
               print(y)

YYEC('1','-2','1')
#import math
#def quadratic_equation(a, b, c):
#    t = math.sqrt(b * b - 4 * a * c)
#    return (-b + t) / (2 * a),( -b - t )/ (2 * a)