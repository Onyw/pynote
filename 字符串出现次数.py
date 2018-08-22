from itertools import groupby
for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")



************************************************************************



if __name__ == '__main__':
    char = input()
    a = char[0]
    sum = 0
    for i in range(len(char)):
        if a == char[i]:
            sum += 1
        else:
            print((sum,int(a)), end=' ')
            a = char[i]
            sum = 1
    print((sum,int(a)))


