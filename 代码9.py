# 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
# 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列[6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
# [6] = 6 * 6 = 36;
# [2] = 2 * 2 = 4;
# [1] = 1 * 1 = 1;
# [6, 2] = 2 * 8 = 16;
# [2, 1] = 1 * 3 = 3;
# [6, 2, 1] = 1 * 9 = 9;
# 从上述计算可见选定区间[6] ，计算值为36， 则程序输出为36。
# 区间内的所有数字都在[0, 100]的范围内;
import sys
n = int(input())
q = []
line = sys.stdin.readline()[:-1]
p = line.split(" ")
p = [int(p[i]) for i in range(len(p))]
length = len(p)
for i in range(0,length):
    for j in range(0,length):
        min = p[i]
        sum = 0
        for k in range(i,j+1):
            if p[k]<=min:
                min = p[k]
            sum = sum + p[k]
        q.append(min*sum)
q.sort(reverse=True)
print(q[0])
# import sys
# n = int(input())
# for line in sys.stdin:
#     a = line.split()
#     print(a)