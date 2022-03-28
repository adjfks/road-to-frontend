'''
用硬币表示给定数值
1 , 5 , 10 , 25

'''


###方法一：递归
##def countWays(n):
##    if n <= 0:
##        return 0
##    return countWaysCore(n , [1,5,10,25] , 3)
##
####n 为当前要凑的数值
#### coins为硬币面额组成的数组
#### cur为当前可用硬币索引，如1表示可用1，5
##def countWaysCore(n , coins , cur):
##    if cur == 0:
##        return 1
##    res = 0
##    #要0个coins[cur]
##    #要1个coins[cur]
##    #...
##    #要i个coins[cur]
##    for i in range(n // coins[cur] + 1):
##        #剩余金额
##        rest = n - i * coins[cur]
##        res += countWaysCore(rest , coins , cur-1)
##    return res
##
##def main():
##    for i in range(100):
##        print('{}---{}'.format(i , countWays(i)))
##        
##main()


#方法二：迭代，二维数组
def countWays(n):
    res = [[0]*(n+1) for _ in range(4)]
    coins = [1,5,10,25]
    for i in range(4):
        for j in range(n+1):
            if i == 0 or j == 0:
                res[i][j] = 1
            else:
                for k in range(j // coins[i] + 1):
                    rest = j - k * coins[i]
                    res[i][j] = res[i][j] + res[i-1][rest]
    return res[3][n]

def main():
    for i in range(100):
        print('{}---{}'.format(i , countWays(i)))
main()
            





    
