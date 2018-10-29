with open(r'F:/python代码/需要的文件/test.txt','r') as file:
    a=file.readlines()
b=[i.swapcase() for i in a]
with open(r'F:/python代码/需要的文件/test2.txt','w') as file:
    file.writelines(b)