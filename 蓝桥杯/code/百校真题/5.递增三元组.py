""" 
给定三个整数数组
A = [A1, A2, … AN],
B = [B1, B2, … BN],
C = [C1, C2, … CN]，
请你统计有多少个三元组(i, j, k) 满足：

1 <= i, j, k <= N
Ai < Bj < Ck
输入
第一行包含一个整数N。 第二行包含N个整数A1, A2, … AN。 第三行包含N个整数B1, B2, … BN。 第四行包含N个整数C1, C2, … CN。
输出
一个整数表示答案
样例输入
3
1 1 1
2 2 2
3 3 3
样例输出
27
 """

n = int(input())
a = [i for i in map(int, input().split())]
b = [i for i in map(int, input().split())]
c = [i for i in map(int, input().split())]

# 暴力求解
# res = 0
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if a[i] < b[j] < c[k]:
#                 res += 1

# print(res)

a.sort()
b.sort()
c.sort()

i, k = 0, 0
res = 0
for j in range(n):
    while i < n and a[i] < b[j]:
      i += 1
    while k < n and c[k] <= b[j]:
      k += 1
    res += i * (n - k)
print(res)
    
