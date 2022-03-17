""" 
问题描述
　　1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。
输出格式
　　按从小到大的顺序输出满足条件的四位十进制数。
"""
res = []
for num in range(10, 100):
    res.append(str(num) + str(num)[::-1])
for num in sorted(map(int, res)):
    print(num)
