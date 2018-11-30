## 注释：

> 单行注释 #

> 多行注释 """ """  '''  '''

> 批量注释

> 中文注释

> cls清空

## 内建函数

> print()   input()   type()  float() int()

单个输出，多个输出，表达式

print("str",end="str")

### 格式化打印   

-  %d（整数） 
-  %f（浮点数）
-  %s（字符串）

```py
print ("He is %d years old"%25)
print("%d"%(10.4))
```



## 变量：

- 没有声明符
- 不需要声明
- 由数字 字母 下划线组成     不能使用$符号   不能以数字开头  区分大小写
- 不支持自增，自减   a+=1
- 不可以使用关键字，保留字

## 数据类型：

### 数字   

- 整数（二进制  0b    八进制  0o    十六进制 0x   科学计数法8e2）
- 浮点数
- 复数    

### 浮点数，整数的转化

>  float()     int()

### 将十进制转化为二进制 八进制  十六进制

- ​	bin() 
- ​    oct() 
    hex()	

### 十六进制和二进制的相互转化

```py
十六进制 to 二进制: bin(int(str,16)) 
二进制 to 十六进制 : hex(int(str,2)) 

二进制 to 十进制 : int(str,n=10) 
def bin2dec(string_num):
    return str(int(string_num, 2))
 
 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
```

| ↓    | 2进制            | 8进制            | 10进制            | 16进制            |
| ---- | -------------- | -------------- | --------------- | --------------- |
| 2进制  | -              | bin(int(x, 8)) | bin(int(x, 10)) | bin(int(x, 16)) |
| 8进制  | oct(int(x, 2)) | -              | oct(int(x, 10)) | oct(int(x, 16)) |
| 10进制 | int(x, 2)      | int(x, 8)      | -               | int(x, 16)      |
| 16进制 | hex(int(x, 2)) | hex(int(x, 8)) | hex(int(x, 10)) | -               |

### 定义方式：

- 单引号  '''str'''
- 双引号 “”“ str"""
- 三引号

### 转义字符：

- r   之后写的为普通字符   \n  \r  \t
- b  后面的字符串是byte (二进制)  在python2中  print()函数操作的全部为byte型数据 在 python3中是Unicode数据
- u  为了python2兼容到python3

## 切片

> str[start: end: step]   step默认为1  可以为负数；

```py
str = "陕西优逸客"
print( str[2:5:] )
```

## 字符串

### 注意：

- 字符串是不可变的

### 字符串的内建函数：

- string.capitalize()  首字母变为大写
- string.lower()  小写
- string.upper() 大写
- string.center(len,"str") 扩充，以string为中心两边填充
- string.ljust(len,"str") 扩充，在string右边填充
- string.rjust(len,"str") 扩充，在string左边填充
- string.count("str",start,end) 在start到end之间str的次数
- string.encode(encoding="utf-8/gbk/gb2312",errors="ignore") 以指定格式编码   //encoding(编码方式)
- string.decode(encoding="utf-8/gbk/gb2312",errors="ignore") 以指定格式解码
- string.endswith(obj,start,end)  是否以obj(某一个字符)结尾
- string.find("str",start,end)  返回str的位置下标，找不到-1；
- string.rfind("str",start,end) 倒着寻找
- string.index("str",start,end)返回str的位置下标，找不到报异常
- string.rindex("str",start,end)倒着寻找
- string.isalnum() 至少有一个字符，并且所有字符都是字母数字，返回boolean值
- string.isalpha()  至少有一个字符，并且所有字符都是字母，返回boolean值
- string.isdecimal() 是否字符串都是十进制的数字
- string.isdigit() 是否字符串都是数字
- string.islower() 是否全部小写
- string.isupper() 是否 全部大写
- string.isspace() 至少为一个字符，string全为空,返回True，否则返回False；
- string.join(seq) 将列表(string)对象用string进行分隔组合为字符串    arr=[1,2,3,4]    =>   ",".join(arr)
- string.split("str",num)将string通过str进行分割，num指定分割次数  
- string.splitlines() 将string通过\n进行分割
- string.strip(["str"]) 在字符串前后删除空格，或者删除str

```py
str = "   山西   "
print(len(str))  获取字符串的长度
str1 = (str.strip())
print(len(str1))  
```

## 列表：

### 语法：

> mylist = [1,2,3,4,5]

### 注意：

- 列表可以保存任意类型数据
- 列表可以使用切片
- 列表是可变的，字符串不可变
- 可以创建空列表，也可以创建只有一个元素的列表
- 可以创建多维列表

### 列表的遍历：

```py
for item in mylist:
print(item,end="")  下标
print(mylist,index(item)) 值
enumerate()   将列表转换为（index,value)or((0,1)(1,2),(2,3),(3,4),(4,5),(5,6))的序列
```

```[]py
mylist = [[1,2],[3,4]]
mylist1 = []
for item in mylist:
	mylist1.append(item)
print(mylist2)  //浅拷贝
import copy
arr = [[1,2],[3,4]]
arr1 = copy.copy(arr) #浅拷贝
arr2 = copy.deepcopy(arr) #深拷贝
```

## 列表函数

- list.append(item)  在列表最后插入元素
- list.insert (index,item) 在指定位置插入item，如果没有index，默认最后插入
- list.extend(list1)  合并两个list数据
- arr + [4,5,6] 合并多个list数据
- list.count(item) 查看某元素在list的次数
- list.index(item) 查看某一元素在list的第一个下标,如果不存在，报异常
- list.pop() 删除最后一个元素
- list.remove(item) 删除list中的元素，有相同的删除第一个
- list.reverse() 将list反转
- list.sort(reverse=True) 排序  默认升序 reverse=True 降序
- list.copy() 浅拷贝
- list.clear() 清空数组

## 元组Tuple

> 定义：mytuple = (1,)

### 注意：

- 元组和列表相似，区别就是元组不能改变
- 元组通过圆括号定义
- 可以使用切片
- 元组可以定义只有一个元素的元组，mytuple=(1,) ,逗号不可缺少
- 空元组

### 操作list/tuple的内建函数

- len(list) 数组的长度
- max() 数组的最大数
- min() 数组的最小数
- list() 将元组转换为列表
- tuple() 将列表转换为元组
- enumerate() 返回下标和元素

## 字典dict

- #### json格式创建

```py
mydict = {"name":"a"}
```

- #### 工厂函数创建

```py
mydict1 = dict(name="小红",age=10) 传入关键字
mydict2 = dict(zip(["name","age"],["小艾"，"24"])) 映射函数方式来构造字典
dict()  创建空字典
mydict3 = dict(['one',1],['two',2]) 可迭代对象方式
```

- #### 字典内建方法

```py
mydict4 = dict.fromkeys(["name1","name2"],"小艾") 批量创建键值
```

- #### 字典访问方式

> mydict[键]

- #### 删除字典属性和方法：

> del.mydict["name"]

- #### 字典的内建函数：

  - ​        dict.get("key","info")  返回key对应的value，没有为none  info指定没找到的错误信息

  - dict.keys() 返回字典中所有的key
  - dict.values() 返回字典中所有的value
  - dict.items() 返回字典中所有的key:value形式数据
  - dict.setdefault(key,value)添加数据
  - dict.pop(key) 删除key
  - dict.popitem() 删除最后一位的key:value
  - dict.clear() 清空dict

## 集合:

> 唯一的不可变的一种无序集合，一个项在集合中只能出现一次，set转换为集合。

- set.add("abc") 添加一项；“abc”看做参数
- set.update() 添加集合
- set.remove() 删除

### 集合的操作：

- 交集     &
- 并集     |
- 差集      -

## boolean：

- True
- False
- None

## 基本算数运算符：

> +-*/ //  %  **(幂运算)

### 注意：

- Python3中，除法无论有无复杂类型，结果都会精确到浮点型。
- +操作两个数字型数据=>加运算
- +操作一个数字型数据=>正数
- +操作的str list tuple =>连接作用
- -加法运算  负数
- *操作两个数字型数据=>乘法运算
- *操作的str list tuple =>重复

### 逻辑运算符：

- and  &
- or  ||
- not  !

### 关系运算符：

- ==
- \>=
- <=
- <
- \>
- js 动态类型  弱类型的语言
- python  动态类型 强类型语言

### 位运算符：

- & 按位与运算符  参与运算的两个值，如果两个 相应位都为1，则该位的结果为1，否则为0 // 源码  反码  补码   补码同源码一样，为负数时，加1
- |  按位或运算符  只要对应的两个二进位有一个为1时，结果为就为1.
- ^  按位异或运算符  当两个对应的二进位相异时，结果为1
- ！按位取反运算符  对数据的两个二进制位取反，即把1变为0，把0变为1
- << 左移位运算符   运算数的各二进位全部左移若干位，由<< 右边的数字指定了移动的位数，高位丢弃，低位补0
- \>> 右移位运算符 把“>>”左边的运算符的各二进位全部右移若干位，>>右边的数字指定了移动的位数。

### 赋值运算符：

- =
- +=
- -=
- *=
- /=
- %=
- **=   幂赋值运算符
- //=   取整除赋值运算符

### 成员运算符：

- in 如果在指定的序列中找到指定的值返回true，否则返回false
- not in  如果在指定的序列中没有找到指定的值返回true，否则返回false

### 身份运算符：

- is   按照地址判断两个标识符是否相等。

### 运算符优先级：

1. **  幂运算符

2. -+  正负

3. */%//  关系运算符

4. +- 

5. \>>  <<

   > 幂运算  正负  算数运算符  关系运算符  赋值运算符  身份  成员 逻辑

## 选择结构：

- ```py
  if 1>2:
  	print("1>2")
  else:
  	print("2>1")


  if 1>2:
  	print("1>2")
  elif 2>1:
  	print("2>1")
  	
  print(结果1  if  表达式  else 结果2)#三元运算符
  ```

- range(start,end,step) #创建序列，start开始下标，end结束，step代表歩进值

- while循环

- 随机数   

  ```py
  import  random 
  num = random.randint(0,100)  
  ```

## 循环中干涉循环的语句：

- continue
- break

## 函数：

> 将完成某一特定功能的代码块集合起来，可以重复使用这些代码块。

### 参数：

- #### 缺省参数：

```py
def fn(name,age=18)
```

- #### 可变参数：

```py
def add(*arr):
	num = 0
	for i in arr:
		num+=i
	print(num)
```

- #### 关键字参数：

```py
def person(name,age=13,**attr):
	print("name:%s"%name)
	print("age:%s"%age)
	print(attr)
person(name = "xn",age = 18,sex = "男"，tel = 45876654123)
```

- #### 参数组合：

> 必选参数>默认参数>可变参数> 关键字参数

### 函数返回值：

> 场景：通过某个函数，处理好数据，想要在外界拿到的处理结果做不同的操作。

- return后续代码不会继续执行
- 值仅返回一次
- 要返回多个数据，整体返回

## 高阶函数：

- 实参高阶函数：把一个函数名当做实参传递给另一个函数

```py
def add(a,b):
    return a + b
def sub(a,b):
    return a - b 
def size(a,b,fn):
    return fn(a,b)
print(size(10,20,sub))
```



- 返回值高阶函数：返回值中包含函数名

```py
def fn1():
    def aa():
        print("this is you")
    return aa

bb = fn1()
bb()
```

## 匿名函数:

> lambda 参数 ：表达式
>
> 可以有多个参数
>
> 表达式不需要return，自动return

```py
1.num = (lambda a,b:a+b)(10,20)  自己调用自己
print(num)
2.fn = lambda a,b:a+b
print(fn(10,20))
匿名函数的调用方法：1.自调用 2.字面量
```

- map(函数，序列)

```py
arr = map(lambda x：x*2,range(1,19))
print(list(arr))
arr = map(lambda x,y：x+y,range(1,19),range(1,19))
print(list(arr))
```

- filter(函数，序列)

```py
filter(lambda x:x>5,range(1,11))
print(list(arr))
```

- import functools    functools.reduce(函数，序列)

```py
res = functools.reduce(lambda x,y:x+y,range(1,11))
print(res)
```

## global:

> 是python唯一看起来像声明语句的语句，但是它并不是一个类型或大小的声明，它是一个命名空间的声明。它告诉python函数打算生成一个或多个全局变量名。即存在于整个模块内部作用域(命名空间)的变量名。声明的同时不能修改。如果修改，必须在修改之前声明。global适用于函数内部修改全局变量的值 

```py
aa = 123
def fn1():
	global aa,bb
	bb = 5
fn1()
```

## nonlocal:

> nonlocal适用于嵌套函数中内部函数修改外部变量的值 

```py 
num1 = 123
def aa():
	num1 = 456
	def bb():
		nonlocal num1
		num1 +=10
	bb()
	print(num1)
aa()
```

## 闭包函数：

>  在一些语言中，在函数中可以定义另一个函数时，如果内部的函数引用了外部函数的变量，则可能闭包。闭包可以用来在一个函数与一组‘私有’变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能保持其永久性。  

```py
def aa():
	num1 = 123
	def bb():
		print(num1)
	return bb
bb = aa()
bb()
```

## 递归函数：

> 如果一个函数在内部不调用其他函数，只调用自己的时候，这个函数就是递归函数。