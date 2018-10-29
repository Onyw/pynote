# for i in range(1,10):
#     for j in range(1,10):
#         m=i*j
#         print('%dx%d=%d\t' %(i,j,m))


a = "\n".join([' '.join('%d*%d=%d' % (x, y, x*y) for x in range(1,y+1)) for y in range(1,10)])
print(a)