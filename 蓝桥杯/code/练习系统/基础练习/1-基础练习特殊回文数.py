"""
问题描述
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
输入格式
　　输入一行，包含一个正整数n。
输出格式
　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
样例输入
52
样例输出
899998
989989
998899
数据规模和约定
　　1<=n<=54。
 """
# 5位数拆成2+3
# 6位数拆成3+3
# 如果是5位数
# 得到每一个5位回文数(字符串)：str(num) + str(num)[:2][::-1]
# str(num)[:2][::-1]是三位数的前两位反转
# 求各位数字之和 sum(map(int , str(num) + str(num)[:2][::-1]))

n = int(input())
res = []
for num in range(100, 1000):
    if sum(map(int, str(num) + str(num)[:2][::-1])) == n:
        res.append(str(num) + str(num)[:2][::-1])
    if sum(map(int, str(num) + str(num)[::-1])) == n:
        res.append(str(num) + str(num)[::-1])
for num in sorted(map(int , res)):
    print(num)
