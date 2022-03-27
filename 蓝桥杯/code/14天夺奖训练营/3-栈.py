'''
python栈
'''
class myStack:
    def __init__(self):
        self._data = []

    #判空函数
    def isEmpty(self):
        return self._data == []

    #入栈函数
    def push(self , val):
        self._data.append(val)
    #出栈函数
    def pop(self):
        if self.isEmpty():
            return
        return self._data.pop()
    #取栈顶元素
    def top(self):
        if self.isEmpty():
            return
        return self._data[-1]
