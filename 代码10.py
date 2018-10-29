#两个队列合为一个并升序排列
def merge_two_sorted_arrays(seq_a,seq_b):

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

    return seq_a


if __name__ == '__main__':
    print(merge_two_sorted_arrays([1,2,4],[0, 1, 2]))
    print(merge_two_sorted_arrays([1, 3, 4], [0, 1, 2, 9]))
    print(merge_two_sorted_arrays([0, 1, 2, 9], [1, 3, 4]))
    print(merge_two_sorted_arrays([1, 2, 3, 5], [4, 6, 7, 8]))
    print(merge_two_sorted_arrays([5, 6, 8, 9], [0, 1, 2, 4]))
    print(merge_two_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]))