""" 
有n个人，第i个人重量为wi。每艘船的最大载重量均为C，且最多只能乘两个人。用最少的船装载所有人。

 贪心策略：考虑最轻的人i，如果每个人都无法和他一起坐船（重量和超过C），则唯一的方案是每个人坐一艘
 否则，他应该选择能和他一起坐船的人中最重的一个j

 求需要船的数量
 """

def main():
  # 人的重量
  w = [1,2,3,4,5,6,7,8,9,10]
  # 人数
  n = len(w)
  # 船的承重
  c = 10

  
  w.sort()  # 先对重量排序
  cntOfPerson = n # 剩余的人数
  cntOfBoat = 0 # 使用的船数
  p1 = 0
  p2 = n - 1  #头尾指针
  while cntOfPerson > 0:
    if w[p1] + w[p2] > c: #重量超过承重
      p2 = p2 - 1 
      cntOfPerson = cntOfPerson - 1 #重的那个人自己坐一条船
      cntOfBoat = cntOfBoat + 1 #使用了一条船
    else:
      p1 = p1 + 1
      p2 = p2 - 1
      cntOfPerson = cntOfPerson - 2
      cntOfBoat = cntOfBoat + 1
  print(cntOfBoat)

main()