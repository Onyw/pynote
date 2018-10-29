import random
x=[random.randint(0,100) for i in range(20)]
print(x)
y=x[0:10]
y.sort()
x[0:10]=y
y=x[10:20]
y.sort(reverse=True)
x[10:20]=y
print(x)

