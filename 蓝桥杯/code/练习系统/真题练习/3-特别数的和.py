""" 
http://lx.lanqiao.cn/problem.page?gpid=T2701
"""



def check(num):
  s = str(num)
  if '2' in s or '0' in s or '1' in s or '9' in s:
    return True
  else:
    return False

n = int(input())
sum = 0
for i in range(1, n+1):
  if check(i):
    sum = sum + i

print(sum)