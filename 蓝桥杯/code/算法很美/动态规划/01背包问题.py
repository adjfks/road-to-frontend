""" 
有n个重量和价值分别为wi，vi的物品，从这些物品中挑选出总重量不超过W的物品，求所有挑选方案中价值总和的最大值。

    1≤n≤100

    1≤wi，vi≤100

    1≤W≤10000

输入：

    n=4
    (w,v)={(2,3),(1,2),(3,4),(2,2)}
    W=5

输出：

    7（选择第0，1，3号物品）

因为对每个物品只有选和不选两种情况，所以这个问题称为01背包。

 """

""" 非记忆型 """
""" w = [2,1,3,2] #重量表
v = [3,2,4,2] #价值表
n = 4 #物品数量
W = 5 #背包承重极限
ww = W #背包剩余容量
ans = dfs(0,ww)
print(ans)

def dfs(i,ww):
  if ww <= 0:
    return 0
  if i == n:
    return 0
  #不选择当前物品的价值
  v2 = dfs(i+1 , ww)
  
  if ww >= w[i]:
    # 选择当前物品的价值
    v1 = v[i] + dfs(i+1 , ww-w[i])
    return max(v1,v2)
  else:
    return v2
 """

""" 改造为记忆型递归 """
w = [2,1,3,2] #重量表
v = [3,2,4,2] #价值表
n = 4 #物品数量
W = 5 #背包承重极限
ww = W #背包剩余容量
# 备忘录
rec = [[-1 for _ in range(W)] for _ in range(4)]
ans = dfs(0,ww)
print(ans)

def dfs(i,ww):
  if ww <= 0:
    return 0
  if i == n:
    return 0
  # 查询
  if rec[i][ww] >= 0:
    return rec[i][ww]
  v2 = dfs(i+1 , ww)
  if ww >= w[i]:
    v1 = v[i] + dfs(i+1 , ww-w[i])
    res =  max(v1,v2)
  else:
    res = v2
  # 记录
  rec[i][ww] = res
  return res

