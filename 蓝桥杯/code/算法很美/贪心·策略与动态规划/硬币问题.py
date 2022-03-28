""" 
面值1,5,10,50,100的硬币各c1,c5,c10,c50,c100个
求n元所需最小硬币数
 """

n = int(input())
coinsCount = list(map(int , input().split()))
coins = [1,5,10,50,100]
res = 0

def solve(money , i , coinsCount):
  global res
  if money == 0:
    return 
  # 计算需要当前面值硬币多少枚
  count = min(money // coins[i] , coinsCount[i])
  res = res + count
  rest = money - count * coins[i]
  # 用剩余面值硬币凑剩余的钱
  solve(rest , i-1 , coinsCount)

solve(n , 4 , coinsCount)
print(res)