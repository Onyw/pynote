def bubble_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq
    length = len(seq)
    for i in range(length):
        is_swapped = False
        # MIND HERE
        for j in range(length - 1, i, -1):
            if seq[j - 1] > seq[j]:
                is_swapped = True
                seq[j - 1], seq[j] = seq[j], seq[j - 1]
        if is_swapped is False:
            break
    return seq
a = input()
a = int(a)
c = a
b = []
d = []
min=0
while a>0 :
    x,y = map(int,input().split())
    b.append((x,y))
    a = a-1
b = bubble_sort(b)
for k in range(0,c):
    sum = c-k
    for p in range(k+1,c):
        if b[k][1]>=b[p][1]:
            sum = sum-1
    if sum==1:
        d.append(b[k])
for m in range(0,len(d)):
    print(d[m][0],d[m][1])
