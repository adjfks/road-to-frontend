""" 
题目描述
设有 n 个人围坐在圆桌周围，现从某个位置 k 上的人开始报数，报数到 m 的人就站出来。下一个人，即原来的第 m+1个位置上的人，又从 1 开始报数，再报数到 m 的人站出来。依次重复下去，直到全部的人都站出来为止。试设计一个程序求出这 n 个人的出列顺序。

ss

要求一：采用循环链表解决。

要求二：可以使用模拟法，模拟循环链表。

要求三：可以不使用循环链表类的定义使用方式。

输入描述
输入只有一行且为用空格隔开的三个正整数 n,k,m，其含义如上所述。

输出描述
共 n 行，表示这 n 个人的出列顺序。

输入输出样例
示例 1
输入

3 5 8
copy
输出

3
2
1
copy
运行限制
最大运行时间：1s
最大运行内存: 128M
 """

n, k, m = map(int, input().split())


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def createLink(n):
    root = Node(1)
    pre = root
    if n > 1:
        for val in range(2, n+1):
            node = Node(val)
            pre.next = node
            pre = node
        pre.next = root
    return root


if n == 1:
    print('1')
else:
    root = createLink(n)
    res = []
    cur = root
    for _ in range(k-1):
        cur = cur.next
    while True:
        for _ in range(m-1):
            pre = cur
            cur = cur.next
        res.append(cur.val)
        pre.next = cur.next
        cur = pre.next
        # 结束条件为pre和cur都指向同一节点
        if cur == pre:
            break
    res.append(pre.val)

    for val in res:
        print(val)
