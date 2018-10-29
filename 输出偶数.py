import random
x=[random.randint(0,100) for i in range(50)]
print(x)
for a in x[100:0:-1]:
    if a%2!=0:
        x.remove(a)

print(x)
