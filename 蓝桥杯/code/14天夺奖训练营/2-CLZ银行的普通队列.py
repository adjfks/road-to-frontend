import os
import sys

# 请在此输入您的代码
m = int(input())
operation = []
for i in range(m):
  operation.append(input().split())

v = []
n = []
for i in range(m):
  if operation[i][0] == 'IN':
    if operation[i][2] == 'V':
      v.append(operation[i][1])
    else:
      n.append(operation[i][1])
  else:
    if operation[i][1] == 'V':
      v.pop(0)
    else:
      n.pop(0)

for item in v:
  print(item)
for item in n:
  print(item)
