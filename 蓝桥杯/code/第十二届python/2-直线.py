""" 
本题总分：5分
【问题描述】
在平面直角坐标系中，两点可以确定一条直线。如果有多点在一条直线上，那么这些点中任意两点确定的直线是同一条。

给定平面上2×3个整点{ ( x , y ) | 0 ≤ x < 2 , 0 ≤ y < 3 , x ∈ Z , y ∈ Z } , 即横坐标是0到1(包含0和1)之间的整数、纵坐标是0到2(包含0和2)之间的整数的点。这些点一共确定了11条不同的直线。

给定平面上20×21个整点{ ( x , y ) | 0 ≤ x < 20 , 0 ≤ y < 21 , x ∈ Z , y ∈ Z},即横坐标是0到19(包含0和19)之间的整数、纵坐标是0到20(包含0和20)之间的整数的点。请问这些点一共确定了多少条不同的直线。

"""

from turtle import pos


points = [[x , y] for x in range(20) for y in range(21)]
res = set()
for i in range(len(points)):
  x1,y1 = points[i][0] , points[i][1]
  for j in range(i , len(points)):
    x2,y2 = points[j][0] , points[j][1]
    if x1 == x2:
      continue
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    if (k,b) not in res:
      res.add((k,b))
print(len(res) + 20)  
# 40257
    
    