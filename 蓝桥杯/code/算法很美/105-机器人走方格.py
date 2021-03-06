#机器人走方格
'''
只能向右和向下走，返回从左上角到右下角的路线数量
'''

#方法一：打工思维

m,n = map(int , input().split())

res = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if i == 1 or j == 1:
            res[i][j] = 1
        else:
            res[i][j] = res[i-1][j] + res[i][j-1]

print(res[m][n])



#方法二：老板思维，递归
def solve(m,n):
    if m == 1 or n == 1:
        return 1
    return solve(m,n-1) + solve(m-1 , n)

print(solve(m,n))
