# 集初始化
def set_init(n):
    s = []
    for i in range(n):
        s[i] = i
    return s


# 查询
# 递归
# 查询优化：路径压缩，沿路径返回时，顺便把所属的集改成根结点
# 要并查，必压缩
def find_set(x, s):
    if(x != s[x]):
        # 返回时把上一个人的帮主赋给自己
        s[x] = find_set(s[x])
    return s[x]


# 合并
# def union_set():
