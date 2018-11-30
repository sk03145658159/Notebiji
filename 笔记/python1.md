# python

教程，语法，数据结构 	Tutorial(官网中)

相关的库  Library  Reference（官网中）

python  基于模块 ，实现开源和共享

- 内置模块（python自带功能，直接import使用）
- 自定义模块     （sys.path查询自定义模块和第三方模块的引用目录）
- 第三方模块   （pip安装第三方模块并放在site-package）sys.path.append()追加引用查找路径  

## 注释：

- 单行注释  #
- 多行注释  ***   * **  ，    ’‘’   ‘’‘

## print

- 格式化打印print（“我今年%d”%23）%d整数 %s字符串 %f浮点型    print（“我的%d，我的%d”%(23,23)）
- print("",end="")end确定每行结尾形式  默认为/n换行
- 输出多个数据用逗号隔开，可以不同数据类型一同输出  print(123,"是好事")

## 变量

- 不需要声明符   name=
- type()  判定变量类型
- 变量不需要声明，可以直接给变量赋值，直接使用
- 可以同时为多个变量赋值
- 同Js，但不能使用$符，开头只能为字母或下划线，区分大小写
- 变量可以储存不同的数据类型，并且可以重复赋值
- 不支持自增自减
- 变量名不可以是关键字和保留字
- id()  查看地址

## 数据类型

### 数据型数据

- 二进制  0b开头   八进制0o开头  十六进制0x
- 科学记数法  8e2   10的2次方

### 数据类型转换

- float()   int()

- 将十进制转换为二进制、八进制、十六进制

  bin()  oct()  hex()

### 获取随机数

```python
import random
num=random.randint(0,100)  //产生随机数的范围，能取到100 
random.choice([1,2,3,4])  //从后面的列表中随机返回一个数
```



### 字符串类型数据

- ‘  ‘      ，  “   ”    ，  ’‘’  ‘’‘            ’‘’  ‘’‘可以支持多行文本输出
- 转义字符“\” print(r"")     具有前缀   r:代表后面的字符串是一个普通字符串    b:代表后面的字符串是byte数据，在python2  print函数操作的字符串全部为byte型数据，在python3中是Unicode型数据    u:主要是python2为了兼容python3，转换为Unicode
- 可以利用下标取值
- \n换行  \t制表  \r回车   
- 不可变量
- len(str)  确定字符串长度

### 字符串的内建函数

- String.capitalize()   把字符串的第一个字符大写
- String.upper()     将字符串转化为大写
- String.lower()     将字符串转化为小写
- String.center(len长度，“str”)   以string为中心两边填充，致使string长度为len
- string.rjust((len长度，“str”)   在string左边填充str，致使长度为len
- string.ljust((len长度，“str”)     在stringy右边填充str，致使长度为len
- string.count（“str”，start，end）从start到end之间的str次数
- string.encode(encoding="编码形式utf-8"，errors="ignore错误忽略")以指定格式编码
- string.decode(encoding="解码形式utf-8"，errors="ignore错误忽略")以指定格式解码
- **string.replace('con','newcon',num)  字符串的部分内容替换**,num指定替换次数，默认全部替换
- **string.endswith(“obj”)是否以obj结尾**  
- **string.find("str",start,end)返回str的位置下标，找不到返回-1   从左**
- string.rfind("str",start,end)  从右
- string.index（“str”，start，end）)返回str的位置下标，找不到报异常    从左
- string.rindex（“str”，start，end）)返回str的位置下标，找不到报异常    从右
- string.isalnum()至少有一个字符，并且所有字符都是字母数字，返回bool
- string.isalpha()至少有一个字符，并且所有字符都是字母   返回bool
- string.isdecima()   是否字符串都是十进制的数字
- string.isdigit()是否字符串都是数字
- string.islower()    是否都是小写
- string.isupper()    是否都是大写
- string.isspace() 至少为一个字符，并且string全为空，返回True，否则返回False
- string.join（seq）将列表对象用string进行分割组合为字符串    arr=[1,2,3,4]    =>   ",".join(arr)
- string.split("str",num)将string通过str进行分割num指定分割次数
- string.splitlines()将string通过/n进行分割
- string.strip(["str"])  在字符串前后删除空格，或者删除str
- string.lstrip()
- string.rstrip()
- 使用加号（+）来合并字符串
- string.title()将每个单词的首字母改为大写

### 列表  mylist=[1,2,3,4,5]

- 列表可以保存任意数据类型
- 列表可以使用切片
- **列表是可变的，字符串不可变**
- 可以创建空列表，也可以创建只有一个元素的列表
- 可以创建多维列表
- len()获取列表的长度
- 可以通过下标获取
- string.index（）获取下标

#### 遍历

```py
for item in mylist:
	print(item)    值
	print(mylist.index(item)) 下标
内建函数  enumerate（）将列表转化为((下标)(值))的数列
for index,value in enumerate(mylist):
  print(index,value)
```

##### 浅拷贝和深拷贝(两个单独个体)

```py
import copy  //引入包
copy.copy(arr)  //浅拷贝
copy.deepcopy(arr) //深拷贝
```

#### 列表的内建函数

- list.append(item)   在列表最后插入一个元素
- list.insert(index插入位置，item)  在指定位置插入item，如果没有index默认最后插入
- list.extend(list1)    合并两个list数据   arr+[]+[]合并多个
- list.count(item)查看某元素在list的次数
- list.index(item) 查看某元素在list中第一次出现的下标，如果不存在就报异常
- list.pop()删除最后一个元素    pop(0) 从开头      print(pop()) 输出删除的数据 
- list.remove(item)  删除list中的元素，有相同的删除第一个
- list.reverse()将list反转
- list.sort(reverse=True)  排序   默认升序  reverse=False降序
- list.copy()  浅拷贝
- list.clear()  清空数组
- arr1=["a","b","c","d"]   arr2=[item for item in arr1 if item=="c"]   推倒式查询  arr2=["c"]

### 元组

类似列表，**不过是不能改变的**，当作用到元组里边的数组时，是可以改变的，因为数组是可变的。

- 元组和列表有点类似，区别就是元组元素不可改变
- 元组通过圆括号定义  mytuple（）
- 可以使用切片
- 元组可以定义只有一个元素的元组，mytuple（1，）逗号不可以省略
- 可以定义空元组。

#### 操作list\tuple的内置函数

- len(list)  数组的长度

- max()数组的最大数

- min()数组的最小数

- list()将元组转化为列表

- tuple()将列表转化为元组

- enumerate()返回下标和元素

  ##### 枚举

  ```py
  arr=[12,123,14,1,23]
  for index,val in enumerate(arr):
      print(index,val)
  输出每一项的下标和对应的值
  ```

  ​

## 切片

```py
str1="shshdd"
print(  str[start:end:step]  )start为开始位置默认从0位置开始 end为结束位置，取不到end默认到结尾  step为步进值，默认为1，当step为-1时，顺序为逆着，决定方向
str1="12345678"
print(str1[::],str1[0::2],str1[::-1],str1[-1:-5:-1],str1[-1:3:-1])
```

## 字典

### 创建方式

#### json格式创建

- **json格式**     mydict={1:"a",2:"b",3:"c"}    

#### 工厂函数创建

- 创建空字典     mydict={"name","小白"｝
- 内建函数方式     mydict=dict(name="小红",age=18)
- 映射函数方式   mydict=dict(zip(["name","age"],["小红",18]))
- 可迭代方式   dict（[('one',1),('two',2),('tree',3)]）
- 批量创建

### 字典的访问方式

mydict[键 ]

### 添加属性和方法

mydict[newkey]=value

### 删除字典和属性

- 删除 del mydict[]

### 字典的内建函数

- dict(arr)   arr=[("a",1),("b",2)]  arr=[["a",1],["b",2]]    转化成字典形式

- dict.get("key","info")  返回key对应的value  没有为None   info指定没找到的时候提示词
- dict.keys（）返回字典中所有的key   返回的是一个key的对象，利用list（）转化成列表
- dict.values()  返回字典中所有的value     返回的是一个value的对象，利用list（）转化成列表
- dict.items()  返回字典中所有的key：value形式数据
- dict.setdefault(key,value)  添加数据
- dict.pop(key)  删除key
- dict.popitem()删除最后一位的key:value
- dict.clear()  清空字典
- dict(zip(arr,arr1))    arr=["a","b"]  arr1=[1,2]    粘合成字典形式


**isinstance(arr,int/str/float)**   判断arr的数据类型，是返回True，不是返回False

## 集合   myset=set({1,2,3,4,5})

创建方式

- myset={1,2,5}
- myset=set([1,2,3,4])
- myset=set("string")

唯一的，不可变的对象的一种无序集合，一个项在集合中只出现一次

- 集合的添加
  - [ ] .add
  - [ ] .update
- 集合的删除
  - [ ] .remove
- 集合的操作
  - [ ] —   差集
  - [ ] ｜   并集
  - [ ] &    交集
- 转化成集合
  - [ ] .set()
- 内建函数
  - [ ] add()
  - [ ] update()
  - [ ] remove()

## Python运算符  

### 算数运算符     除法无论有无复杂类型，结果都会精确到浮点型

- 基本运算符
  - [ ] +操作两个数字型数据=>加法运算 \操作的是一个数字型数据=>正数\操作的是str、list、tuple起到连接作用
  - [ ] —   减法运算和负数
  - [ ] *操作两个数字型数据=>乘法运算\操作的是str、list、tuple=>重复
- 特殊运算符
  - [ ] //  向下取整（地板除）
- 逻辑运算符  and（&&），or（｜｜），not（！）
- **python  动态类型，强类型语言，不存在类型的隐式转换（js 动态类型，弱类型语言，存在隐式转换）**
- 算数运算符：+  —   *    /(浮点数除法)    %    //(整除)    **(幂运算)     divmod(13,3)同时获得商和余数，返回一个元组
- 赋值运算符：
- 关系运算符
  - [ ] ==等于，比较对象是否相等
  - [ ] ！=
  - [ ] 》
  - [ ] <
  - [ ] 》=
  - [ ] 《=
- 位运算符
  - [ ] &   按位与运算符：参与运算的两个值，如果两个相应位都为1则该位结果为1，否则为0
  - [ ] ｜ 按位或运算符：只要对应的二个二进位有一个为1时，结果位为1
  - [ ] ^ 按位异或运算符：当两对应的二进位相异时，结果为1
  - [ ] —按位取反运算符：对数据的每个二进制位取反，及把1变成0，把0变成1
  - [ ] ！按位取反运算符  对数据的两个二进制位取反，即把1变为0，把0变为1
  - [ ] << 左移位运算符   运算数的各二进位全部左移若干位，由<< 右边的数字指定了移动的位数，高位丢弃，低位补0
  - [ ] \>> 右移位运算符 把“>>”左边的运算符的各二进位全部右移若干位，>>右边的数字指定了移动的位数。
- 成员运算符
  - [ ] in  如果在指定的序列中找到值返回True，否则返回False
  - [ ] not in  如果在指定的序列中没有找到值返回True，否则返回False
- 优先级
  - [ ] 幂运算符
  - [ ] 正负
  - [ ] 算数运算符
  - [ ] 关系运算符
  - [ ] 赋值运算符
  - [ ] 身份
  - [ ] 成员
  - [ ] 逻辑

## 流程控制

### if

```python
if 1>2:
    print()
//elif 1<2:
    print()
elif 1==2:
    print()//
else:
    print()
```

### 三元运算符

```python
print(结果1 if 表达式 else 结果2)
print（1 if 1>2 else 2）
```

### 创建序列

```python
range(start,end,step)
start开始下标  end结束   step步进值  start和step可以省略  取不到end
九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%s"%(j,i,j*i),end=" ")
    print("")

```

## while

```python
while 条件:
猜字游戏
import random
num=random.randint(0,100)
print(num)
num1=int(input("输入一个0-100的整数"))       
#  input的返回值为字符串
time=0
while True:
    time=time+1
    if time>5:
        print("你输了")
        break
    if num>num1:
        print("猜小了")
    elif num<num1:
        print("猜大了")
    else:
        print("猜对了")
        print("你赢了")
        break
    num1=int(input("输入一个0-100的整数"))  
```

## 循环

```py
for 变量 in 序列":
	......

range（start，end，step）//创建序列

```



for 变量 in 序列：

​	。。。

range（start，end，step）

### 循环中干预循环的语句

- continue   结束本次，开始下一次
- break   终止循环

## 函数

```python
阶乘
def fn(num):
    num1=1
    for i in range(1,num+1):
        num1=num1*i
    return num1
参数的传递可以改变顺序
```

### 注意事项

- 不需要接受参数，也必须要有（）
- 不要遗漏 ：
- 注意缩进

### 参数

#### 缺省参数(默认参数)

调用参数时，缺省参数的值如果没有传入，则被认为时默认值

```python
def fn(num=10)
```

#### 可变参数

定义可变参数和定义list和tuple参数相比，仅仅在参数前面加一个*号，在函数内部，参数number接收到的是一个tuple，因此，函数代码完全不变，但是，调用该函数时可以传入任意个参数，包括0个参数

```python
def cale(*number):
 	print(type(number))
    for i in number:
        print(i)
cale(1,2,3,4,5,6)        
```

#### 关键字参数

```python
def person(name,age=18,**attr):
    print("name:%s"%name)
    print("age:%s"%age)
    print(attr)
person(name="xb",age=18,sex="男",tel=12233121421332)
```



#### 参数组合（不可以采用赋值的形式传参，如name=18）

在python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这四种参数都可以一起使用，或者只用其中某些，但需注意，参数定义的顺序必须是：

必选参数=>默认参数=>可变参数=>关键字参数

## 函数返回值

返回多个值时，以元组的形式返回

```pyth
def fn(a,b):
	return a,b
a,b=fn(10,20)
```

## 高阶函数

- 返回高阶函数

  ```py
  def fn1():
      def aa():
          print("this is aaa")
      return aa
  bb=fn1()
  bb()
  ```

- 实参高阶函数

  ```py
  def add(a,b):
      return a+b
  def jian(a,b):
      return a-b
  def size(a,b,fn):
      return fn(a,b)
  print(size(10,5,add))
  ```

## 匿名函数

```py
lambda 参数(可以有多个参数) : 表达式(只能写一行，不需要return，自动return)
lambda a,b:a+b
自调用 num=(lambda a,b:a+b)(10,20)
字面量调用：fn=lambda a,b:a+b
		   fn(10,20)
经常使用场合：map、reduce、filter
1    map（函数，序列） 使序列的每一项都执行函数
arr=map(lambda x,y:x+y,range(1,11),range(1,11))
print(list(arr))
2    filter(函数，序列)   
arr=filter(lambda x:x>5,range(1,11))
print(list(arr))
3   reduce  可以实现累加累成
import functools
res=functools.reduce(lambda x,y:x*y,range(1,11))  //x为前面形成的集合
print(res)
```

## 全局变量和局部变量

局部变量：函数内部定义的

全局变量：外部定义的

局部是可以访问全局变量的，但是不能改变，若想改变，需使用**global语句声明**

#### global

是python唯一看起来像声明语句的语句，但是它并不是一个类型或大小的声明，它是一个命名空间的声明。它告诉python函数打算生成一个或多个全局变量名。即存在于整个模块内部作用域(命名空间)的变量名。声明的同时不能修改。如果修改，必须在修改之前声明。global适用于函数内部修改全局变量的值 

```py
aa=123
def fn():
	global aa,bb  //也可以添加全局变量
	aa=456
```

#### nonlocal

```py
num1=123
def fn1():
    num1=456
    def fn2():
        nonlocal num1
        num1+=10
    fn2()
    return num1
print(fn1())
```

## 闭包函数

在一些语言中，在函数中可以定义另一个函数时，如果内部的函数引用了外部函数的变量，则可能闭包。闭包可以用来在一个函数与一组‘私有’变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能保持其永久性。  

```py
def aa():
    num1=123
    def bb():
        print(num1)
    return bb
cc=aa()
cc()
```

## 递归函数

#### 定义

如果一个函数在内部不调用其他的函数，而是自己本身的话，这个函数就是递归函数。**设置出口**

```py
def fn(num):
    if num==1:
        return 1
    else:
        return num*fn(num-1)
print(fn(2)) 
```

## 装饰器

#### 三个原则

- 不能修改被装饰的函数的源代码
- 不能修改被装饰的函数的调用方式
- 满足上面的原则的情况下给程序添加功能

#### 例子

```py
import time
def tester(fn):
    def newtest():
        start=time.time()
        fn()
        end=time.time()
        print("运行的总时间为：",end-start)
    return newtest

def test():
    time.sleep(1)
    print("this is test")
test=tester(test)
test()            //函数的柯里化


import time
def tester1(aa):
    def tester(fn):
        def newtest():
            start=time.time()
            fn()
            end=time.time()
            print(aa)
            print("运行的总事件为：",end-start)
        return newtest
    return tester
@tester1(20)
def test():
    time.sleep(1)
    print("this is shenkuo")
test()

```

#### 装饰器定义公式

函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖=装饰器

#### 清屏

```py
import os
os.system("cls")
```

## 面向对象

### 基本语法

```py
class 类名:
	方法列表
*******************例
class play:
	name="sss"				//类属性，静态变量，静态数据
	def __init__(self):     //初始化，定义实例属性。self指向实例化对象,当没有实例化属性时，实例化对像
		self.name="sddd"		会访问类属性，不同的实例化对像可以访问同一个类属性，但无法改变。
	def type(self):         //定义实例方法
		print("")
	@staticmethod     //定义静方法  不能调用实例的属性和方法，同时不能调用类的属性和方法，不能调用类的
	def say():			静态方法
		print("")
	@classmethod    //类方法，不能调用实例的属性和方法，可以调用类的属性和方法，也可以调用静态方法                              (class.say())                                                        
	def sayclass(cls):     
		print("")
		print(cls.name)
```

### 类方法和静态方法

静态方法和类方法都可以通过类或者实例来调用，其两个的特点都是不能够调用实例属性

类属性与类方法是类固有的方法和属性，不会因为实例不同而改变，写他们的目的是为了减少多实例时所创造出来的内存空间，加快运算速度

### 类的自带属性

Class.  __ name__    返回类名

Class.   __ doc __          对类的描述，注释内

 Class.__ bases __    所有的父类，返回一个元组

 Class.__ base __      父类

 Class.__ dict __      以字典的形式返回所有的方法

 Class.__ module __   返回类所在的模块__ main__

   Class.__  class__   返回类对应的类__ type __  

### 特殊实例的方法（魔法方法）不需要调用，自己执行

在python中方法名如果是__ xxxx __()的，那么就有特殊的功能，因此叫做“魔法”方法

- __ new __(cls)    创建对象

- __ new __至少有一个参数cls，代表要实例化的类，此参数在实例化时python自动提供

- __ new __ 必须要有返回值，返回出实例化的实例 ，这点在自己实现__ new __时要特别注意，可以

  return父类 __ new__ 出来的实例，或者直接是object的 __ new __出来的实例

  ```py
  class Myfloat(float):
      def __new__(cls,var,var1,var2):
          return float.__new__(cls,round(var,3))
      def __init__(self,var,var1,var2):
          self.num=var
      def get(self,type):
          return "%0.2f%s"%(self.num,type)
  num=Myfloat(4.1233,1.231,1.3422)
  print(num)
  print(num.get("$"))
  ```

- __ init __(self)  作用是初始化实例，有一个参数是self，这个就是self实例化出来的实例，

  __ int __ 在 __ new __的基础上可以完成完成一些 初始化的动作,不需要返回值

- __ str __(self)   作用：给实例一个描述

  当使用print输出对象的时候，只要自己定义了__ str __(self)方法，那么就会打印从在这个方法中return的数据

   ```py
  __str__方法：
  使用：如：
  class Car:
      def __init__(self, newWheelNum, newColor):
          self.wheelNum = newWheelNum
          self.color = newColor 
      def __str__(self):
          msg = "嘿。。。我的颜色是" + self.color + "我有" + int(self.wheelNum) + "个轮胎..."
          return msg
      def move(self):
          print('车在跑，目标:夏威夷')
  BMW = Car(4, "白色")
  print(BMW)
       总结：
  在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
  当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据 
   ```

- __ repr __()  作用：给实例一个描述

- __ del__()   作用：实例被注销时调用  

- __ dir __()   实例的内建魔法方法，以列表的形式返回实例的属性和方法

### 继承和派生

#### 继承延用父元素的属性和方法

#### 派生在父元素的属性和方法之外新增新的属于子类的方法和属性，包括方法的重写

```py
class B:
	...
class A(B):
静属性和静方法，类属性和类方法，实例属性和实例方法均可继承。当子类定义与父类名字相同的属性或方法时，子类会方法重写（覆盖）。
class C
   .....
class A(B,C)   多继承
   ...
当父类中具有相同的方法或属性时，子类会先从距离自己近的父类中查找，也就是B中，并且尊崇就近原则，深度优先
```

单继承

**多继承：尊崇就近原则，深度优先**

### 派生新的功能

```py
class Myfloat(float):
    def __new__(cls,var,var1,var2):
        return float.__new__(cls,round(var,3))
    def __init__(self,var,var1,var2):
        self.num=var
    def get(self,type):
        return "%0.2f%s"%(self.num,type)
num=Myfloat(4.1233,1.231,1.3422)
print(num)
print(num.get("$"))
***********************************
class Mystr(str):
    def __new__(cls,var):
        return str.__new__(cls,var*2)
string=Mystr("123")
print(string)
```

## 面向对象中的常用内建函数

- issubclass(sub,parent)判断sub是否为parent的子类，返回bool

- isinstance(ins,class)判断ins是否为class的实例，返回bool

- hasattr(obj,"attr")判断obj中是否有attr属性，返回bool

- getattr(obj,"attr")获取obj中attr属性

- setattr(obj,attr,value)设置obj中attr的属性

- delattr(obj,attr)删除obj中attr属性

- **dir()列出类或实例的属性和方法  返回列表型**

- super()寻找父类信息supper(type[object-or-type])

  Python3.x和Python2.x的一个区别是Python3可以直接使用

  supper().xxx代替supper(Class,self).xxx

  ```py
  class B:
  	def __init__(self,val1,val2):
  		self.val1=val1
  		self.val2=val2
  class A(B):
  	def __init__(self,val1,val2):
  		supper().__init__(val1,val2)
  ```

- vars(object)函数返回对象object的属性和属性值的字典对象


### 私有变量

封装（私有化）：对内部数据进行保护（隐藏），或合理的暴露

```py
class Car:
	def __init__(self):
		self.__name="ssd"      //定义前加__
	def setname(self,val):
		self.__name=val        //改变私有属性的方法（在外部无法直接引用修改），也可以利用dir()打印出正确的引用语法。
```

### 单例模式   只有一个实例

```py
class Person:
    __instance=None
    def __new__(cls):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
        return cls.__instance
    def __init__(self):
        pass
    def say(self):
        print(self.name)
print(Person._Person__instance)
p=Person()
print(Person._Person__instance)
p.name="sk"
p1=Person()
print(id(p))
print(id(p1))     //两个实例对像具有相同的地址，是同一个实例
```

### 工厂模式

```py
class Dz():
    def __init__(self):
        self.name="大众"
    def run(self):
        print("启动")
class Bmw():
    def __init__(self):
        self.name="宝马"
    def run(self):
        print("启动")
class factory:
    def Createcar(self,type):
        if type=="dz":
            obj=Dz()
        elif type=="bmw":
            obj=Bmw()
        return obj
factory=factory()
car=factory.Createcar("dz")
print(car.name)
car1=factory.Createcar("bmw")     
print(car1.name)      
```

### 类之间的相互引用，参数的传递（射击实例）

```py
class Ren:
    def __init__(self,name):
        self.name=name
        self.xue=100
        self.qiang=""
    def anzidan(self,danjia,zidan):
        """
        安子弹
        """
        danjia.zhuangzidan(zidan)
    def andanjia(self,danjia):
        """
        安弹夹
        """
        self.qiang.zhuangdanjia(danjia)
    def naqiang(self,qiang):
        """
        拿枪
        """
        self.qiang=qiang
    def kaiqiang(self,ren):
        """
        开枪
        """
        self.qiang.sheji(ren)
    def __str__(self):
        return "name:%s,xue:%s,枪:%s,剩余子弹：%s"%(self.name,self.xue,self.qiang.name,self.qiang.danjia.zidannum)
class Zidan:
    def __init__(self,shanghai):
        self.shanghai=shanghai
    def diaoxue(self,ren):
        """
        掉血
        """
        if ren.xue>0:
            ren.xue-=self.shanghai
        else:
            input("%s死忙，按任意键继续"%ren.name)
class Danjia:
    def __init__(self,size):
        self.rongliang=size
        self.zidannum=0
        self.zidans=[]
    def zhuangzidan(self,zidan):
        if self.zidannum<self.rongliang:
            self.zidannum+=1
            self.zidans.append(zidan)
    def tanchuzidan(self,ren):
        if self.zidannum>0:
            self.zidannum-=1
            self.zidans[-1].diaoxue(ren)
            self.zidans.remove(self.zidans[-1])
class Qiang:
    def __init__(self,name):
        self.name=name
        self.danjia=""
    def zhuangdanjia(self,danjia):
        self.danjia=danjia
    def sheji(self,ren):
        self.danjia.tanchuzidan(ren)
r1 = Ren("小白")
r2 = Ren("小黑")

q1 = Qiang("98k")

q2 = Qiang("AWM")

r1.naqiang(q1)
r2.naqiang(q2)

dj1 = Danjia(30)
dj2 = Danjia(60)

area1 = []
area2 = []

for i in range(100):
    area1.append(Zidan(20))
    area2.append(Zidan(10))

for i in range(50):
    r1.anzidan(dj1,area1[i])
    r2.anzidan(dj2,area2[i])


r1.andanjia(dj1)
r2.andanjia(dj2)

r1.kaiqiang(r2)
r1.kaiqiang(r2)
r1.kaiqiang(r2)


print(r1)
print(r2)      
```



### 异常

当不想让异常影响到下面代码的运行时，利用捕获异常，

#### 异常类

```py
BaseException
 +-- SystemExit  解释器请求退出
 +-- KeyboardInterrupt  用户中断执行（ctr + c）
 +-- GeneratorExit   生成器发生异常来通知退出
 +-- Exception   常规错误基类
      +-- StopIteration 	迭代器没有更多的值
      +-- StopAsyncIteration
      +-- ArithmeticError   数值计算错误基类
      |    +-- FloatingPointError   浮点计算错误
      |    +-- OverflowError    数值运算超出最大限制
      |    +-- ZeroDivisionError    除(或取模)零 (所有数据类型)
      +-- AssertionError    断言语句失败
      +-- AttributeError    对象没有这个属性
      +-- BufferError   
      +-- EOFError  没有内建输入，到达EOF标记
      +-- ImportError   导入模块失败
      |    +-- ModuleNotFoundError
      +-- LookupError   无效数据查询基类
      |    +-- IndexError 序列中没有此索引(index)
      |    +-- KeyError 映射中没有这个键
      +-- MemoryError   内存溢出错误
      +-- NameError 未声明未初始化的本地变量
      |    +-- UnboundLocalError 	访问未初始化的本地变量
      +-- OSError   操作系统错误
      |    +-- BlockingIOError 操作阻塞设置为非阻塞操作的对象（例如套接字）时引发
      |    +-- ChildProcessError 子进程上的操作失败时引发
      |    +-- ConnectionError 连接相关的问题的基类
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError 尝试创建已存在的文件或目录时引发
      |    +-- FileNotFoundError    在请求文件或目录但不存在时引发
      |    +-- InterruptedError 系统调用被输入信号中断时触发
      |    +-- IsADirectoryError 在目录上请求文件操作时引发
      |    +-- NotADirectoryError 在对非目录的os.listdir()事物请求目录操作（例如）时引发
      |    +-- PermissionError 尝试在没有足够访问权限的情况下运行操作时引发 - 例如文件系统权限。
      |    +-- ProcessLookupError 当给定进程不存在时引发
      |    +-- TimeoutError 系统功能在系统级别超时时触发。
      +-- ReferenceError    弱引用(Weak reference)试图访问已经垃圾回收了的对象
      +-- RuntimeError  一般的运行时错误
      |    +-- NotImplementedError  	尚未实现的方法
      |    +-- RecursionError
      +-- SyntaxError 一般的解释器系统错误
      |    +-- IndentationError 缩进错误
      |         +-- TabError    Tab 和空格混用
      +-- SystemError Python 语法错误
      +-- TypeError     对类型无效的操作
      +-- ValueError    传入无效的参数
      |    +-- UnicodeError  Unicode 相关的错误
      |         +-- UnicodeDecodeError  	Unicode 解码时的错误
      |         +-- UnicodeEncodeError  Unicode 编码时错误
      |         +-- UnicodeTranslateError   Unicode 转换时错误
      +-- Warning   警告的基类
           +-- DeprecationWarning   关于被弃用的特征的警告
           +-- PendingDeprecationWarning    关于特性将会被废弃的警告
           +-- RuntimeWarning   可疑的运行时行为(runtime behavior)的警告
           +-- SyntaxWarning    可疑的语法的警告    
           +-- UserWarning  用户代码生成的警告
           +-- FutureWarning    关于构造将来语义会有改变的警告
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

### 异常原理

Try的工作原理，当开始一个try语句后，python就在当前程序的上下文做标记，这样异常出现时就可以回到这里，try子句先执行，接下来发生什么依赖于发生了什么异常

- 如果当try后语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except字句，异常处理完毕，控制流就通过整个try语句
- 如果try后语句发生异常，却没有匹配的except语句，异常将递交上层try，或者到程序的最上层，终止程序，并输出出错信息。
- 如果在try子句执行时没有发生异常，python将执行else语句，然后控制流通过整个try

### except  相对于一个分支，也可以捕获多个异常

当捕获多个异常时，可以把要捕获异常的名字，放到except后，并用元组的方式进行存储

```py
try:               //try起到标记的作用
	print(1/0)     //发生错误，执行except后面的语句
except ZeroDivisionError as e:  //获取异常信息，e为异常类的实例化对象。
	print(e)
except ValueError:     //except分支
	print("发现错误")
except (AssertionError ,ImportError):   //捕获多个异常，利用元组
	print("出错")
else：        //没有捕获到异常时，执行的模块
	print("没有错误")
finally:    //不管有没有异常，都执行的代码
	print("不管有没有异常，都执行的代码")
```

### 自定义异常

自定义异常可以在系统原有的捕获异常情况下添加新的功能

raise可以抛出系统和自定义异常，有异常了  可以用rasie决定异常了该做什么
不过 即使没有异常 也可以raise来定义满足特定条件后抛弃什么异常。当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。

```py
class myExcept(Exception):
    def __init__(self,info):
        self.name="这是我定义的异常"
        self.info=info     #提示信息
    def __str__(self):
        return "myExcept"
num=int(input("输入一个整数"))
if num<0:
    try:
        raise myExcept("myExcept错误")
    except myExcept as e:     //e为异常类的实例化对象
        print(e.info)
```

### 异常的传递性

```py
def A():
    print(1/0)
def B():
    A()
def C():
    B()
try:
    C()
except:
    print("发现异常")
```

### 异常总结

- except语句不是必须的，finally语句也不是必须的，但二者必须要有一个，否则就没有try的意义
- except语句可以有多个，python会按照except语句的顺序依次匹配你指定的异常，如果异常已经处理就不会进入后面的except语句
- except语句可以以元组的形式同时指定多个异常
- **except语句后面如果不指定异常类型，则默认捕获所有异常，你可以通过logging或sys模块获取当前异常**
- 如果要捕获异常后重复抛出，请使用raise，后面不要带任何参数或信息
- 不建议捕获并抛出同一个异常

## 包和模块  由from和import引用的包只会执行一次 

### 模块：每一个py文件都是一个模块

- 模块的链接：import+模块名1，模块名2

### 包：特殊的文件夹（内部必须有一个文件__ init__.py）

- 包的引用：

  - [ ] import +包名.模块名

  - [ ] from 包名 import 模块名(a) as a2     a2相当于给模块a起了一个别名  

  - [ ] from 包名.模块名 import 方法名1,方法名2（直接调用该方法）

        from 包名.模块名 import  *（**全部导入**） 在其中选几个，在模块中定义一个变量__ all __=[方法名1，方法名2.....]     不影响单独引用

- 使用相对路径导入**包中子模块**        （一个 . 表示当前文件夹，两个 .. 表示退出当前文件夹）**相对路径只能在子模块里面使用**

  - [ ] 使用点的这种模式从不是包的目录中导入将会引发错误
  - [ ] 在顶层的脚本的简单模块中，它们将不起作用
  - [ ] 包的部分被作为脚本直接执行，那它们将不起作用

- 主模块运用绝对路径

### 利用命名空间导入目录分散的代码

你可能有大量的代码，由不同的人来分散地维护，每一个部分被组织为文件目录。然而，你希望能用共同的包前缀将所有组件连接起来，不是将每一个部分作为独立的包来安装。

在下面的目录结构里，都有共同的命名空间spam。**在任何一个目录里都没有__ init __.py文件（即都不是包）**

```py
目录结构
xb
	spam
		xbd.py
xm
	spam
		xmd.py
dome.py
代码实现
import sys   //sys.path 操作（查找）目录
sys.path.extend([r"C:\Users\sk109\Desktop\domen\xb",r"C:\Users\sk109\Desktop\domen\xm"])
from spam import xb,xm
print(xb.date)
```

### 将模块分割成多个模块

你想将一个模块分割成多个文件，但是你不想将分离的文件统一成一个逻辑模块时使已有的代码遭到破坏。

例如：假设你想mymodule.py分为两个文件，每个定义一个类

```py
#mymodule.py
class A:
	def spam(self):
		print("A.spam")
class B:
	def spam(self):
		print("B.spam")
```

- 第一步：mymodule目录来代替文件mymodule.py。这个目录下，创建以下文件：

  ```py
  mymodule/
  __init__.py
  a.py
  b.py
  ```

- 第二步：在a.py文件中插入以下代码：

  ```py
  class A:
  	def spam(self):
  		print("A.spam")
  ```

  在b.py文件中插入以下代码：

  ```py
  class B:
  	def spam(self):
  		print("B.spam")
  ```

- 第三步：最后，在__ init __.py中，将两个文件粘合在一起：

  ```py
  #__init__.py
  from .a import A
  from .b import B
  ```

  ​

### 通过字符串名导入模块

你想导入一个模块，但是模块的名字在字符串里。你想对字符串调用导入命令。使用importlib.import_module()  函数来手动导入名字为字符串给出的一个模块或者包的一部分   

import_module只是简单的执行和import相同的步骤，**但是返回生成的模块对象。你只需要将其储存在一个变量，然后像正常的模块一样使用**

```py
import importlib
math=importlib.import_module("math")
math.sin(2)
0.9092974268256817
mod=importlib.import_module("urllib.request")
u=mod.urlopen("http://www.python.org")
```

如果你正在使用的包，import_module()也可用于相对导入。但是，你需要给一个额外的参数

```py
import importlib
b=importlib.import_module(".b",__package__)  #Same as "from . import b"
```



### 读取位于包中的数据文件

假设你的包中的文件组织成如下：

```py
mypackage/
	__init__.py
	somedate.dat
	spam.py
```

现在假设spam.py文件需要读取somedate.date文件中的内容。你可以用以下代码来完成

```py
#spam.py
import pkgutil
data=pkgutil.get_data(__package__,"somedata.dat")
```



### 运行目录或压缩文件

有一个已成长为包含多个文件的应用，它已远不再是一个简单的脚本，你想向用户提供一些简单的方法运行这个程序。

如果你的应用程序已经有多个文件，你可以把你的应用程序放进它自己的目录并添加一个__ main __.py程序。举个例子，你可以像这样创建目录

```py
myapplication/
	spam.py
	bar.py
	grok.py
	__main__.py
```

如果__ main __.py存在，你可以简单地在顶级目录运行Python解释器：python myapplication

解释器将执行__ main __.py文件作为主程序

将你的代码打包成zip文件，这样的技术同样也适用。（需要进入zip文件中）

### 重新加载模块

你想重新加载已经加载的模块，因为你对其源码进行了修改，使用imp.reload来重新加载先前加载的模块

```py
import spam
import imp
imp.reload(spam)
```



### 使用相对路径导入包中子模块

将代码组织成包，想用import语句从另一个包名没有编程过的包中导入子模块，使用包的相对导入，使一个模块导入同一个包的另一个模块，举个例子，假设在你的文件系统上有mypackage包，组织如下：

```py
mypackage/
	__init__.py
	A/
		__init__.py
		spam.py
		grok.py
	B/
		__init__.py
		bar.py
```

如果模块mypackage.A.spam要导入同目录下的模块grok，他应该包括的import语句如下：

```py
#mypackage/A/spam.py
from . import grok
```

如果模块mypackage.A.spam要导入不同目录下的模块B.bar，他应该包括的import语句如下：

```py
#mypackage/A/spam.py
from ..B import bar
```

​	**运行哪个文件，哪个文件就是主模块**

- 使用相对路径导入**包中子模块**        （一个 . 表示当前文件夹，两个 .. 表示退出当前文件夹）**相对路径只能在子模块里面使用**
  - [ ] 使用点的这种模式从不是包的目录中导入将会引发错误
  - [ ] 在顶层的脚本的简单模块中，它们将不起作用
  - [ ] 包的部分被作为脚本直接执行，那它们将不起作用
- 主模块运用绝对路径

## 机器人的制作

```py
qqbot    图灵机器人
from qqbot import QQBotSlot as qqbotslot,RunBot
import requests,json
key="f7d25d87f22e4961aa7dbbf8cd51dd78"
@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content[0:2]=="沈括":
        url="http://www.tuling123.com/openapi/api?key=%s&info=%s"%(key,content[2:])
        res=requests.get(url,content[0:2])
        res.encoding="utf-8"
        obj=json.loads(res.text)
        text=obj['text']
        bot.SendTo(contact,text)
if __name__=="__main__":
    RunBot()
```

## GUI

### tkinter编程

#### tkinter里边的Tk方法

```py
import tkinter as tk
window=tk.Tk()       #创建窗口（顶层窗口）
window.title("我的窗口")  #设置窗口的title
window.geometry('600x300')#设置窗口尺寸  +x+y窗口出现的位置（'600x400+300+300'）
window.resizable(0,0)#重置尺寸的大小,分别是x轴和y轴（0和非0），非0的方向可以改变大小，0的方向不可改变大小，默认都为非0
window.mainloop()    #进行事件循环
```

### Label标签   文本标签

l=tkinter.Lebal(window)

l['text']=""    文本

l['font']=("",20,'blod/italic')   设置字体样式，字体样式，大小，加粗/倾斜

l['bg']=""   设置背景颜色      background

l['fg']=""    设置前景（字体）颜色      foreground

l['width']=    设置宽

l['height']=    设置高

l['anchor']='n'                   n北/s南/w西/e东/c居中/nw/ne/sw/se

l['image']   tk.PhotoImage(file="文件路径.gif/png")

### Button  按钮标签

b=tk.Button(window)

command=fn

b['activebackground']添加点击后的背景颜色

b['activeforeground']添加点击后的字体颜色

b['state']='disable/normal'   disable不可点击，normal可以点击

b['text']=   文本提示

### Entry输入组件

e=tk.Entry(window)

e['state']='normal/disable'

e['show']=""     设置字体表现形式

e['selectbackground']="red"   添加字体选中背景颜色

e['selectforeground']="#fff"   添加字体选中的字体颜色

### 文本域组件  Text

t=tk.Text(window)

t.insert("end",con插入内容)  在末尾插入内容

t.insert("insert",con插入内容)   在选中位置插入内容  （不可以使用下标插入）  

t.get(0.0,tk.END)  获取t中的内容，0.0从第一行到tk.END末尾

t.delete(0.0,tk.END)   删除t中的内容

t.search(con,0.0,'end')  查询con，返回0.0样式的坐标（每次都从头开始找）

在text部分内容添加样式

```py
tag_add()添加Tags
tag_config()设置Tags的样式
如果你对同一个范围内的文本加上多个Tags，并且设置相同的选项，那么新创建的Tag样式会覆盖比较旧的Tag
说道覆盖，我们还可以使用tag_raise,tag_lower来提高或降低某个Tag的优先级（通俗来说就是让Tag变新或变旧）
import tkinter as tk
window=tk.Tk()
t=tk.Text(window)
t.pack()
t.insert(insert,'shdajksad')
t.tag_add('tag1',1.2,1.6)   给tag起个名字，加样式的开始坐标和结束坐标
t.tag_config('tag1',background='yellow')  tag名字，加样式
window.mainloop()
```



```py
import tkinter as tk
window=tk.Tk()       #创建窗口
window.title("我的窗口")  #设置窗口的title
window.geometry('600x300')#设置窗口尺寸
window.resizable(0,0)#重置尺寸的大小,分别是x轴和y轴（0和非0），非0的方向可以改变大小，0的方向不可改变大小，默认都为非0

# str1=tk.StringVar()
#Label  标签 
img1=tk.PhotoImage(file="book1.png")
l1=tk.Label(window)   #实例化Label   第一个参数是主窗口  
#l1=tk.Label(window,text="hello world",font=("",20,"bold italic"))设置字体样式，字体样式，大小，加粗/倾斜
l1['text']="hello world"   #文本
l1['font']=("",20,"bold italic")   #设置字体，利用元组（字体样式，大小，加粗/倾斜）
l1['bg']='#ff6700'    #设置背景色
l1['fg']='#fff'   #前景色
l1['width']=20
l1['height']=1
l1['anchor']='c'       #n北/s南/w西/e东/c居中/nw/ne/sw/se
# l1['image']=img1   #引用图片
# l1['variable']


#Button  按钮标签
num=1
def aa():
    global num
    l1['text']="你好%d"%num
    num=num+1
def fn():
    val=e.get()  #获取e中输入组件的数据
    t.insert('end',val)   #在文本域组件t的末尾添加
def fn1():
    val=e.get()   #获取e中输入组件的数据
    t.insert('insert',val)   #在文本域组件t的选中位置添加
b1=tk.Button(window,text="点击",width=20,height=1,bg="#333",fg="#fff",command=aa)
b2=tk.Button(window,text="插入",width=20,height=1,bg="#333",fg="#fff",command=fn)
b3=tk.Button(window,text="insert",width=20,height=1,bg="#333",fg="#fff",command=fn1)
#输入组件
e=tk.Entry(window)
e['selectbackground']="red"  #选中文字，添加的背景色
e['selectforeground']="blue"  #选中文字，字体的颜色
e['show']="*"  #指定输入的样式
#文本域组件
t=tk.Text(window)
#相对布局
l1.pack()
b1.pack()
e.pack()
b2.pack()
b3.pack()
t.pack()
window.mainloop()    #进行事件循环
```

### 单选按钮   Radiobutton

```py
import tkinter as tk
window=tk.Tk()       #创建窗口
window.title("我的窗口")
window.geometry('600x400')


# l1=tk.Label(window,width=20,height=3,bg="blue",fg="#fff",font=("",20))

# v1=tk.Variable()  #设置可变的值  可变量
# v1.set("A")   #设置初值
# def fn():
#     con=v1.get()    #获取v1的值
#     l1['text']="你选择了%s"%con
# #  单选按钮
# r1=tk.Radiobutton(window,text="A",variable=v1,value="A",command=fn)  当选中时，value赋值给variable
# r2=tk.Radiobutton(window,text="B",variable=v1,value="B",command=fn)
# r3=tk.Radiobutton(window,text="C",variable=v1,value="C",command=fn)
# l1.pack()
# r1.pack()
# r2.pack()
# r3.pack()
v1=tk.Variable()
# v1.set("请输入数据")
v2=tk.Variable()
def fn1():
    con=e.get()
    print(con)
    if len(con)>10:
        return True
    else:
        return False
def fn3():
    con=v2.get()
    print(con)
    if len(con)>10:
        return True
    else:
        return False
def fn2():
    print("长度不够")
def fn4():
    print("22")
e=tk.Entry(window,width=40,textvariable=v1,validate="focusout",validatecommand=fn1,invalidcommand=fn2)#当
#validate focus获取焦点或失去焦点  focusin获取焦点  focusout失去焦点  key输入    引发validate事件后进行验证fn1,验证不对执行fn2
e1=tk.Entry(window,width=40,textvariable=v2,validate="focusout",validatecommand=fn3,invalidcommand=fn2)
b=tk.Button(window,text="登录",width=20,height=1,command=fn4)
e.pack()
e1.pack()
b.pack()
window.mainloop()
```

### 多选按钮Checkbutton

 ```py
import tkinter as tk
window=tk.Tk()
window.title("多选框")
window.geometry("600x400")

v1=tk.Variable()
v2=tk.Variable()
v1.set(0)
v2.set(0)
def fn():
    con1=int(v1.get())
    con2=int(v2.get())
    if con1==1 and con2==0:
        l['text']="我喜欢看电影"
    elif con1==0 and con2==1:
        l['text'] = "我喜欢敲代码"
    elif con1==1 and con2==1:
        l.config(text="都喜欢")
    else:
        l.config(text="都不喜欢")
l=tk.Label(window,width=60,height=3,bg="#333",fg="#fff",font=("",20))
l.pack()
c1=tk.Checkbutton(window,text="看电影",variable=v1,command=fn)   #多选按钮
c1.pack()
c1=tk.Checkbutton(window,text="看电影",variable=v2,command=fn)
c1.pack()

window.mainloop()
 ```

### 登录系统案列

```py
import tkinter as tk
window=tk.Tk()
window.title("登录系统")
window.geometry("600x400")

username,password=False,False

def fn1():
    con=len(en1.get())
    global username
    if con>=10:
        username=True
        l1['text']="成功"
        l1['background']="green"
        l1['foreground']='#fff'
        isOk(username,password)
        return True
    else:
        return False
def fn3():
    con=len(en2.get())
    global password
    if con>=10:
        password=True
        l2['text']="成功"
        l2['background']="green"
        l2['foreground']='#fff'
        isOk(username,password)
        return True
    else:
        return False

def fn2():
    l1['text']="长度不够10位"
    l1['background']="red"
    l1['foreground']='#fff'
def fn4():
    l2['text']="长度不够10位"
    l2['background']="red"
    l2['foreground']='#fff'

def isOk(username,password):
    if username==True and password==True:
        btn1['state']="normal"
    else:
        btn1['state']="disable"

def issuccess():
    u=en1.get()
    p=en2.get()
    if u=='1234567890' and p=='1234567890':
        l3=tk.Label(window)
        l3.place(x=100,y=150)
        l3['text']="登录成功"
        l3['bg']="green"
        l3['fg']="#fff"
        btn1['state']='disable'
    else:
        l3=tk.Label(window)
        l3.place(x=100,y=150)
        l3['text']="输入错误"
        l3['bg']="red"
        l3['fg']="#fff"
tk.Label(window,text="用户名:").place(x=40,y=40)

en1=tk.Entry(window,validate="focusout",validatecommand=fn1,invalidcommand=fn2)
en1.place(x=100,y=40)


l1=tk.Label(window)
l1.place(x=280,y=40)

tk.Label(window,text="密码:").place(x=40,y=80)


en2=tk.Entry(window,validate="focusout",validatecommand=fn3,invalidcommand=fn4)
en2.place(x=100,y=80)


l2=tk.Label(window)
l2.place(x=280,y=80)


btn1=tk.Button(window,text="登录",command=issuccess)
btn1.place(x=100,y=120)
btn1['state']='disable'
btn1['activebackground']="green"
btn1['activeforeground']="#fff"


btn2=tk.Button(window,text="注销")
btn2.place(x=200,y=120)
btn2['state']='normal'
btn2['activebackground']="red"
btn2['activeforeground']="#fff"






window.mainloop()
```



### 下拉列表Listbox

lx1=tk.Listbox(window)

lx1['selectmode']="extend"   设定多选模式

lx1.curselection()   所选择选项对应的的当前下标，元组的形式返回

lx1.insert('end',con内容)   在末尾插入   或者insert(tk.END,con)

lx1.insert(0,con)  可指定下标插入

```py
import tkinter as tk
window=tk.Tk()
window.title("登录系统")
window.geometry("600x400")


l=tk.Label(window,width=10,height=1,bg="#333",fg="#fff")
l.pack()
en=tk.Entry(window)
en.pack()
def fn():
    arr=lxl.curselection()   #index=lxl.curselection()   #所选择的当前下标，元组的形式返回
    con=en.get()
    if con=="":
        return
    elif len(arr)==0:
        lxl.insert('end',con)
    elif len(arr)==1:
        lxl.insert(arr[0]+1,con)
    else:
        num=1
        for item in range(0,len(arr)):
            lxl.insert(arr[item]+num,con)
            num=num+1
btn=tk.Button(window,text="插入",command=fn)
btn['activebackground']="green"
btn['activeforeground']="#fff"
btn.pack()
#下拉列表
lxl=tk.Listbox(window,selectmode="extended")   #selectmode="extended"多选模式
lxl.insert(0,"北京")     #可以指定下标插入
for item in ['上海','广州',"深圳"]:
    lxl.insert("end",item)                             


lxl.pack()
```

下拉列表中添加点击事件，确定下标和读取相对应的值(当事件是下拉列表为事件源时需要传参数e，事件源时其他事不用传参，用第二种方法)

```py
import tkinter as tk
window=tk.Tk()
var=['北京','杭州','上海','广州']
lx1=tk.Listbox(window)
for item in var:
    lx1.insert(tk.END,item)
lx1.pack()
def fn(e):
    index=e.widget.curselection()[0]#获取下拉列表中所选的对应下标，返回元组类型
    val=e.widget.get(index)
    print(val)
    '''
    index=lx1.curselection()
    val=lx1.get(index)    注意传参数e
    '''
lx1.bind('<Double-Button-1>',fn)

window.mainloop()

```



### scale  滑块

```py
import tkinter as tk
window=tk.Tk()
window.title("我的窗口")
window.geometry('600x400')
l1=tk.Label(window)
# l1['bg']='red'
l1['fg']='black'
l1.config({
    'text':"this is labal",
})
l1.pack()
def fn():
    con=s1.get()
    # print(type(con))
    if con>100:
        l1['bg']='red'
    else:
        l1['bg']='green'
    l1['text']='获取的温度是%s'%con
btn=tk.Button(window,text='查询',command=fn)
btn.pack()
e1=tk.Entry(window)
v1=tk.Variable()
v1.set('A')
r1=tk.Radiobutton(window,text='A',variable=v1,value='A')
r2=tk.Radiobutton(window,text='B',variable=v1,value='B')
r1.pack()
r2.pack()
#scale  滑块
def fn1(v):
    pass
s1=tk.Scale(window,command=fn1)#需要传参数，参数自动传送每一次滑动的数值
  #属性
s1.config({
    'orient':tk.HORIZONTAL,   #设置方向 水平方向
    'from_':50,   #设置数值变化范围   默认为0-100
    'to':200,
    'length':500,   #设置滑块长度
    'resolution':10,  #设置滑动的步进值
    'digits':4,   #设置数字的位数
    'tickinterval':50,   #间隔刻度提示  最小为步进值的一半
    'showvalue':1,   #bool 1 0   显示上方的值
    'label':'温度',     #添加滑块文字标签
    #command方法  需要传参数，参数自动传送每一次滑动的数值
})
   #方法
s1.set(150)   #设置默认初值
s1.get()     #获取值
s1.pack()
window.mainloop()
```

### Spinbox  数字框



```py
import tkinter as tk
window=tk.Tk()
window.title("我的窗口")
window.geometry('600x400')
l1=tk.Label(window)
# l1['bg']='red'
l1['fg']='black'
l1.config({
    'text':"this is labal",
})
l1.pack()
def fn1(v):
    # print(float(v))
    if float(v)>100:
        l1['bg']='red'
    else:
        l1['bg']='green'
    l1['text']='获取的温度是%s'%v
    sp1['value']=v
    sp1['value']=""
s1=tk.Scale(window,command=fn1)#需要传参数，参数自动传送每一次滑动的数值，文件执行会自动运行
  #属性
s1.config({
    'orient':tk.HORIZONTAL,   #设置方向 水平方向
    'from_':50,   #设置数值变化范围   默认为0-100
    'to':200,
    'length':500,   #设置滑块长度
    'resolution':1,  #设置滑动的步进值
    'digits':4,   #设置数字的位数
    'tickinterval':50,   #间隔刻度提示  最小为步进值的一半
    'showvalue':1,   #bool 1 0   显示上方的值
    'label':'温度',     #添加滑块文字标签
    #command方法  需要传参数，参数自动传送每一次滑动的数值
})
   #方法
s1.set(150)   #设置默认初值
s1.get()     #获取值
s1.pack()
#Spinbox  数字框
def fn2():    #不需要传参
    num=sp1.get()
    s1.set(num)
sp1=tk.Spinbox(window,command=fn2)
sp1.config({
    "from_":50,     #设定数值范围
    "to":200,
    'width':20,   #设置宽度，没有高度
    # 'value':50    #设置固定值,设为空字符串""就相当于删除了该属性
})
# sp1['values']=('北京','上海','广州')  不仅可以设置数字还可以设置文字  
sp1.get()   #获取值  没有sp1.set()  可以通过value可以设置固定值，设为空字符串""就相当于删除了该属性
sp1.pack()





window.mainloop()
```

### canvas画布

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')

#canvas  画布
can=tk.Canvas(window)
can.config({
    'width':500,
    'height':500,
    'bg':'#ccc'
})
#画图片
img1=tk.PhotoImage(file="book1.png",width=200,height=200)#设置图片的大小
cimg=can.create_image(0,0,image=img1)#图片位置
#画线
cline=can.create_line(0,0,200,200,fill='red')   #开始坐标，结束坐标，填充
#画扇形
carc=can.create_arc(200,200,300,300,extent=270,start=90,fill='blue') #旋转角度，开始旋转角度，填充
#画圆
coval=can.create_oval(300,300,350,350,fill='yellow')
#文本
ctext=can.create_text(50,50,text='Python',font=("",20))
#画多边形
cp=can.create_polygon(0,0,0,100,100,100,fill='green')#确定顶点位置
#画正方形
cr=can.create_rectangle(300,300,500,500,fill='pink')
can.pack()
def fn():
    can.move(coval,-50,-50)#移动方法
btn=tk.Button(window,text='click',command=fn)
btn.pack()

window.mainloop()
```

### Menu 菜单栏

- 首先创建菜单栏，并添加到window上

  ```py
  menubar=tk.Menu(window)#创建菜单栏
  window.configure(menu=menubar)#添加菜单栏
  ```

- 然后创建菜单项（一级菜单），并添加到菜单栏，命名（向谁添加就想谁Menu实例化）

  ```py
  menu1=tk.Menu(menubar,tearoff=False)#创建菜单项,一级菜单，tearroff取消默认可移动样式
  menubar.add_cascade(label='文件(F)',menu=menu1)
  ```

- 菜单项中包括功能和二级菜单

  - [ ] 添加功能

        ```py
        menu1.add_command(label='新建文件(N)',command=fn1)#添加菜单功能项
        fn1为对应功能函数
        ```

  - [ ] 添加二级菜单

        ```py
        向一级菜单Menu实例化，并添加到一级菜单中
        menu1_1=tk.Menu(menu1,tearoff=False)#创建二级菜单
        menu1.add_cascade(label='打开最近的文件(R)',menu=menu1_1)
        ```

- 以后步骤同上

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
#Menu 菜单栏
menubar=tk.Menu(window)#创建菜单栏
menu1=tk.Menu(menubar,tearoff=False)#创建菜单项,一级菜单，tearroff取消默认可移动样式
def fn1():
    pass
menu1.add_command(label='新建文件(N)',command=fn1)#添加菜单功能项
menu1.add_command(label='新建窗口(W)')
menu1.add_separator()#设置分割线
menu1.add_command(label='打开文件(O)')
menu1.add_command(label='打开文件夹(F)')
menu1.add_command(label='打开工作区(K)')
menu1_1=tk.Menu(menu1,tearoff=False)#创建二级菜单
menu1_1.add_command(label='重新打开已关闭的编辑器(R)')
menu1.add_cascade(label='打开最近的文件(R)',menu=menu1_1)
menu1.add_separator()
menu1.add_command(label='将文件添加到工作区(D)')
menu1.add_command(label='将工作区另存为..')
menu1.add_separator()
menu1.add_command(label='保存(S)')
menu1.add_command(label='另存为(A)...')
menu1.add_command(label='全部保存(L)')
menu1.add_separator()
menu1.add_command(label='自动保存(O)')
menu1.add_separator()
menu1_2=tk.Menu(menu1,tearoff=False)#创建二级菜单
menu1_2.add_command(label='设置(S)')
menu1_2.add_separator()
menu1_2.add_command(label='键盘快捷方式(K)')
menu1_2.add_command(label='按键映射扩展(K)')
menu1_2.add_separator()
menu1_2.add_command(label='用户代码片段(S)')
menu1.add_cascade(label='首选项(P)',menu=menu1_2)
menu1.add_separator()
menu1.add_command(label='还原文件(V)')



menubar.add_cascade(label='文件(F)',menu=menu1)

window.configure(menu=menubar)#添加菜单栏

#菜单单选功能   语言选项
yuyan=tk.Variable()
yuyan.set(0)
def fn1():
    print(yuyan.get())
menu1_3=tk.Menu(menu1)
menu1.add_cascade(label='选择语言',menu=menu1_3)
menu1_3.add_radiobutton(label='英语',variable=yuyan,value=0,command=fn1)
menu1_3.add_radiobutton(label='中文',variable=yuyan,value=1,command=fn1)
menu1_3.add_radiobutton(label='俄语',variable=yuyan,value=2,command=fn1)
#菜单选项添加图片
img1=tk.PhotoImage(file="book1.png",width=50,height=50)
menu1_4=tk.Menu(menu1)
menu1_4.add_command(label="图片",image=img1,compound='left')
menu1.add_cascade(label='图片',menu=menu1_4)
#菜单多选功能
s1=tk.Variable()
s2=tk.Variable()
s3=tk.Variable()
s1.set(0)
s2.set(0)
s2.set(0)
def fn2():
    print(s1.get())
    print(s2.get())
    print(s3.get())
menu1_5=tk.Menu(menu1,tearoff=False)
menu1_5.add_checkbutton(label='加粗',variable=s1,command=fn2)
menu1_5.add_checkbutton(label='倾斜',variable=s2,command=fn2)
menu1_5.add_checkbutton(label='下划线',variable=s3,command=fn2)
menu1.add_cascade(label='字体',menu=menu1_5)


window.mainloop()
```

菜单点击事件

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
menubar=tk.Menu(window,tearoff=False)
for item in ['css','html','javasript','python']:
    menubar.add_command(label=item)

def click(e):
    menubar.post(e.x_root,e.y_root)   #定位  返回点击的位置
window.bind('<Button-1>',click)  #<Button-3>右击事件  <Button-1>左击事件   <Button-2>滚轮事件


window.mainloop()
```

### frame框标签

带边框的框标签   f1=tk.LabelFrame(window,text='边框')

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
#frame框标签，相当于div
f1=tk.Frame(window,width=200,height=200,bg='red')
f1.pack(side='left')   #pack相对定位，side指定上下左右，实现横排排列
# f2=tk.Frame(f1,width=100,height=100,bg='blue')  #框的嵌套
# f2.pack()
f2=tk.Frame(window,width=100,height=100,bg='blue')  #框的嵌套
f2.pack(side='right')

# l1=tk.Label(f1,text='this is l1')
# l1.pack()
window.mainloop()
```

### 布局

#### 相对布局pack：

组建的位置和大小会随着窗口的大小的改变而改变

pack(side='left/top/bottom/right/tk.TOP/tk.BOTTOM/tk.LEFT/tk.RIGHT')   对齐方式

pack(anchor='n')    n北/s南/w西/e东/c居中/nw/ne/sw/se   毛位置，当剩余空间远远大于所需空间

pack(fill=tk.X/tk.Y/X/Y)   填充，横向填充/纵向填充                          fill=BOTH两端填充（后面要跟expand=1）

pack(expand=0/1)  扩充、展开   0为不将剩余空间扩展   1为将剩余空间扩展

pack(padx=10，pady=10）(外间距)

pack(ipadx=10,ipady=10)(内间距)   

b2.pack_forget()   将b2隐藏，想再次出现，重写创建步骤

```py
# l1=tk.Label(window,bg='blue')
# l1.pack(fill='x')
# btn=tk.Button(l1,text='class')
# btn.pack(side='left',expand=1,fill='x')
# btn1=tk.Button(l1,text='class')
# btn1.pack(side='left',expand=1,fill='x')
```



#### 绝对布局place：

组建的位置和大小不会随着窗口的大小的改变而改变

```py
f1=tk.Frame(window,width=200,height=200,bg='red')
f1.place(x=100,y=100)#x/y   相对于父元素的x轴偏移量，y轴偏移量
                    #relx/rely=[0-1]  参照于父元素的x y
                    #width/height  指定容器的宽和高
                    #relwidth/relheight=[0-1]  参照于父元素的宽高（父元素的多少倍）
f2=tk.Frame(f1,bg='blue',width=100,height=100)
f2.place(relwidth=0.5,relheight=0.5)
f2.place_forget() #隐藏
```



#### 网格布局：

通过表格的形式进行布局

```py
btn1=tk.Button(window,width=6,height=6,text='click1')
btn2=tk.Button(window,width=6,height=6,text='click2')
btn3=tk.Button(window,width=6,height=6,text='click3')
btn4=tk.Button(window,width=6,height=6,text='click4')
btn1.grid(row=0,column=0,padx=10,pady=10)
btn2.grid(row=0,column=1,padx=10,pady=10)
btn3.grid(row=1,column=0,padx=10,pady=10)
btn4.grid(row=1,column=1,padx=10,pady=10,columnspan=2)   #横跨两列
#row/column  指定行列位置
#columnspan  横跨列数  rowspan  行跨行数
#sticky         组件在表格的对齐方式，九个方位，调整位置
```

#### 面向对象的方式实现计算器的排布

````py
import tkinter as tk 
class Mywindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.createmenu()
        self.createscreen()
        self.keys=[
            ['MC','MR','MS','M+','M-'],
            ['→','CE','c','±','√'],
            ['7','8','9','/','%'],
            ['4','5','6','*','1/x'],
            ['1','2','3','-','='],
            ['0','.','+'],

        ]
        self.createbtns()
    def createmenu(self):
        menubar=tk.Menu(self)
        self.configure(menu=menubar)
        menu1=tk.Menu(menubar,tearoff=False)
        menu1.add_command(label='标准型')
        menu1.add_command(label='科学型')
        menubar.add_cascade(label='查看',menu=menu1)
        menu2=tk.Menu(menubar,tearoff=False)
        menu2.add_command(label='复制')
        menu2.add_command(label='粘贴')
        menubar.add_cascade(label='编辑',menu=menu2)
    def createscreen(self):
        self.screen=tk.Label(self,text='screen',bg='#ccc',height=3,anchor='e',fg='#fff',font=('',20))
        self.screen.grid(row=0,column=0,columnspan=5)
    def createbtns(self):
        for arr in self.keys:
            for item in arr:
                if self.keys.index(arr)==4 and arr.index(item)==4:
                    tk.Button(self,text=item,width=10,height=11,font=('',10)).grid(row=self.keys.index(arr)+1,column=arr.index(item),rowspan=70)
                    continue
                if self.keys.index(arr)==5 and arr.index(item)==0:
                    tk.Button(self,text=item,width=22,height=5,font=('',10)).grid(row=self.keys.index(arr)+1,column=arr.index(item),columnspan=2)
                    continue
                if self.keys.index(arr)==5 and arr.index(item)==1:
                    tk.Button(self,text=item,width=10,height=5,font=('',10)).grid(row=self.keys.index(arr)+1,column=arr.index(item)+1)
                    continue
                if self.keys.index(arr)==5 and arr.index(item)==2:
                    tk.Button(self,text=item,width=10,height=5,font=('',10)).grid(row=self.keys.index(arr)+1,column=arr.index(item)+1)
                    continue
                tk.Button(self,text=item,width=10,height=5,font=('',10)).grid(row=self.keys.index(arr)+1,column=arr.index(item),pady=5,padx=5)

if __name__=="__main__":
    window=Mywindow()
    window.mainloop()
````

#### 面向对象的方式

```py
import tkinter as tk 
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
    def com1(self):
        tk.messagebox.showinfo(message='新建文件')

class Addmenu:
    def __init__(self,window):
        self.window=window
        self.menubar=tk.Menu(window)
        self.window.configure(menu=self.menubar)
        self.createfile()
    def createfile(self): 
        menu1=tk.Menu(self.menubar,tearoff=0)
        menu1.add_command(label='新建文件',command=self.window.com1)
        menu1.add_command(label='保存文件')
        self.menubar.add_cascade(label='文件',menu=menu1)

if __name__=="__main__":
    window=Application()
    Addmenu(window)
    window.mainloop()
```



#### 键盘事件及鼠标事件

```py
#事件
import tkinter as tk 
window=tk.Tk()
window.geometry('600x400')

#鼠标事件
#单击事件
# window.bind('<Button-1>',lambda x:print('左击'))  #第一个参数是事件名，第二个是函数
window.bind('<Button-2>',lambda x:print('中间滚轮'))
# window.bind('<Button-3>',lambda x:print('右击'))
#双击事件
# window.bind('<Double-Button-1>',lambda x:print('左击'))
# window.bind('<Double-Button-2>',lambda x:print('中间点击'))
# window.bind('<Double-Button-3>',lambda x:print('右击'))
# #三击事件
# window.bind('<Triple-Button-1>',lambda x:print('左击三击'))
# window.bind('<Triple-Button-2>',lambda x:print('中间点击'))
# window.bind('<Triple-Button-3>',lambda x:print('右击三击'))


#window.bind('<B1-Motion>',lambda x:print('左键移动'))  左键按下移动



# window.bind('<ButtonRelease-1>',lambda x:print('左键抬起'))


# window.bind('<Enter>',lambda x:print('鼠标移入'))
# window.bind('<Leave>',lambda x:print('鼠标移出'))


#滚轮事件
# window.bind('<Button-4>',lambda x:print('向上滚动'))
# window.bind('<Button-5>',lambda x:print('向下滚动'))


#键盘事件

e=tk.Entry(window)
e.pack()
# e.bind('<Key>',lambda x:print('键盘按下'))
# e.bind('<KeyRelease>',lambda x:print('键盘抬起'))


# e.bind('<Return>',lambda x:print('回车'))
# e.bind('<Up>',lambda x:print('上'))
# e.bind('<Down>',lambda x:print('下'))
# e.bind('<Right>',lambda x:print('左'))
# e.bind('<Left>',lambda x:print('右'))

# e.bind('<Shift_L>',lambda x:print('shift_l'))   左边shift
# e.bind('<Shift_R>',lambda x:print('shift_r'))   右边shift
# e.bind('<Control_L>',lambda x:print('control_r'))  左边ctrl
# e.bind('<Shift_R>',lambda x:print('shift_r'))
# e.bind('<Alt_L>',lambda x:print('Alt_r'))
e.bind('<A>',lambda x:print('A'))    大写A
e.bind('<a>',lambda x:print('a'))     小写a
# e.bind('<Shift-R>',lambda x:print('Shift+r'))   shift+R一起按下
e.bind('<Shift-R>',lambda e:print(e.widget))


#事件对象属性
# keykode  键盘码
# keysym   键盘符  
# char     字符
# widget   事件源
# x
# y
# x_root   返回点击的位置
# y_root   返回点击的位置

```

#### 跳出弹框事件

```py
import tkinter as tk 
from tkinter import messagebox
#弹框


window=tk.Tk()
window.geometry('600x400')



def fn():
    # tk.messagebox.showerror(title='error',message='代码出现错误')
    # tk.messagebox.showinfo(title='info',message='你选择的是科学型计算机')
    # tk.messagebox.showwarning(title='warning',message='这是一个警告')
    # b=tk.messagebox.askyesno(title='ask',message='确定关闭吗')
    # print(b)
    # c=tk.messagebox.askokcancel(title='ask',message='确定退出吗')
    # print(c)   返回布尔值
    # d=tk.messagebox.askquestion(title='ask',message='是否关闭')
    # print(d)  #返回yes和no
    # e=tk.messagebox.askretrycancel(title='ask',message='程序未响应，是否退出')
    #print(e)
    f=tk.messagebox.askyesnocancel(title='ask',message='是否退出')
    print(f)   #返回true false none

button=tk.Button(window,text='click',command=fn)

button.pack()

window.mainloop()
```

**关闭窗口：window.destroy()**

python基于模块：核心模块 、自定义模块、第三方模块





datetime    python处理时间的模块

.strftime("%Y-%m-%d %H:%M:%S")



### 生成器  特殊的迭代器（目的节省空间）

快速的生成一个迭代器

一。

aa=((i for i in range(100000)))  基本不占空间，数据是利用动态生成的

print(next(aa))         动态计算出来位置对应的数据

print(naxt(aa))

二。

```
def aa(n):
    a,b=0,1
    c=0
    while c<n:
        yield  b    #将函数返回的内容，装进生成器对象里面
        a,b=b,a+b
        c+=1
print(list(aa(10)))   将生成器对象转换成列表
```

#### 迭代对象  Iterable

字符串，列表，字典，集合

所有迭代对象都可以循环

#### 迭代器   生成迭代对象    Iterator 

```py
自己利用迭代器创建迭代对象
from collections import Iterable   #迭代对象
class aa:
    def __init__(self):
        self.datas=["a","b","c"]
        self.index=0
    def __iter__(self):   #规定的，不变的
        return self
    def __next__(self):    #下一步做的事情
        if self.index<len(self.datas):
            val=(self.datas[self.index])
            self.index+=1
            return val
        else:
            raise StopAsyncIteration
for item in aa():
    print(item)
```

#### 协成

利用yield,程序碰见yield会停止运行，当运行next后继续执行

```py
import time
def aa():
    while True:
        yield
        print("这是aa函数")
        time.sleep(1)
def bb():
    while True:
        yield
        print("这是bb函数")
        time.sleep(1)
aa=aa()
bb=bb()
while True:
    next(aa)
    next(bb)
```

#### 如何在python输出界面上设置样式

```
"\033(开头)+[显示方式(0,1..);+字体颜色;+背景色m+文本+\033[0m"    其中/033=Esc键，显示方式默认为0正常显示，1为高亮显示，前景色为30-37，背景色为40-47
例如：
print("\033[1;32;47m] * \033[0m",end="")

```
#### 如何将中文转换成十进制

name="月英俊"

name.encode("utf8")  首先转化成16进制

print(int.from_bytes(name.encode("utf8"),byteorder="big"))  转化成十进制