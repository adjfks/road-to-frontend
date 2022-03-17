""" 
问题描述
　　回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。
输入格式
　　输入第一行是两个不超过200的正整数m, n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。
输出格式
　　输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。
样例输入
3 3
1 2 3
4 5 6
7 8 9
样例输出
1 4 7 8 9 6 3 2 5
样例输入
3 2
1 2
3 4
5 6
样例输出
1 3 5 6 4 2
 """

m, n = map(int, input().split())
arr = []
for i in range(m):
    arr.append([i for i in input().split()])


def main():
    # 存储结果
    res = []
    # 确定边界
    left, right, up, down = 0, n - 1, 0, m - 1
    while up < down and left < right:
        # 遍历左列
        for row in range(up, down):
            res.append(arr[row][left])
        # 遍历下行
        for col in range(left, right):
            res.append(arr[down][col])
        # 遍历右列
        for row in range(down, up, -1):
            res.append(arr[row][right])
        # 遍历上行
        for col in range(right, left, -1):
            res.append(arr[up][col])
        # 当前层遍历结束，范围内缩
        left += 1
        right -= 1
        up += 1
        down -= 1
    # up < down and left < right 至少有一个条件不满足时
    # 分2种情况
    #第一种left == right
    if left > right or up > down:
        print(" ".join(res))
        return
    elif left == right and up < down:
        for row in range(up, down + 1):
            res.append(arr[row][left])
    elif left < right and up == down:
        for col in range(left, right + 1):
            res.append(arr[up][col])
    else:
        res.append(arr[left][up])

    print(" ".join(res))


main()
