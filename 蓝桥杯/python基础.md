# 蓝桥杯基本信息

## 1. 环境

版本：python 3.8.6

操作系统win7及以上



## 2. 库

只能使用标准库： [python 3标准库](https://docs.python.org/zh-cn/3.8/library/index.html)



## 3、IDLE基本操作

1. 按**tab**自动补齐代码
2. 按下**F5**运行代码
3. **alt+3**注释代码，**alt+4**取消注释

<br/>

# 一、基础

### 1. 字符串

#### （1） split()

```python
#split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#num 默认为-1即分隔所有
str.split(str="", num=string.count(str)).
```



```python
s = "1.1.1.1"
s.split(".",1) #['1', '1.1.1']
```



#### （2）upper()

将字符串中的小写字母转为大写字母。

```python
#str.upper()
```



#### （3）切片

##### 1. 翻转字符串 [::-1]

```python
"123"[::-1] 
#'321'
```



#### (4) 数字字符串转数字列表

```python
list(map(int , "123"))
#[1, 2, 3]
```



### 2.int()

```python
#int() 函数用于将一个字符串或数字转换为整型。
#int(x, base=10)
int('12',16) #18 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
```



### 3. 进制转换函数

#### (1) oct()函数

10进制转8进制

```python
#oct() 函数将一个整数转换成 8 进制字符串。
print(oct(12)) #0o14
```



#### （2） hex()函数

10进制整数转换成16进制，以字符串形式表示。

```python
hex(255)  #'0xff' 
```

返回结果中的字母是小写的

#### （3） bin()函数

10进制整数转2进制，返回二进制字符串

```python
bin(8) #'0b1000'
```



#### （4）转十进制

```python
int('0b1011',2)	#11

int('0o20' , 8)
16
```



### 4. enumerate()函数

```python
#用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#enumerate(sequence, [start=0下标起始位置])

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```



### 5. 字典

#### (1) items()方法

```python
#items() 函数以列表返回可遍历的(键, 值) 元组数组。
#dict.items()

tinydict = {'Google': 'www.google.com',
            'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print("字典值 : %s" % tinydict.items())
#字典值 : dict_items([('Google', 'www.google.com'), ('Runoob', 'www.runoob.com'), ('taobao', 'www.taobao.com')])
```



### 6. for in用法

```python
#遍历字符串
s = 'I love you more than i can say'
for i in s:
    print(i)

#遍历列表
l = ['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']
for i in l:
    print(i)
# 可以获取下表，enumerate每次循环可以得到下标及元素
for i, v in enumerate(l):
    print(i, v)
    
#遍历字典
d = {'a':'apple', 'b':'banana', 'c':'car', 'd': 'desk'}
for key in d:
# 遍历字典时遍历的是键
print(key, d.get(key))
# for key, value in d.items():
# 上下两种方式等价 d.items() <=> dict.items(d)
for key, value in d.items():
    print(key, value)
    
# 列表生成式
print([i for i in range(1, 11)])
print([i*2 for i in range(1, 11)])
print([i*i for i in range(1, 11)])
print([str(i) for i in range(1, 11)])
print([i for i in range(1, 11) if i % 2 == 0])
```



### 7.运算符优先级

![image-20220301115719663](https://gitee.com/PencilX/myblogassets/raw/master/src/202203011157722.png)



### 8. sum()函数

**sum()** 方法对序列进行求和计算。

```python
sum([0,1,2])  #3 
 
sum((2, 3, 4), 1)        #10 元组计算总和后再加 1
```





### 9. sorted()函数

**sorted()** 函数对所有可迭代的对象进行排序操作。

> **sort 与 sorted 区别：**
>
> sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
>
> list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

```python
sorted(iterable, key=None, reverse=False)  
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
```



```python
sorted([5, 2, 3, 1, 4]) 
#[1, 2, 3, 4, 5]  默认为升序

sorted( { 1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A' } ) 
#[1, 2, 3, 4, 5]

sorted("1 2 3 1 9 6") 
#[' ', ' ', ' ', ' ', ' ', '1', '1', '2', '3', '6', '9']

sorted("731053") 
# ['0', '1', '3', '3', '5', '7']

sorted("731053" , reverse=True) 
# ['7', '5', '3', '3', '1', '0']

sorted(["123" , "89" , "2345"])
#['123', '2345', '89']
#字符数字不要直接排序，是一次比较每个字符
```





### 10. 列表

```python
[0]*10
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[[0]*i for i in range(5)] 
#[[], [0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]

s = [1,2,3,4,5]
s[-1] # 5

s = ["1" , "2" , "3"]
"".join(s) # "123"

#列表方法： pop() append() insert()
queue = []
# 末尾添加元素
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)	# [1, 2, 3, 4]
#头部添加元素
queue.insert(0,5)
print(queue) 	#[5, 1, 2, 3, 4]
#弹出最后一个元素
queue.pop()
print(queue)	#[5, 1, 2, 3]
#弹出第一个元素
queue.pop(0)
print(queue)	#[1, 2, 3]

#判断某元素不在列表
if num not in nums:
    print(-1)
    
#获得某元素在列表中的索引
list.index(item)

#移除指定元素
list.remove(num)

#移除指定索引元素
del list[index]
```

remove() 函数用于移除列表中某个值的第一个匹配项。

```python
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
print(aList.remove('xyz'))
```



### 11.bool()函数

**bool()** 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。

```

```



### 12.max()函数和min()函数

max() 方法返回给定参数的最大值，参数可以为序列。

min() 方法返回给定参数的最小值，参数可以为序列。

```python
max(1,4,6,12) 
12  
>>> max([1,3,5]) 
5
>>> max((1,2,5)) 
5
>>>
```



### 13. print

```python
#输出以空格结尾，默认以换行结尾
print(打印内容，sep=" ")
```



### 14. max()、min()和sum()

max() 方法返回给定参数的最大值，参数可以为序列。

min() 方法返回给定参数的最小值，参数可以为序列。

**sum()** 方法对序列进行求和计算。

```

```



### 15. 代码进行封装运行得快一些？



### 16. round()函数

**round()** 方法返回浮点数x的四舍五入值。

有坑

```
round( x [, n]  )
x -- 数值表达式。
n -- 数值表达式，表示从小数点位数。
```



### 17. format()格式化函数

```python
"{1} {0} {1}".format("hello", "world")  # 设置指定位置 'world hello world'

#可以设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com")) #网站名：菜鸟教程, 地址 www.runoob.com

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```

数字格式化

```python
print("{:.2f}".format(3.1415926)) #3.14

"{:.2%}"  保留两位小数的百分比格式 如0.25%

"{:0>3d}".format(3)	#'003' 数字左边补0，总长为3
"{:a<3d}".format(3)  #'3aa' 右边补'a'


"{:0<4d}".format(4)  #'4000' 数字右边补0 总长为4


```





### 18. 闰年2月29天，平年28天，年份%100！=0 且%4\==0或%100==0且%400\==0



### 19. `num >> 1 == num // 2`



### 20. str.zfill（）方法返回指定长度字符串前面补0

```python
# 返回十进制的8位二进制数
def bin8(num):
  return bin(num)[2:].zfill(8)

bin8(15)	#'00001111'
```





### 21 交换两数

```python
a , b = b , a
```



### 22. 字符转化成ASCII码ord(),ASCII码化成字符chr()

```
ord('A') #65

ord('Z') #90

chr(65) #'A'
```





### 23. str.count()

count() 方法用于统计字符串里某个**字符**或**子字符串**出现的次数。可选参数为在字符串搜索的开始与结束位置。



```python
"absddapplefdxxappleddapplexcdapplaa".count("apple")  #3
```

注意统计数值中数字个数时，参数为字符或字符串，带引号

```python
str(13471811182).count('1')	#5
```



### 24、for循环可以与else搭配

若for循环正常执行完则不执行else代码，若由break退出则执行else代码

```python
n = int(input("please enter the number："))
for i in range(2, n):
    if n % i == 0:
        print(" %d is not a prime number！" % n)
        break
else:
    print(" %d is a prime number！" % n)

```





### 25、集合

1. 集合间运算

```python
# 下面展示两个集合间的运算.

a = set('abracadabra')
b = set('alacazam')
>>> a                                  
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
```



2. 添加元素

   ```python
   s.add(x)
   
   s.update(x) #可以添加多个元素，且参数可以是列表，元组，字典等
   
   thisset.update([1,4],[5,6])  
   >>> print(thisset)
   {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
   ```

3. 移除元素

   ```python
   s.remove( x ) #如果元素不存在，则会发生错误。
   
   s.discard( x ) #如果元素不存在，不会发生错误
   ```

   





### 26. 类

```python
x = MyClass()

#类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
def __init__(self):
    self.data = []
    
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
```





### 27. 移位、位与

```python
10 >> 1 #5

10 << 1 #20

#取第n位， num >> (n-1) & 1
>>> bin(12)[2:]
'1100'
>>> 12 >> 3 & 1
1

#取二进制数num的第i位 函数
def getBit(num , i):
	return num >> (i-1) & 1
```





### 28. count()统计列表中某个元素个数

```python
list.count(item)
```





### 29. python正常退出程序

```
import sys
sys.exit(0)
```



## 二、输入输出模板

```python
#输入一个整数
#3
n = int(input())
n = map(int , input())

#输入一行，多个整数
#1 2 3
a,b,c = map(int , input().split())
nums = list(map(int , input))

#第一行输入n,其余n行每行输入一个数字
#3
#4
#5
#6
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
    
    
#字符串 字符用空格隔开
res = "abc"
" ".join(res) # "a b c"

res = ""
res += str(col + 1)
print(" ".join(res))

```









## 三、 库

### 1、 math库

#### (1) 圆周率 math.pi



### (2)math.sqrt(x)求平方根

```python
import math
>>> math.sqrt(100)
10.0
```

**注意点:** 使用此函数返回的永远都是一个 float 类型数据。

可以用于求素数和一个数的所有因数

### 四、 数据结构

#### 1. 链表

```python
class Node():
    def __init__(self,value,next=None,befor=None):
        self.value=value
        self.next=next
        self.befor=befor
        
def createLink():
    root=Node(0)
    tmp=root
    for i in range (1,12) :
        tmp.next=Node(i)
        tmp.next.befor=tmp
        tmp=tmp.next

    tmp.next=None
    return root

def insert(x,root):

    tmp = Node(x)
    tmp.next=root.next
    tmp.next.befor=tmp
    root.next=tmp

def delete(x,root):
    tmp =  root
    while tmp.next != None:
        if tmp.value==x :
            tmp.befor.next=tmp.next
            tmp.next.befor=tmp.befor

        tmp=tmp.next

def show (root):

    tmp = root.next
    while tmp.next != None:
        print(tmp.value,end=" ")
        tmp=tmp.next
    print("")


if __name__=='__main__':

    n=int(input())
    root=createLink()
    # show(root)


    for i in range (n):
        x = int(input())
        delete(x,root)
        insert(x,root)
        show(root)        
```

# 二、python库

## 1、 math库

### (1) 圆周率 math.pi



## (2)math.sqrt(x)求平方根

```python
import math
>>> math.sqrt(100)
10.0
```

**注意点:** 使用此函数返回的永远都是一个 float 类型数据。

可以用于求素数和一个数的所有因数







# 栈

```python
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

```

