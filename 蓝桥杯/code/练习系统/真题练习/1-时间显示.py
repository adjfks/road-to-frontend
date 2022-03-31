""" 
http://lx.lanqiao.cn/problem.page?gpid=T2909
"""

n = int(input())
h = n // 1000 // 60 // 60 % 24
m = n // 1000 // 60 % 60
s = n // 1000 % 60
print("{:0>2d}:{:0>2d}:{:0>2d}".format(h,m,s))