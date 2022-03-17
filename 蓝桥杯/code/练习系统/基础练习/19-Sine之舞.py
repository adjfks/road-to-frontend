""" 
问题描述
　　最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。
　　不妨设
　　An=sin(1–sin(2+sin(3–sin(4+...sin(n))...)
　　Sn=(...(A1+n)A2+n-1)A3+...+2)An+1
　　FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。
输入格式
　　仅有一个数：N<201。
输出格式
　　请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。
样例输入
3
样例输出
((sin(1)+3)sin(1–sin(2))+2)sin(1–sin(2+sin(3)))+1
 """


def An(n, arr):
    if n == 1:
        arr[n] = "sin(1)"
        return arr[n]

    if arr[n] != '':
        pre = list(arr[n-1])
    else:
        pre = list(An(n-1, arr))
    if n % 2 == 0:
        pre.insert(1-n, '+')
    else:
        pre.insert(1-n, '-')
    pre.insert(1-n, 'sin(' + str(n) + ')')
    arr[n] = "".join(pre)
    return arr[n]


def Sn(n, s):
    if n == 1:
        s[n] = An(n,arr) + "+1"
        return s[n]
    if s[n-1] != '':
        pre = s[n-1]
    else:
        pre = Sn(n-1, s)
    temp = []
    temp.append(pre[:-3])
    temp.append(pre[-2:])
    temp.insert(0, '(')
    temp.insert(2, '+' + str(n) + ')' + An(n, arr))
    s[n] = "".join(temp)
    return s[n]


n = int(input())
global arr, s
arr = [''] * 202
s = ['']*202
print(Sn(n, s))
