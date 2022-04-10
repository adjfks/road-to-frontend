""" 
5 2 6 1 7 3 4 0
 """

arr = [i for i in map(int, input().split())]
arr.pop()

# 交换两个数


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# 快排


def quickSort(arr, l, r):
    if l < r:
        i = l
        j = r
        base = arr[l]
        while i < j:
            while i < j and arr[j] >= base:
                j -= 1
            swap(arr, i, j)
            while i < j and arr[i] < base:
                i += 1
            swap(arr, i, j)
        quickSort(arr, 0, l - 1)
        quickSort(arr, j + 1, r)


quickSort(arr, 0, len(arr) - 1)
for num in arr:
    print(num, end=" ")

# arr = [i for i in map(int, input().split())]
# # 处理 0 值，不参与排序
# if 0 in arr:
#     arr.remove(0)

# def swap(arr, i, j):
#     """位置互换"""
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr

# def QuickSort(arr, start, end):
#     if start < end:
#         i, j = start, end
#         base = arr[i]  # 设置基数
#         while i < j:
#             while i < j and arr[j] >= base:  # 从后往前找
#                 j -= 1
#             swap(arr, i, j)  # 当找到比基数小的数与其互换位置
#             while i < j and arr[i] <= base:  # 从前往后找
#                 i += 1
#             swap(arr, i, j)  # 当找到比基数大的数与其互换位置
#         # 递归
#         QuickSort(arr, start, i - 1)
#         QuickSort(arr, j + 1, end)
#         return arr

# res = QuickSort(arr, 0, len(arr) - 1)
# for x in res:
#     print(x, end=' ')
