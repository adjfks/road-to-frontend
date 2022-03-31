""" 
http://lx.lanqiao.cn/problem.page?gpid=T2906
"""

n , m = map(int , input().split())
a = [i for i in range(1,n+1)]
operation = []
for i in range(m):
  p1,p2 = map(int , input().split())
  operation.append([p1,p2])

for item in operation:
  p1 = item[0]
  p2 = item[1] - 1
  if p1 == 1:
    a = a[:p2] + sorted(a[p2:])
  else:
    a = sorted(a[:p2+1],reverse=True) + a[p2 + 1:]

for i in a:
  print(i, end=" ")