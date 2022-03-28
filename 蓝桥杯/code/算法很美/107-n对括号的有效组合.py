'''
107.n对括号的组合
'''

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        #左右括号剩余数量，str为当前构建的字符串
        def dfs(lRemain , rRemain , str):
            #结束条件：当前构建字符串长达2n时，加入解集
            if len(str) == 2 * n:
                res.append(str)
                return 
            #当剩余左括号数量大于0时就可以选择
            if lRemain > 0:
                dfs(lRemain - 1 , rRemain , str + "(")
            #当剩余右括号数量大于左括号时就可以选择
            if rRemain > lRemain:
                dfs(lRemain , rRemain - 1 , str + ")")
        dfs(n , n , "")
        return res


s = Solution()
print(s.generateParenthesis(4))
