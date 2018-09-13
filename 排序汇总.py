def bubble_sort(alist):
    '''
    冒泡排序
    它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
    最坏时间复杂度：O(n^2)
    稳定性：稳定
    :param alist:
    :return:
    '''
    for j in range(len(alist)-1,0,-1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def selection_sort(alist):
    '''
    选择排序
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕。
    最优时间复杂度：O(n^2)
    最坏时间复杂度：O(n^2)
    稳定性：不稳定（考虑升序每次选择最大的情况）
    :param alist:
    :return:
    '''
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

def insert_sort(alist):
    '''
    插入排序
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
    最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
    最坏时间复杂度：O(n^2)
    稳定性：稳定
    :param alist:
    :return:
    '''
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

def quick_sort(alist, start, end):
    """
    快速排序
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，
    整个排序过程可以递归进行，以此达到整个数据变成有序序列。
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n^2)
    稳定性：不稳定
    :param alist:
    :return:
    """
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)

def shell_sort(alist):
    '''
    希尔排序
    记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n^2)
    稳定想：不稳定
    :param alist:
    :return:
    '''
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2
import time
li = [54,26,93,17,77,31,44,55,20,32,58,62,54,21,89,56,32,54,98,74,85,63,14,2,58,74,77,31,44,55,20,32,58,62,1,5,8,9,6,2,4,7,85,2,15,45,63,25452,4,5698,522,5,65,52,214,7,8,96,3,2,55,4,7,8,9,6,5,48,8,52,2,3,6,69,85254,8,55248,987654]
t1 = time.time()
bubble_sort(li)
t2 = time.time()
print(li, t2-t1)
li = [54,26,93,17,77,31,44,55,20]
selection_sort(li)
print(li)