def findMinAndMax(L):
    max=L[0]
    min=L[0]
    for i in L:
        if i<=min:
            min=i
        if i>=max:
            max=i
    return (min,max)
print(findMinAndMax([3,4,2,6,3]))

L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)]