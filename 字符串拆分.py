"非正则"
x='i am a teacher,i am man, and i am 38 years old. I am not a businessman.'
x=x.replace('i ','I ')
print(x)
"正则"
import re
x='i am a teacher,i am man, and i am 38 years old. I am not a businessman.'
print(re.sub(r'\bi\s',r'I ',x))
