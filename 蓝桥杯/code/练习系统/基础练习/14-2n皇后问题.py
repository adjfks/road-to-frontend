""" 问题描述
　　给定一个n*n的棋盘，棋盘中有一些位置不能放皇后。现在要向棋盘中放入n个黑皇后和n个白皇后，使任意的两个黑皇后都不在同一行、同一列或同一条对角线上，任意的两个白皇后都不在同一行、同一列或同一条对角线上。问总共有多少种放法？n小于等于8。
输入格式
　　输入的第一行为一个整数n，表示棋盘的大小。
　　接下来n行，每行n个0或1的整数，如果一个整数为1，表示对应的位置可以放皇后，如果一个整数为0，表示对应的位置不可以放皇后。
输出格式
　　输出一个整数，表示总共有多少种放法。
样例输入
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
样例输出
2
样例输入
4
1 0 1 1
1 1 1 1
1 1 1 1
1 1 1 1
样例输出
0 """

""" 
思路：利用两个深度优先搜索，先放白皇后，白皇后放完再放黑皇后。
用2个一维数组存储白皇后和黑皇后放的位置，数组下标代表行，值代表列。
用2个函数判断一个位置是否可以放置
用1个二维数组接收输入矩阵
"""

n = int(input())
# 方案数
nums = 0
# 二维矩阵标志是否可放置
canInput = []
for i in range(n):
    canInput.append(list(map(int, input().split())))
# 存放白皇后和黑皇后放置的位置
posW = [0] * n
posB = [0] * n

# 判断白皇后是否可放置,i为行数


def checkW(row, col):
    # 是不可放置位置
    if canInput[row][col] == 0:
        return False
    # 第一行随便放
    if row == 0:
        return True
    # 检查之前所有行
    for i in range(row):
        # 当列有放过，不能放 或 对角线不能放：行的差值==列的差值
        if posW[i] == col or abs(row - i) == abs(col - posW[i]):
            return False
    return True


# 判断黑皇后是否可放置,i为行数


def checkB(row, col):
    # 不可放置的位置 或 放了白皇后
    if canInput[row][col] == 0 or posW[row] == col:
        return False
    if row == 0:
        return True
    # 检查之前所有行
    for i in range(row):
        # 当列有放过，不能放 或 对角线不能放：行的差值==列的差值
        if posB[i] == col or abs(row - i) == abs(col - posB[i]):
            return False
    return True

# 白皇后dfs


def dfsW(row):
    # 结束条件
    if row == n:
        # 递归黑皇后
        dfsB(0)
    # 对于每一列
    else:
        for col in range(n):
            # 检查并放置
            if checkW(row, col) == True:
                posW[row] = col
                dfsW(row + 1)
            else:
                continue

# 黑皇后dfs


def dfsB(row):
    if row == n:
        global nums
        nums += 1
    else:
        for col in range(n):
            # 检查并放置
            if checkB(row, col) == True:
                posB[row] = col
                dfsB(row + 1)
            else:
                continue


# 调用
dfsW(0)
print(nums)
