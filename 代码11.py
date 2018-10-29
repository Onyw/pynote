#两个队列合为一个并升序排列并求出中位数
def findMedianSortedArrays(seq_a,seq_b):

    if seq_a and not seq_b:
        return seq_a

    if not seq_a and seq_b:
        return seq_b

    if not (seq_a and seq_b):
        return None
    # 考虑两个游标分别指向 seq_a 和 seq_b 的尾部，并且同时移动游标
    # 在移动过程中比较元素大小，将较大的元素后置
    cursor_a, cursor_b = len(seq_a) - 1, len(seq_b) - 1
    tail = len(seq_a) + len(seq_b) - 1

    for i in range(len(seq_b)):
        seq_a.append(None)

    # 注意临界条件的选择
    while cursor_b >= 0 and tail >= 0:
        # 不断移动较大的数到最后去
        while cursor_a >= 0 and seq_a[cursor_a] > seq_b[cursor_b]:
            seq_a[tail] = seq_a[cursor_a]
            tail -= 1
            cursor_a -= 1
        else:
            seq_a[tail] = seq_b[cursor_b]
            tail -= 1

        cursor_b -= 1
    print(seq_a)
    if len(seq_a)%2 == 0:
        num1 = int(len(seq_a)/2 - 1)
        num2 = int(len(seq_a)/2)
        r = int(seq_a[num1]) + int(seq_a[num2])
        Nr = r/2
        return Nr
    else:
        num1 = int((len(seq_a)+1)/2-1)
        Nr = seq_a[num1]
        return Nr
if __name__ == '__main__':
    print(findMedianSortedArrays([1, 2, 4], [0, 1, 2]))
    print(findMedianSortedArrays([1,3,4], [0,1,2,9]))
    print(findMedianSortedArrays([0,1,2,9], [1,3,4]))
    print(findMedianSortedArrays([1,2,3,5], [4,6,7,8]))
    print(findMedianSortedArrays([5,6,8,9], [0,1,2,4]))
    print(findMedianSortedArrays([1,2,3], [4,5,6,7,8]))