""" 
你一定听说过“数独”游戏。
如下图所示，玩家需要根据9×9盘面上的已知数字，推理出所有剩余空格的数字，并满足每一行、每一列、每一个同色九宫内的数字均含1-9，不重复。
数独的答案都是唯一的，所以，多个解也称为无解。
本图的数字据说是芬兰数学家花了3个月的时间设计出来的较难的题目。但对会使用计算机编程的你来说，恐怕易如反掌了。
本题的要求就是输入数独题目，程序输出数独的唯一解。我们保证所有已知数据的格式都是合法的，并且题目有唯一的解。
格式要求，输入9行，每行9个数字，0代表未知，其它数字为已知。
输出9行，每行9个数字表示数独的解。
输入：

005300000
800000020
070010500
400005300
010070006
003200080
060500009
004000030
000009700

程序应该输出：

145327698
839654127
672918543
496185372
218473956
753296481
367542819
984761235
521839764

再例如，输入：

800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400

程序应该输出：

812753649
943682175
675491283
154237896
369845721
287169534
521974368
438526917
796318452
 """
import sys

def check(table,x , y , i):
  #检查行和列
  for j in range(9):
    if table[x][j] == i or table[j][y] == i:
      return False
  #检查九宫格
  for m in range( (x//3)*3 , (x//3)*3 + 3):
    for n in range( (y//3) * 3 , (y//3) * 3 + 3):
      if table[m][n] == i:
        return False
  return True

def dfs(table, x, y):
  #结束条件
  if x == 9:
    printTable(table)
    sys.exit(0)

  # 该位置没有填过
  if table[x][y] == 0:
    # 遍历数字1到9
    for i in range(1, 10):
      # 检查该数字是否合法，返回布尔值
      isLegal = check(table, x, y, i)
      # 若合法
      if isLegal:
        # 填入该数字i
        table[x][y] = i
        # 状态转移，搜索下一位置
        dfs(table, x+y//8, (y+1) % 9)
    #回溯
    table[x][y] = 0
  #该位置已经填过数字了
  else:
    #搜索下一位置
    dfs(table, x+y//8, (y+1) % 9)

def printTable(table):
  for i in range(len(table)):
    for num in table[i]:
      print(num , end="")
    print('\n')
    

      

def main():
  table = []
  for i in range(9):
    table.append([int(i) for i in input()])
  dfs(table,0,0)
  

main()
    


      
