import os
import sys

# 请在此输入您的代码
class myStack:
    def __init__(self):
        self._data = []

    #判空函数
    def isEmpty(self):
        return self._data == []

    #入栈函数
    def push(self , val):
        self._data.append(val)
    #出栈函数
    def pop(self):
        if self.isEmpty():
            return
        return self._data.pop()
    #取栈顶元素
    def top(self):
        if self.isEmpty():
            return
        return self._data[-1]

n = int(input())
op = [input().split() for i in range(n)]
stack = myStack()
for i in range(n):
  if op[i][0] == 'in':
    stack.push(op[i][1])
  else:
      cur = stack.pop()
      while cur != op[i][1]:
        cur = stack.pop()
if stack.isEmpty():
  print('Empty')
else:
  print(stack.top())
      


