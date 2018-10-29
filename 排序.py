import random
#############################
# Bubble sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################冒泡
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
#############################
# Selection sort
# Time complexity:
#   - Best: O(n^2)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################选择
def selection_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq
    length = len(seq)
    for i in range(0, length):
        min_index = i
        # MIND HERE
        for j in range(i + 1, length):
            if seq[j] < seq[min_index]:
                min_index = j
        if i != min_index:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq
#############################
# Insertion sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################插入
def insertion_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq
    length = len(seq)
    # MIND HERE: start with 1
    for i in range(1, length):
        val = seq[i]
        j = i
        while j > 0 and seq[j - 1] > val:
            seq[j] = seq[j - 1]
            j -= 1
        seq[j] = val
    return seq

def insert_sort(L):
    #遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    for x in range(1,len(L)):
    #将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
    #range(x-1,-1,-1):从x-1倒序循环到0
        for i in range(x-1,-1,-1):
    #判断：如果符合条件则交换
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp
    return L
#############################
# Shell sort
# Time complexity:
#   - Best: O(n log^2 n)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: No
#############################希尔
def shell_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq
    length = len(seq)
    gap = length // 2
    while gap > 0:
        # MIND HERE
        for i in range(gap, length):
            val = seq[i]
            j = i
            # MIND HERE: `j >= gap`
            while j >= gap and seq[j - gap] > val:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = val
        gap //= 2
    return seq
#############################
# Merge sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(n)
# Stability: Yes
#############################归并
def merge_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq
    def merge(left_, right_):
        from collections import deque
        merged, left_, right_ = deque(), deque(left_), deque(right_)
        while left_ and right_:
            merged.append(left_.popleft() if left_[0] < right_[0] else right_.popleft())
        merged.extend(left_ or right_)
        return list(merged)
    # MIND HERE
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)
#############################
# Heap sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(1)
# Stability: No
#############################堆
def heap_sort(seq=None):
    """Heap sort
    1. build heap
    2. swap with the element on the right side (keep bigger element on the right)
    3. rebuild heap(heapify)
    """
    if seq is None or len(seq) <= 1:
        return seq
    def heapify(seq, index, length):
        max_index = index
        left = index * 2 + 1
        right = index * 2 + 2
        if left < length and seq[left] > seq[max_index]:
            max_index = left
        if right < length and seq[right] > seq[max_index]:
            max_index = right
        if max_index != index:
            seq[index], seq[max_index] = seq[max_index], seq[index]
            heapify(seq, max_index, length)
    def build_heap(seq, length):
        # MIND HERE
        for j in range(length // 2, -1, -1):
            heapify(seq, j, length)
        return seq
    length_ = len(seq)
    seq = build_heap(seq, length_)
    # MIND HERE
    for i in range(length_ - 1, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        heapify(seq, 0, i)
    return seq
#############################
# Quick sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(n^2)
# Space complexity: O(logn) ~ O(n)
# Stability: No
#############################快
def quick_sort(seq=None):
    """Quick sort
    1. choose a pivot
    1. make partition (left < pivot < right)
    """
    if seq is None or len(seq) <= 1:
        return seq
    def partition(left, right):
        pivot = random.randrange(left, right)
        pivot_value = seq[pivot]
        # MIND HERE
        seq[pivot], seq[right] = seq[right], seq[pivot]
        stored_index = left
        for i in range(left, right):
            # MIND HERE
            if seq[i] < pivot_value:
                seq[i], seq[stored_index] = seq[stored_index], seq[i]
                stored_index += 1
        seq[stored_index], seq[right] = seq[right], seq[stored_index]
        return stored_index
    def sort(left, right):
        if left < right:
            pivot = partition(left, right)
            sort(left, pivot - 1)
            sort(pivot + 1, right)
    sort(0, len(seq) - 1)
    return seq
if __name__ == '__main__':
    print(bubble_sort([3, 1, 0, 8]))
    print(selection_sort([3, 1, 0, 8]))
    print(insertion_sort([3, 1, 0, 8]))
    print(shell_sort([3, 1, 0, 8]))
    print(merge_sort([3, 1, 0, 8]))
    print(heap_sort([3, 1, 0, 8]))
    print(quick_sort([3, 0, 1, 8]))
    print(insert_sort([3, 0, 1, 8]))
# def find_dup_numbers1(seq):#找出数组中重复的数字（排序）
#     if seq is None  or len(seq) <= 1:
#         return None
#     seq = merge_sort(seq)
#     seen = []
#     for i in range(1,len(seq)):
#         if seq[i-1] == seq[i]:
#             seen.append(seq[i])
#     return set(seen) or None
# def find_dup_numbers2(seq):#找出数组中重复的数字（二分法）
#     """二分法查找，用时间换空间，提高算法空间效率"""
#     if seq is None or len(seq) <= 1:
#         return None
#     start, end = 1, len(seq) - 1
#     while start <= end:
#         mid = start + (end - start) // 2
#         count = count_range(seq, start, mid)
#         if end == start:
#             if count > 1:
#                 return start
#             else:
#                 break
#         if count > mid - start + 1:
#             end = mid
#         else:
#             start = mid + 1
#     return None
# def count_range(seq, start, end):
#     count = 0
#     for x in seq:
#         if start <= x <= end:
#             count += 1
#     return count
# def find_in_sorted_matrix1(matrix,rows,colums,target):
#     if matrix is None or rows <=0 or colums <=0:
#         return False
#     row,col = 0,colums-1
#     while row < rows and col >=0:
#         k = matrix[row][col]
#         if k == target:
#             return True
#         elif k < target:
#             row += 1
#         elif k > target:
#             col -= 1
#     else:
#         return False
# if __name__ == '__main__':
#     matrix = [
#         [1,2,3,4],
#         [2,3,4,5],
#         [44,45,67,980],
#         [78,89,99,1111]
#     ]
#     print(find_in_sorted_matrix1(matrix,4,4,1111))
#     print(find_dup_numbers1([3,5,2,1,2,5,3,1,4,9]))
#     print(find_dup_numbers2([1,1,2,2,3,3,4,5,5,9]))

