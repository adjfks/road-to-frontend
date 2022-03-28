'''
108. 子集生成
'''

'''
origin为要生成子集的原数组
cur为当前要选择的元素索引
sub为当前已构建的子集
res为最终结果数组，包含所有构建的子集
'''
def subSet(origin , cur , n):
    # 当索引cur超出，结束递归
    if cur == n:
        res.append(sub)
        return 
    #选择当前元素
    sub.append(origin[cur])
    subSet(origin , cur + 1 , n)
    sub.pop()
    #不选择当前元素
    subSet(origin , cur + 1 , n)

res = []
arr = [1,2,3]
sub = []
subSet(arr , 0 , len(arr))
print(res)
