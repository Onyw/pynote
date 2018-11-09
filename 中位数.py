def maxCommon(a, b):
    while b: a,b = b, a%b
    return a

def minCommon(a, b):
    c = a*b
    while b: a,b = b, a%b
    return c//a

def median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half])/2

# ~x = -x-1
a = 36
b = 21
l = [1,3,4,53,2,46,8,42,82]

if __name__ == '__main__':
    print(median(l))
    print(maxCommon(a,b))
    print(minCommon(a,b))