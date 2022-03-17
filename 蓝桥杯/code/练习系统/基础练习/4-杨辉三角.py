import queue
""" 
问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。

　　
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。

　　
下面给出了杨辉三角形的前4行：

　　
   1

　　
  1 1

　　
 1 2 1

　　
1 3 3 1

　　
给出n，输出它的前n行。

输入格式
输入包含一个数n。

输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
样例输入
4
样例输出
1
1 1
1 2 1
1 3 3 1
数据规模与约定
1 <= n <= 34。
 """

# 方法一： 二维数组
n = int(input())
nums = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            nums[i][j] = 1
        else:
            # 这里j负数的时候取的是最后一列，最后一列为0（除了最后一个元素）
            nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
for i in range(n):
    for j in range(n):
        if nums[i][j] != 0:
            print(nums[i][j], end=" ")
    print()
