# 得到输入的字符串
originStr = ''.join(input().split())
# 字符串长度
n = len(originStr)
# 结果
res = []
# 生成子集
for i in range(2 ** n):
  # 子集
  sub = ''
  # 得到该种情况的二进制字符串并反转
  binStr = bin(i)[2:][::-1]
  # 遍历字符串组合得到子集
  for j in range(len(binStr)):
    if binStr[j] == '1':
      sub = sub + originStr[j]
  res.append(sub)

print(originStr)
print(res)
      



