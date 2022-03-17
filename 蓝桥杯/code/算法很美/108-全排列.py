"""
108-全排列
"""
#方法一：迭代法

def getPermutation(s):
    n = len(s)
    if n <= 0:
        return []
    res = [s[0]]
    if n == 1:
        return res
    
    #在字符串s的i位置插入字符c的函数
    def insertChar( s , i , c ):
        return s[0:i] + c + s[i:]

    #遍历给定字符串的每一个字符
    for k in range(1,n):
        #遍历前一个全排列集合里的每一个字符串，创建一个新数组更新结果
        new_res = []
        res_len = len(res)
        #遍历字符串里的每一个间隙
        for i in range(res_len):
            cur_char = res[i]
            cur_len = len(cur_char)
            #遍历字符串的每一个间隙
            for j in range(cur_len + 1):
                #在i位置插入新字符生成新排列并加入排列集合
                new_res.append(insertChar(cur_char , j , s[k]))
        res = new_res
    return res

    
        



    
        
            
            
    
