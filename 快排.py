def QuickSort(arr, low, high):
    i = low
    j = high
    if (i >= j):
        return arr
    temp = arr[low]
    while (i < j):
        while (i < j and arr[j] >= temp):
            j = j - 1
        arr[i] = arr[j]
        print(arr)
        while (i < j and arr[i] <= temp):
            i = i + 1
        arr[j] = arr[i]
        print(arr)
    arr[i] = temp
    print(arr)
    QuickSort(arr, low, i - 1)
    QuickSort(arr, i + 1, high)

if __name__ == '__main__':
    arr = [10, 3, 6, 8, 9, 7, 5, 1, 0]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)
