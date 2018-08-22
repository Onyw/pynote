if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    bignum = max(arr)
    while max(arr) == bignum:
        arr.remove(bignum)
    print(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    temp = 0
    bignum = 0
    for i in arr:
        if bignum < i:
            bignum = i
    for i in arr:
        if temp < i and i != bignum:
            temp = i
    print(temp)
