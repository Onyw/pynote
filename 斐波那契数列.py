#斐波那契数列
# def fibonacci(n):
#     if n < 1:
#         return 0
#     result = []
#     for i in range(n):
#         if i < 2:
#             result.append(1)
#         else:
#             result.append(result[-1] + result[-2])
#     return result
# print(fibonacci(5))
#丑数
# def uglyNumber(index):
#     if index < 1:
#         return 0
#     data = [1]
#     index1 = 0
#     index2 = 0
#     index3 = 0
#     temp = 0
#     while temp < index:
#         temp += 1
#         element = min(data[index1] * 2, data[index2] * 3, data[index3] * 5)
#         data.append(element)
#         if data[index1] * 2 == element:
#             index1 += 1
#         if data[index2] * 3 == element:
#             index2 += 1
#         if data[index3] * 5 == element:
#             index3 += 1
#     return data
# print(uglyNumber(20))


def fid(n):
    curr = 0
    next = 1
    count = 0
    while count<n:
        yield next
        curr, next = next, curr+next
        count += 1
if __name__ == '__main__':
    while True:
        a = input("请输入一个正整数：")
        a = int(a)
        for i in fid(a):
            print(i)