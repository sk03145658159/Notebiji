# 类和对象：

```py
class Play:
    name = "lj"   #类属性  静态变量   静态数据
    def __init__(self):  #初始化
        # self.name = "lk"   #实例属性
        pass
    def type(self):  #实例的方法
        print("司令")
    def ability(self):  #实例的方法
        print("指挥")

    @staticmethod
    def tell():
        print("这是tell方法")
    @staticmethod   #静态方法,属于类的方法，所以不能调用实例的属性和方法，但同时也不能调用类的属性和方法,也不能调用类的其他静态方法
    def say():
        print("这是say方法")

    @classmethod
    def say2(cls):
        print("这是say2方法")
    @classmethod    #类方法，不能调用实例的属性和方法,但是能调用类属性和方法,也能调用静态属性和方法

    def say1(cls):
        print("这是类方法")
        print(cls.name)
        cls.say2()
        cls.say()


p1 = Play()  # p1 实例
             # play 类
# p1.name = "lk"
# print("类属性：",Play.name)
# print("实例属性：",p1.name)
 
# Play.name = "小白"
# print("类属性：",Play.name)
# print("实例属性：",p1.name)
p2 = Play()


p1.say()
p2.say()

```

## 类方法.静态方法

> 两者都可以通过类或者实例来调用，特点都是不能够调用实例属性
>
> 类属性和方法是类固有的方法与属性，不会因为实例不同而改变。

## 类内建属性：

```py
# 类的方法：
class Car:
    def __init__(self):
        """
        这是一个汽车类
        """
        self.pp = "大众"
    def run(self):
        print("运行")


print(Car.__name__) #类名
print(Car.__doc__)  #对类的描述
print(Car.__bases__)#所有的父类，返回一个元组
print(Car.__base__) #父类
print(Car.__dict__) #以字典的形式返回所有的方法
print(Car.__module__) #返回类所在的模块 __main__
print(Car.__class__)  #类对应的类 <class type>


```

## 特殊实例的方法：(魔法方法)

```py
# 魔法方法：
#1._ _new _ _  “方法在Python中是真正的构造方法（创建并返回实例），通过这个方法可以产生一个”cls”对应的实例对象，所以说” _ _ new _ _”方法一定要有返回对于”2._ _ init _ _ “方法，是一个初始化的方法，“self”代表由类产生出来的实例对象，” _ _ init _ _”将对这个对象进行相应的初始化操作
class Car:
    def __new__(cls):  #“_ _ new_ _” 方法是在类实例化对象时第一个调用的方法，将返回实例对象，“_ _ new_ _” 方法始终都是类方法（即第一个参数为cls），即使没有被加上装饰器
        """
        创建实例
        """
        return object.__new__(cls) #__new__至少有一个参数cls，代表要实例化的类，此参数在实例化时python自动提供
        #__new__必须要有返回值，返回出实例化的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例
    def __init__(self):
        """
        初始化实例
        """
        self.pp = "大众"
    def run(self):
        print("运行")
        
    def __str__(self):
    		"""
    		作用：给实例一个描述
    		"""
    		return "这是一个汽车实例"
		def  __repr__(self):
				"""
    		作用：给实例一个描述
    		"""
    		return "这是一个汽车实例"
     def __del__(self):
     		"""
     		作用：实例被注销时调用
     		"""
     		print("实例被删除")
     	def __dir__(self)   以列表形式返回实例属性和方法

c = Car()
c.run()

```



## 封装：

> 对内部数据进行保护(隐藏)，或合理的暴露

```py
class Car:
	def __init__(self):
		self.__name = "大众"
	def getname(self):
		return self.__name
	def setname(self,var):
		self.__name = var
c = Car()
c.__name = "宝马"
```



## 继承和派生：

> 继承：目的是延续父元素的属性和方法     派生：在旧类的基础上添加新的功能 ，包括方法的重写。

> 基类  超类   父类             派生类  子类  

> 继承：直接或者间接继承object类，objects是一切类的基类（超类）父类  ，分为单继承和多继承。就近原则，深度优先  
>
> 派生： 在继承父类的基础上衍生出新的属性  

## 类内建函数：

- issubclass(sub,parent)   判断sub是否为parent的子类，返回bool

- isinstance(ins,class) 判断ins是否为class的实例，返回bool

- hasattr(obj,"attr")  判断obj中是否有attr属性，返回bool

- getattr(obj,"attr")  获取obj中attr属性

- setattr(obj,attr,value)  设置obj中attr属性

- delattr(obj,attr)  删除obj中attr属性

- dir() 列出类或实例的属性和方法，以列表的形式显示出来

- super()  寻找父类信息super(type[,object-or-type]),python3可以直接使用，python2 不可以

- super().xxx代替super(Class,self).xxx

- vars(object) 返回类或实例的属性，以字典的形式

  ```py
  class Myfloat(float):
      def __new__(cls,var):
          return float.__new__(cls,round(var,3))
      def __init__(self,num):
          self.num = num
      def get1(self):
          #return str(self.num)+"$"
          return "%0.2f%s/"%(self.num,type)
  num = Myfloat(4.5555)
  print(num.get1())
  ```


# 模式：

### 单例模式：实例只有一个

```py
class Person():
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self):
        pass
def say(self):
    print(self.name)
 
p = Person()
p.name = "小艾"
print(p.name)
```



### 工厂模式：

   ```py
class Dz():
    def __init__(self):
        self.type = "大众"
    def run(self):
        print("启动")
    def stop(self):
        print("熄火")

class Bmw():
    def __init__(self):
        self.type = "宝马"
    def run(self):
        print("启动")
    def stop(self):
        print("熄火")




class Carfactory():
    def CreateCar(self,type):
        if type == "dz":
            obj = Dz()
        elif type == "BMW":
            obj = Bmw()
        return obj

cf = Carfactory()
car = cf.CreateCar('dz')
print(car,type)
car.run()
car.stop()
   ```

# 异常：

> 程序出现了错误而在正常控制流以外采取的行为。
>
> 异常发生两个阶段：1.发生异常   2.异常处理

```py
try:#标志的作用，如果try里面的内容出错，则执行except里面的内容
	print((1/0))
except(ZeroDivisionError,ValueError):  #捕获多个异常
	prite("出错")
except ValueError： #分支
	prite("ValueError")
	
except ValueError as e: #获取异常信息
	prite(e)
	
else:  #没有捕获到异常时，执行的模块
	print("没有错误")
	
finally：
	print("不管有没有异常，都执行的代码")
	
	
def A():    #异常的传递
	print(1/0)
def B():
	A()
def C():
	B()
try:
	C()
except:
	print("error")
	
```

```py
异常类.md

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

#### 自定义一个异常类

```py
class error(Exception):   #建一个错误类，继承python中的异常类
    def __init__(self,msg):    #msg错误信息
        super(error,self).__init__()
        self.msg=msg
    def __str__(self):
        return self.msg
 def get(self,index):
    if index<0 or index>self.lenth()-1:
        raise error("超出范围")   #报自己定义的异常
```



### 总结：



1. except语句不是必须的，finally语句也不是必须的，但是二者必须要有一个，否则就没有try的意义。

2. Except语句可以有 多个，Python会按照except语句的顺序依次匹配你指定的异常，如果异常已经处理就不会进入后面的except语句。
3. Except语句可以以元组形式同时指定多个异常
4. Except语句后面如果不指定异常类型。 则默认捕获所有的异常，你可以通过logging或sys模块获取当前异常。
5. 如果要捕获异常后重复抛出请使用raise，后面不要带任何参数或信息
6. 不建议捕获并抛出同一个异常。

# 模块和包

## 模块：

> 模块就是一个py文件

## 包：

> 包就是一个文件夹，包含多个py文件，必须有\__init__py文件

## 引用方法：

### 构建模块的层级包：

> 模块和包是任何大型数据的核心，就连python安装程序本身也是一个包。

```py
import a,b
import bao1.a,bao1.b
from bao1 import a
from bao1 import a as a2  #相当于给a起了新的名字
from bao1.a import aa3,aa2
from bao1.a import * #一次性导入
__all__=['aa2','aa3']   
from .a import aa3  #使用相对路径导入子模块,一个点是在当前目录，两个点是退出当前目录，相对路径只能在子模块中使用。
```

### 控制模块全部导出：

> from moudle import *  从mouble模块中全部导出内容。在模块中定义变量\__all__,可以有效的控制被全部导入



### 使用相对路径导入包中子模块:

将代码组织成包，想用import语句从另一个包名没有编码过的包中导入子模块。使用包的相对导入，使一个模块导入同一个包的另一个模块。

```py
mypackage/
	__init__py
	A/
		__init__.py
		spam.py
		grok.py
	B/
		__init__.py
		br.py
```

- 如果要导入同目录下的模块grok，语句如下：

  ```py
  from .  import grok
  ```

- 如果要导入不同目录下的模块B bar,语句如下：

  ```py
  from ..B  import bar
  ```

### 将模块分为多个文件：

> 在包(package)中的\__init__模块中利用from .a import  A的方式将其他模块导入到\__init__这个模块中，这时它所在的包可以被认作一个模块，然后在主模块中利用from mypackage.con1.myclass import *导入使用。

分为三步：

1. mymodule目录来替换文件mymodule.py,这个目录下，创建以下文件：

   ```py
   mymodule/
   	__init__.py
   	a,py
   	b,py
   ```

2. 分别在a.py和b.py文件中插入一下代码：

   ```py
   # a.py
   class A:
   	def spam(self):
   		print("A.spam)
   # b.py
   class B:
   	def spam(self):
   		print("B.spam)
   ```

3. 最后在\__init__.py中，将两个文件粘合在一起：

   ```py
   from .a import A
   from .b import B
   ```


### 利用命名空间导入分散的代码：

> 这种工作机制被称为包命名空间，从本质上讲，包命名空间是一种特殊的封装设计，为合并不同的目录的代码到一个共同的命名空间.它是将两个不同的包目录合并在一起，可以导入spam.xbd和spam.xmd,并且他们能够工作。

```py
import sys
sys.path.extend([r"C:\Users\牛培楠\Desktop\python\xb",r"C:\Users\牛培楠\Desktop\python\xm"])
from spam import xbd,xmd
xbd.a()
xmd.a()

# 在目录里，有着共同的命名空间，在任何一个目录里面都没有__init__py文件。
import sys
print(sys.path)
可以在python 环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后自己添加的路径就会自动消失！
```

### 重新加载模块：

> 重新加载先前加载,但修改了其源码的模块

```py
import spam
import imp
imp.reload(spam)  
```

### 运行目录或压缩文件：

> 如果应用程序有多个文件，可以把应用程序放进他自己的目录并添加一个\__main__.py文件。比如以下例子：

```py
myspplication/
	spam.py
	bar.py
	grok.py
	__main__.py
```

如果\__main__.py存在，可以简单的在顶级目录运行python解释器。

python.myapplication

解释器将执行\__main__.py文件作为主程序。

将代码打包成zip文件，这种技术同样适用。

### 读取位于包中的数据文件：

```py
mypackage/
	__init__.py
	somedate.dat
	spam.py
```



> 1.假设spam.py文件需要读取somedate.dat文件中的内容，可以用data = pkgutil.get_data(\__packge__,"mydate.dat")实现。     #字节
>
> 2.f = open("mypackage/mydate.dat","r")   con = f.read()   f.close()

### 通过字符串名导入模块：

> 如果想要导入一个模块，但是模块的名字在字符串里，逆像对字符串调用导入命令。使用importlib.import_mouble()函数来手动导入名字为字符串的一个模块或者包的一个模块。

> import_moudle知识简单的执行个import相同的步骤，但是返回生成的模块对象，你只需将其存储在一个变量，然后像正常的模块一样使用。如果你正在使用的包，import_moudle()也可用于相对导入，但是，你需要给他一个额外的参数。

```py
import importlib   #通过字符串创建模块
data = importlib.import_mouble("mydate.dat")
u = mod.urlopen("http://www.python.org")
print(aa,data)
```

# GUI：

> 客户端服务器构架，简称c/s结构。

```py
import tkinter as tk
window = tk.Tk()  #创建窗口
window.title('棒棒的窗口') #设置窗口的title
window.geometry('800x400')  #设置窗口尺寸  中间为x,不是乘法
# window.resizable(0,0)  #重置尺寸的大小

# Label 标签   tk.Label 传统标签
# v1 = tk.StringVar()
# v1.set("hello world")
# img1 = tk.PhotoImage(file="mi2.png")
# l1 = tk.Label(window,image=img1,textvariable=v1) #两种方式  实例化 Label 第一个参数是主窗口
# l1['text'] = "hello world"  #文本
# l1['font'] = ("",20,"bold italic") #字体 元组(字体样式,大小,"倾斜或加粗")
# l1['bg'] = "#ff6700"  #背景色
# l1['fg'] = "#000"  #前景色，定义字的颜色
# l1['width'] = 200
# l1['height'] = 100
# l1['anchor'] =  "ne"    #文本位置  n北   s南  e东  w西  ne  nw  se  sw  c
# l1['value'] = ""
# l1['variable'] = ""
# l1['image'] = img1



# Button的使用 按钮
# num = 0
# def aa():
#     global num
#     l1['text'] = str(num)
#     num+=1
# b1 = tk.Button(window,text="点击",width=20,height=1,bg="#333",fg="#fff",command=aa)


# 输入组件
# e = tk.Entry(window)
# e['selectbackground'] = "red"  #选中文字，的背景色
# e['selectforeground'] = "blue" #选中文字，的颜色
# e['show'] = ""   #默认不指定，指定对应的字符


#button
# def fn1():
#     val = e.get()
#     t.insert('insert',val)  #从任意位置插入

# b1 = tk.Button(window,text="insert",command=fn1)
# def fn():
#     val = e.get()
#     t.insert('end',val)      #从最后插入
 
# b2 = tk.Button(window,text="after",command=fn)

#文本域组件
# t = tk.Text(window)




# e.pack()
# t.pack()
# b1.pack()
# b2.pack()
# l1.pack()  #主件加载到窗口上
# b1.pack()

# l2 = tk.Label(window,text="",width=20,height=3,bg="#ff6700",fg="#ccc",font=("",20))


# v2 = tk.Variable()
# v2.set("默认值")

# def fn():
#     con = v2.get()
#     l2['text'] = "你选择了%s"%con
# r1 = tk.Radiobutton(window,text="A",variable=v2,value="A")
# r2 = tk.Radiobutton(window,text="B",variable=v2,value="B")
# r3 = tk.Radiobutton(window,text="C",variable=v2,value="C")


# l2.pack()
# r1.pack()
# r2.pack()
# r3.pack()

# v3 = tk.StringVar()
# v3.set("")
# def fn1():
#     print("验证")
#     con = v3.get()
#     if len(con)>10:
#         return True
#     else:
#         return False
# def fn2():
#     print("长度不足")
# e = tk.Entry(window,textvariable = v3,validate="focusout",validatecommand=fn1,invalidcommand=fn2)  #entry是输入框
#validate   focus  focusin  focusout  key
# e.pack()
# e1 = tk.Entry(window)
# e1.pack()


# v4 = tk.StringVar()
# v4.set("")
# def fn4():
#     con = v4.get()
#     if con == "张三":
#         print("输入正确")
#     else:
#         print("输入错误")
# z = tk.Entry(window,textvariable = v4,validate = "focusout",validatecommand=fn4)
# z.pack()
# v5 = tk.StringVar()
# v5.set("")
# def fn6():
#     con = v4.get()
#     if con == 111111:
#         print("输入正确")
#     else:
#         print("输入错误")
# m = tk.Entry(window,textvariable = v5,validate = "focusout",validatecommand=fn6)
# m.pack()

tk.Label(window,text="用户名:").place(x=40,y=40)
username,password,yanzheng= False,False,False
def isOk():
    u = en1.get()
    p = en2.get()
    y = en3.get()
    if u=="123456789" and p=="1234567879" and y=="123456":
        tk.Label(window,text="成功登录").place(x=100,y=160)
    else:
        tk.Label(window,text="登录失败").place(x=100,y=160)
        btn1['state'] = "disable"
def islogin(u,p,y):
    if len(u)>=10 and len(p)>=10 and len(y)>=6:
        btn1['state'] = "normal"
    else:
        btn1['state'] = "disable"

def fn1():
    global username
    if len(en1.get())>=10:
        l2['text'] = "成功"
        l2['foreground'] = "green"
        username = True 
        islogin(username,password,yanzheng)
        return True
    else:
        return False
def fn2():
    global username
    username = False
    l2['text'] = "长度不足十位"
    l2['foreground'] = "yellow"
en1 = tk.Entry(window,validate="focusout",validatecommand=fn1,invalidcommand=fn2)
en1.place(x=100,y=40)
l2 = tk.Label(window,background="white")
l2.place(x=280,y=40)

tk.Label(window,text="密码:").place(x=40,y=80)
def fn3():
    global password
    if len(en2.get())>=10:
        l4['text'] = "成功"
        l4['foreground'] = "green"
        password = True 
        islogin(username,password,yanzheng)
        return True
    else:
        return False
def fn4():
    global password
    password = False
    l4['text'] = "长度不足十位"
    l4['foreground'] = "yellow"
en2 = tk.Entry(window,validate="focusout",validatecommand=fn3,invalidcommand=fn4)
en2.place(x=100,y=80)
l4 = tk.Label(window,background="white")
l4.place(x=280,y=80)


tk.Label(window,text="验证码:").place(x=40,y=120)
def fn5():
    global yanzheng
    if len(en3.get())>=6:
        l6['text'] = "成功"
        l6['foreground'] = "green"
        yanzheng = True 
        islogin(username,password,yanzheng)
        return True
    else:
        return False
def fn6():
    global yanzheng
    yanzheng = False
    l6['text'] = "长度不足十位"
    l6['foreground'] = "yellow"
en3 = tk.Entry(window,validate="focusout",validatecommand=fn5,invalidcommand=fn6)
en3.place(x=100,y=120)
l6 = tk.Label(window,background="white")
l6.place(x=280,y=120)


btn1 = tk.Button(window,text="登录",command=isOk)
btn1.place(x=100,y=160)
# btn1['state'] = "normal"
btn1['activebackground'] = "red"
btn1['activeforeground'] = "#fff"


btn2 = tk.Button(window,text="注册")
btn2.place(x=200,y=160)
btn2['state'] = "normal"  #normal or disable
btn2['activebackground'] = "red"
btn2['activeforeground'] = "#fff"


window.mainloop() #进行事件循环





import tkinter as tk
window = tk.Tk()  #创建窗口
window.title('棒棒的窗口') #设置窗口的title
window.geometry('800x400')  #设置窗口尺寸  中间为x,不是乘法
# window.resizable(0,0)  #重置尺寸的大小
v1 = tk.Variable()
v2 = tk.Variable()
v1.set(0)
v2.set(0)
def fn():
    con1 = int(v1.get())
    con2 = int(v2.get())
    if con1==1 and con2==0:
        l['text'] = "我喜欢看电影"
    elif con1==0 and con2==1:
        l['text'] = "我喜欢敲代码"
    elif con1==1 and con2==1:
        l.config(text="都喜欢")
    else:
        l.config(text="都不喜欢")
l = tk.Label(window,width=60,height=5,bg="#333",fg="#fff",font=("",23))
l.pack()
c1 = tk.Checkbutton(window,text="看电影",variable=v1,command=fn)
c1.pack()
c2 = tk.Checkbutton(window,text="敲代码",variable=v2,command=fn)
c2.pack()

window.mainloop() #进行事件循环




import tkinter as tk
window = tk.Tk()  #创建窗口
window.title('棒棒的窗口') #设置窗口的title
window.geometry('800x400')  #设置窗口尺寸  中间为x,不是乘法
# window.resizable(0,0)  #重置尺寸的大小


# listbox
l = tk.Label(window,width=10,height=1,bg="#333",fg="#fff")
l.pack()

en = tk.Entry(window)
en.pack()

def fn1():
    arr = lx1.curselection()  #返回选中数据的下标，是一个元组
    con = en.get()
    if len(con)==0:
        return
    elif len(arr)==0: 
        lx1.insert('end',con)
    elif len(arr)==1:
        lx1.insert(arr[0]+1,con)
    else:
        num = 1
        for i in arr:
            lx1.insert(i+num,con)
            num+=i

b1 = tk.Button(window,text="插入",command=fn1)
b1.pack()


lx1 = tk.Listbox(window,selectmode="extended")
lx1.insert(0,"上海")


for item in ['北京','广州','深圳']:
    lx1.insert('end',item)


lx1.pack()

def fn():
    print(lx1.curselection())

b = tk.Button(window,text="点击",command=fn)

window.mainloop() #进行事件循环
```

