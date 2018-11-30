# Typora markdown

# JS  javascript   阮一峰的es6  javascript标准参考教程

**特征：单线程异步机制的语言** 

**目的：利用极少的资源，做更多的事情，单线程模拟多线程**

单线程：程序同一时间只能执行同一件事件

异步：把需要耗费时间以及不确定的时间的代码，放到异步执行

（从上到下执行，线程先执行正常线程的代码，遇到异步的代码将其一次放到后面的数组中，等正常线程代码执行完后线程再执行异步的代码）

## 组成：

	1.ECMAscript 基础语法：变量  数据类型  运算符  数组 函数  对象
	2.BOM 浏览器对象模型
		window对象  history对象 location对象
	3.DOM 文档对象模型
		元素获取 操作属性 操作央视样式  节点 事件  事件对象
## 作用：

	1.数据验证
	2.动态的创建和删除元素
	3.操作元素的内容和样式
	4.模拟动画
	5.创建cookie
	6.ajax
	7.json格式的数据处理
## 特征：

	客户端脚本语言，实现用户交互。
	  基于对象和事件驱动的松散型解释型语言
@import url('base.css');    一个css引用到另一个css中

## js的引入方式(相互关联)

- 外部引入方式 

  ```
  <script src=""></script>
  ```

- 嵌入式

  ~~~css
  在html页面中（底部）用script标签对引入js
  ~~~

- 事件后

  ~~~css
  <div onclick="alert(1)(js代码)"></div>
  ~~~

- **注意：**

  - [ ] js的几种引入方式是相互关联的，可以相互操作与访问
  - [ ] 外部js中不能添加script标签对
  - [ ] 嵌入式js中不能添加src属性

## js输出工具

- 弹出框（会阻止程序的运行）

  ~~~css
  alert(1);  alert("a")  alert("中国"）
  ~~~

- 输出到控制台

  ~~~css
  console.log(内容);
  console.dir(详细内容)；
  ~~~

- 输出到页面中（可识别标签对）

  ~~~css
  document.write("a"); document.write("<i>倾斜</i>")

  ~~~

## 注释

- 单行注释  ctrl+/
- 块级注释  ctrl+shift+/     取消：ctrl+/

## 变量：一个容器，存放数据

- 定义变量  var num=10；   无论定义什么类型变量都用var ，变量类型取决于所赋的值

- 命名规范：（数字、字母、下划线_、$）

  - [ ] 不能以数字开头
  - [ ] 区分大小写
  - [ ] 不能以关键字命名（js中已经用到的）
  - [ ] 不能以保留字命名（js中将来会用到的）
  - [ ] 尽量有意义
  - [ ] 首字母大写  Array
  - [ ] 驼峰命名法  getElementByld

- 赋值：

  var  num=Math.random()  产生一个0-1的随机数。 例：产生30~60的随机数 let num=Math.random*30+30

  ​                  Math.floor()向下取整

  ​		  Math.ceil()向上取整

  ​		 Math.pow(x,y)  x的y次幂

  ```
  var rgb1=Math.floor(Math.random()*256)  取0-255之间向下取整得随机数
  ```

  - [ ] 先声明，后赋值

        ~~~css
        var num;num=10;
        ~~~

  - [ ] 声明的同时赋值

        ~~~css
        var num=10；
        ~~~

  - [ ] 一次性声明多个变量，再赋值

        ~~~css
        var a,b,c; a=1;b=2;c=3;
        ~~~

  - [ ] 一次性声明多个变量并赋值

        ~~~css
        var a=1,b=2,c=3;
        ~~~

- 注意事项：

  - [ ] 变量要先声明后访问，变量的默认值为undefined
  - [ ] 新值覆盖旧值
  - [ ] 变量可以重复声明
  - [ ] 不用var关键字声明变量，但赋值，不会报错，此变量为全局变量
  - [ ] 不用var关键字声明，且不赋值，会报错
  - [ ] 先访问后声明变量是，值为undefined，由于预解析（解析var、function关键字）

## 数据类型

- 根据数据在内存中的存储位置划分。基本数据类型存放在栈中，引用数据类型存放在堆中（指针存放在堆中，内容存放在堆中）

- 数据类型分为基本型和引用型，因为数据类型的不同导致存储位置的不同（基本型[简单型数据]存储在栈中，引用型[数组、对象等复杂型数据]存储在堆中[头指针地址数据存储在栈中]）。所以赋值分为浅拷贝（传址）和深拷贝（传值）。深拷贝需要拷贝到每一项。

  ```py
  var zhangsan={name:'zhangsan',son:{name:'xiaozhangsan',son:{name:'xiaoxiaozhangsan'}}}
      function extend(obj){
          var newobj={}
          for(var i in obj){
              if(typeof(obj[i])=='object'){
                 newobj[i]=extend(obj[i])
              }else{
                 newobj[i]=obj[i]
              }
          }
          return newobj
      }
      var lisi=extend(zhangsan)
      lisi.son.name='xiaolisi'
      console.log(lisi.son.name)
      console.log(zhangsan.son.name)
  ```

  ​

  ### 基本数据类型

  - undefined    声明未定义
  - null           空
  - string    字符编码 :Ascall\utf-8\gb2312\unicode万国码。转义字符：\',\",\n,\r,\f,\t，\\。    
  - boolean
  - number   
    - [ ] 八进制：以0o开头，0-7
    - [ ] 十六进制：以0x开头，0-9  a-f
    - [ ] NaN:not a number  本来期望返回数值的操作但并未返回数值的情况。
    - [ ] 二进制：以0b开头

  ### 引用数据类型

  - object(属性与方法的集合)数组、函数、对象

  ### typeof

  用来判断变量的数据类型的。结果是字符串   （typeof 变量名）

  | 数据类型       | 值                         | 情况   | typeof的结果 |
  | ---------- | ------------------------- | ---- | --------- |
  | undefined  | undefined                 |      | undefined |
  | null       | null，空（占位符）               |      | object    |
  | boolean布尔型 | true和false                |      | boolean   |
  | string字符串型 | 带有引号的（单双引号均可）             |      | string    |
  | number数值型  | 整数、小数、负数、八进制、十进制、十六进制、特殊值 |      | number    |
  | object     |                           |      |           |

  ### 运算符：

  ~~~hrml
  表达式：能够求值的语句
  ~~~

  - 算术运算符:

    ~~~html
    + - * / % ++var var++ --var var--
    +:操作数都是数值型进行四则运算
      操作数中包含字符串，进行拼接。
    ++var：++在前，先算++，再执行本行中的其他语句
    var++：++在后，先执行本行中的其他语句，在执行++
    ~~~

  - 关系运算符

    返回值为布尔值 ture false

    ~~~css
    >   <   >=  <=  ==  ===  !=  !== 
    ~~~

    - [ ] 如果两个操作数都是字符串（数字型字符串），按照ASCLL码表进行比较大小。
    - [ ] 如果两个操作数都是数字，直接比较大小。
    - [ ] 如果操作数一个是字符串，另一个为数字，先尝试将字符串转换为数字，如果转换成功，按照数字进行比较大小，若转换不成功，返回false。
    - [ ] 1==true，0==false
    - [ ] ==：值相同
    - [ ] ===：值相同，数据类型也相同。
    - [ ] undefined==null

  - 赋值运算符

    ~~~css
    =  +=   -=   *=  /=   %=
    ~~~

    ~~~js
    var num=5;
    num+=10; //num=num+10;
    ~~~

    ### 逻辑运算符

    ​	测量值与变量之间的逻辑关系。

    ​		为假false的值：0、false、undefined、null、NaN、""

    - &&与

    - ||或

    - !取反

      #### 逻辑运算符真值表

      | A     | B     | A&&B  | A\|\|B | !A    |
      | ----- | ----- | ----- | ------ | ----- |
      | true  | true  | true  | ture   | false |
      | true  | false | false | ture   | false |
      | false | ture  | false | ture   | true  |
      | fales | false | false | false  | true  |

      #### 返回值：

      - #### &&  

        ​	同真为真，返回第一个假值（都为真时返回最后一个返回值）

      -  ||

        ​	同假为假，返回第一个真值（都为假时返回最后一个返回值

      -  ！

        ​	取反，返回值只有true和false


三元运算符

​         	表达式？语句1：语句2；

​                  如果表达式的结果为真时，执行语句1，为假时执行语句2.

弹出消息框	

​	confirm("提示内容")；


  ### 流程控制：

> 代码按照指定条件的执行顺序
>
> #### 	顺序结构：
>
> ​		语句按照从上到下的顺序进行
>
> #### 	分支结构：
>
> ​		当条件成立时执行响应的语句。
>
> #### 	   if:
>
> ##### 		单分支结构
>
> ​			if（条件）{ 
>
> ​				条件成立时，执行的语句
>
> ​			}
>
> ##### 		双分支结构
>
> ​			if(条件){
>
> ​				条件成立时，执行的语句
>
> ​			}
>
> ​			else{
>
> ​				条件不成立时，执行的语句
>
> ​			}
>
> ##### 		多分支结构
>
> ​			if（条件1）{
>
> ​				条件1成立时，执行的语句

​				}

​			   else if（条件2）{

​					条件1不成立，条件2成立，执行的语句

​				}

​		          else{

​					以上条件都不成立时，执行的语句

​				}

##### 		    嵌套分支

​				if（条件1）{

​					条件1成立时，执行语句

​				}

​				else{

​					if（条件2）{}

​					else{}

​				}

#### 		switch:

​				switch(表达式){

​					case 值1：语句1；break;     

​					case 值2:  语句2；break；

​					...

​					...

​					default:语句；			

​				}

​			case的值与表达式的值相匹配来选择执行语句

### 循环结构 ：当满足条件时，重复不断的执行一段代码

#### for循环：

~~~js
for(初始条件；终止条件；步进值){
  循环体；
}
    执行顺序：
    1.初始条件
    2.终止条件
    3.循环体
    4.步进值
    5.重复以上2、3、4步骤直到不满足终止条件，跳出循环。
~~~

#### while循环

~~~js
while(终止条件)｛
	当满足条件时执行的语句;
｝
~~~

#### do while循环

~~~js
do{
  循环体；
}while(循环终止条件)
~~~

#### 终止循环的语句

#### continue  终止本次循环，如果后面的语句仍满足条件，继续执行。

#### break   终止整个循环

### 输入工具  输入框

~~~html
prompt(提示文本，【默认值】)；
var num=prompt(提示文本，【默认值】)；  定义一个变量接受输入值
~~~

<table border="" bgcolor="" width="" height="" cellspacing="0"单元格与单元格之间的距离 cellpadding=""内容到边框的距离>

模版字符串：字符串拼接:    `字符串+${变量}+字符串`

​      	`字符串+${变量}+字符串`

## 数组

- 按照顺序排列的一组相关数据。

- 特点：每一个数组元素均有特定的键名（下标）。

- 初始化数组元素：

  - [ ] 先声明，后赋值    `var arr=[];arr[0]='a' ,arr[1]='b'；`
  - [ ] 声明的同时赋值   `var arr=[1,2,3,4];`

- 数组的下标：

  访问数组元素

- 数组的长度：

  `arr.length  访问数组`长度

  arr.length=0 ;      清空数组

- 遍历数组元素：访问数组中的每一个元素

  - [ ] for

        ~~~js
        for(var i=0;i<arr.length;i++){
          arr[i];
        }
        ~~~

        ​

  - [ ] 用for in

        ~~~js
        for(var i in arr){
          i;  arr的下标
          arr[i];   arr元素
        }
        var arr=[90,,89,67,56,,,89];
           var arr1=[];
           for(var i in arr){
               if(arr[i]!=undefined){
                   arr1[arr1.length]=arr[i];
               }
           }
           console.log(arr1);
        ~~~

        ​

- 注意事项：

  - [ ] 数组元素默认值为undefined
  - [ ] 数组长度是可变的
  - [ ] 数组元素可以是任意数据类型

-    数组对象.push()方法：向数组的后面插入一个元素。

     ~~~js
      var arr=[90,,89,67,56,,,89];
        var arr1=[];
        for(var i in arr){
            if(arr[i]!=undefined){
                arr1.push(arr[i]);
            }
        }
        console.log(arr1);
     ~~~

### 二维数组

- 访问:`arr[i][j]`

- 遍历

  ~~~js
  for(var i=0;i<arr.length;i++){
    for(var j=0;j<arr[i].length;j++){
      arr[i][j];
    }
  }
  ~~~

### 数组的方法：

- forEach

  ```js
  数组的遍历：
      数组名.forEach(function(value,index)){

     }
  第一个参数（value）为数组的各个数据
  第二个参数（index）为数组的下标
  参数名随意取
  例：function join(arr,...rest) {
        rest.forEach(function (value) {
            arr[arr.length]=value;

        })
        return arr;
    }
    var arr=[1,2,3,4];
     console.log(join(arr, 5, 6, 7));
  ```

  ​

## 函数：

实现某一特定功能的代码块封装起来并且能够重复调用。

### 定义函数

~~~js
function functionName函数名([形参1]，[形参2],..){
  函数体；
  [return 返回值;]
}      return终止函数
~~~

- 字面量，自变量

  ```js
  var varible变量=function(){
    函数体
  }；
  varible();  函数的引用
  ```

- var varible=new function("a","b","alert(a+b)");

- 对象的方式

  用自变量声明的函数必须先声明后调用，用关键字function声明的函数，调用可以在声明前也可以在声明后，由于预解析。

### 函数调用：

- 函数名+()      functionName()

- 自变量+()

- 箭头函数： let aa=(形参)=>{函数体}

  ​		    引用：aa(实参);

  ​		箭头函数中没有this，内部的this指向上下文

  ```js
  let asd=[1,4,2,4,7,3,9,1,6];
      asd.sort((x,y)=>x-y);
      console.log(asd);
      asd.sort((x,y)=>y-x);
      console.log(asd);
      let aq=asd.find(item=>item>2);
      console.log(aq);
  ```

  ​

- 自调用 ：   (function (){

  ​			})()

#### 递归函数：

1.当函数要自己调用自己时

2.一定要设置一个出口，不然成为死循环

```js
function fn(num) {
        if(num==1){
            return num;
        }
        else{
            return num*fn(num-1);
        }
    }

    console.log(fn(10));
```



#### 回调函数：

​	把一个函数的指针（函数名）作为参数传递给另一个函数，当指针调用函数时，这个函数叫做回调函数。   

```js
function isExist(arr,fn) {
       for(var i=0;i<arr.length;i++){
           if(fn(arr[i])){
               return true;
           }
       }
       return false;
   }
   function isOdd(num) {
       var a=num%2==0?true:false;
       return a;
   }
   function isEven(num) {
       var a=num%2==1?true:false;
       return a;
   }

   console.log(isExist([1,3,5,7],isEven));
```

### 闭包函数

```js
function fn1() {
       let a="123";
       function fn2() {
           console.log(a);
       }
       return fn2();
   }
   let fn2=fn1();
    console.log(fn2);
```



##### 参数：

动态改变函数体的变量，使函数更加灵活。

- 形参：

  定义函数时，写在括号中的变量，作用为接收实参。

- 实参：

  函数调用时写在括号中的值，作用时给形参传值。


#### 参数默认值

- 分支结构
- 三元运算符
- 逻辑或
- es6给形参赋值，当形参的值为undefined时。

### 参数的传递：

- 参数可以是任意的数据类型
- 参数是按照顺序传递的
- 形参=实参     一一对应传递
- 形参>实参     多余的形参赋值为undefined
- 形参<实参       实参由arguments对象来接收。
  - [ ] arguments对象：

        ```js
          function sum(arr) {
                for(let i=1;i<arguments.length;i++){
                    console.log(arguments[i]);
                }

            }
            sum([1,2],3,4,5)
        ```

        ​

        - 用来接受参数的详细信息
        - 每声明一个函数，在其函数内部会自动声成arguments对象。arguments对象只在函数内部起作用。
        - arguments[i]    arguments.length     遍历   类似数组但不是数组

  - [ ] 剩余参数：
        - 声明：`...rest`

          ```js
          function syy(arr,...rest) {
                  for(var i=0;i<rest.length;i++){
                      console.log(rest[i]);
                  }

              }
              let arr=[1,2,3];
          ```

          ​

        - rest参数与arguments对象的区别：
          - [ ] rest接受多余的参数，arguments接收全部的参数
          - [ ] rest是数组，能够使用数组的方法；arguments对象类似数组，不能使用数组的方法。

### 返回值：return

- 返回值可以是任意的数据类型
- return终止函数     return后面的语句不再执行
- 一个函数内部可以有多条return分支语句，最终只执行一条return语句。
- 一个函数如果没有返回值，返回undefined。

### 作用域：变量起作用的范围

- 全局作用域
  - [ ] 在整个js代码中都能访问的变量，凡是修改，变量的值均会改变
        1. 在函数外部用var声明的变量，拥有全局作用域。
        2. 不用var声明，但赋值的变量，拥有全局作用域。
- 局部作用域    （局部作用域的优先级大于全局作用域）
  - [ ] 在函数内部
        1. 形参是局部变量，拥有局部作用域。
        2. 在函数内部用var关键字声明的变量，拥有局部作用域
- 块级作用域  ：{}内部的域。

#### let:

- 声明变量，用法和var一样。
- 可以识别块级作用域，var不能
- 不能重复声明变量
- 不存自变量提升（先访问后声明）

### const:

- 声明常量，一旦声明不能被改变
- 声明常量的同时要赋值，否则会报错
- 可以识别块级作用域
- 不能重复声明
- 不存在变量提升

### 内置顶层函数：

- 内置：ECMAscript自带的函数，只知道如何使用，不用关心如何封装。
- 顶层：在代码中任意位置均能使用。
- escape()      将输入的字符串进行编码
- unescape()    将编码的字符串进行解码
- Bollean()     将其余数据类型转换为布尔型
- String()       将任意数据类型转换为字符串型
- Number()    将其余数据类型转换为数值型
  - [ ] null->0      “”->0      "   "->0
  - [ ] false->0  true->1
  - [ ] undefined->NAN
  - [ ] 进制数转换为十进制
  - [ ] 去掉没有意义的后导0
  - [ ] 字符串：规范的浮点数，数值型字符串
- parselnt()     将字符串转换为整数
  - [ ] 开始的字母需是数字、+、—、空格 。    转换不成功，转换为NAN
- parseFloat 将字符串转换为浮点型。
  - [ ] 仅能转换规范的浮点数。转换不成功，返回NAN
- isNaN() 判断值是否能够转换为数值型，能转换返回false，不能则返回true。

### 数据类型转换

- 强制类型转换
- 隐式数据类型转换 ：算数运算符、逻辑运算符、条件if() while()

### github

- 克隆 ：git clone  网址
- 打开文件夹：cd 文件名
- 添加：git  add  *
- 查看状态：git  status
- 标记：git commit -m"标记"
- 提交：git push     
- 用户名、密码
- 查看网址：
  - [ ] setting->github pages->master branch/save->刷新

   如何删除项目：setting->delete this repository->项目名

​    如何二次提交：拉取:git  pull->输入提交顺序语句.....

##    对象：

- 概念：

  - [ ] 类：一群具有相同特征的对象集合的描述
  - [ ] 对象：具体存在的对象个体
  - [ ] 属性：对象基础信息的描述
  - [ ] 方法：对象功能的描述

- 定义对象

  - [ ] 构造函数（类），实例化对象

        ```js
        function Computer(color,size){
          this.color=color;
          this.size=size;
          this.play=funcyion{
            console.log("上网");
          }
        }
        //实例化对象
        let ASUS=new Computer();
        //this默认指向window,实例化对象后指向ASUS。
        用call,reply,blind改变指针
        ```

        ​

  - [ ] JSON

        ```js
        直接定义对象
        let ASUS={
          属性名：属性值,
          属性名：属性值;
          方法明：function(){
          
        	}
        }
        ```

        ​

  - [ ] class定义类，实例化对象

- 属性

  对象.属性名=属性值；

- 方法：

  对象.方法明=函数

  方法一般放在原型(prototype)中

- 属性的增删改查

  - [ ] 增加：对象.属性名=属性值；
  - [ ] 删除：delete 对象.属性名
  - [ ] 修改：对象.属性名=属性值
  - [ ] 访问：对象.属性名/对象[’属性名‘]/对象.方法

- 遍历：

  ```js
  for(let i in apple){
    i;//属性名
    apple[i];//属性值
  }
  ```

- 对象的属性：

  - [ ] constructor:     对象名.constructor

        返回该对象的构造函数

  - [ ] instanceof:

        `对象 instanceof 构造函数`判断函数是否为对象的构造函数，是返回true,不是返回false。


#### 窗口响应式事件（随着屏幕大小的改变所发生的事件，可用于pc端和移动端的切换）

- js：windo.onresize=function(){

  ​	var client=document.documentElement.clientWidth

  }

- css3中的  @media screen and (min-width:1000px){}   屏幕像素大于等于1000时

  ```py
   @media screen and (min-width:1000px){
     div{
       width:
       hei:
       ...
     }
   }
   例子
   .bigbox{
          width: 300px;
          height: 600px;
          overflow: hidden;
          margin: 0 auto;
      }
      .list{
          width:300px;
          height: 600px;
          float: right;
      }
      .list li{
          width:300px;
          height: 200px;
          border: 1px solid #ccc;
          box-sizing: border-box;
      }
      .aa2{
          width:300px;
          height: 300px;
          background-color:bisque;
          float: right;
          border:1px solid salmon;
          box-sizing: border-box;
      }
      .aa3{
          width:300px;
          height: 300px;
          background-color:bisque;
          float: right;
          border:1px solid salmon;
          box-sizing: border-box;
      }
      .aa1{
          width:600px;
          height: 300px;
          background-color: aqua;
          float: right;
          border:1px solid yellow;
          box-sizing: border-box;
      }
      .aa4{
          width:600px;
          height: 300px;
          background-color: aqua;
          float: right;
          border:1px solid yellow;
          box-sizing: border-box;
      }
      @media screen and (min-width:900px){
          .bigbox{
              width:900px;
          }
          .aa2{
              display: none;
          }
      }
      @media screen and (min-width:1200px){
          .bigbox{
              width:1200px;
          }
          .aa2{
              display: block;
          }
      }
  <div class="bigbox">
          <div class="list">
              <li>1</li>
              <li>2</li>
              <li>3</li>
          </div>
          <li class="aa2">2</li>
          <li class="aa1">1</li>
          <li class="aa4">4</li>
          <li class="aa3">3</li>
  </div>
  ```

- 十二栅格化

  ```py
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <style>
       *{
              margin: 0;
              padding: 0;
              list-style: none;
          }
      .container{
          width:100%;
          height: auto;
          margin: 0 auto;
          border:1px solid red;
      }
      .container .row{
          width:100%;
          height: 200px;
          overflow:hidden;
          margin:0 auto;
      }
      .container .row .col-l-3{
          height: 100%;
          border:1px solid #ccc;
          box-sizing: border-box;
          float:left
      }
      @media screen and (min-width:600px){
          .container{
              width:600px;
          }
          .container .row .col-m-1{
              width: 8.3333333%;
              height: 100%;
              float:left
          }
          .container .row .col-m-2{
              width: 16.66666666%;
              height: 100%;
              float:left
          }
          .container .row .col-m-3{
              width: 25%;
              height: 100%;
              float:left
          }
          .container .row .col-m-4{
              width: 33.33333333%;
              height: 100%;
              float:left
          }
          .container .row .col-m-5{
              width: 41.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-m-6{
              width: 50%;
              height: 100%;
              float:left
          }
          .container .row .col-m-7{
              width: 58.3333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-m-8{
              width:66.66666666666% ;
              height: 100%;
              float:left
          }
          .container .row .col-m-9{
              width: 75%;
              height: 100%;
              float:left
          }
          .container .row .col-m-10{
              width: 83.333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-m-11{
              width: 91.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-m-12{
              width: 100%;
              height: 100%;
              float:left
          }

      }
      @media screen and (min-width:900px){
          .container{
              width:900px;
          }
          .container .row .col-s-1{
              width: 8.3333333%;
              height: 100%;
              float:left
          }
          .container .row .col-s-2{
              width: 16.66666666%;
              height: 100%;
              float:left
          }
          .container .row .col-s-3{
              width: 25%;
              height: 100%;
              float:left
          }
          .container .row .col-s-4{
              width: 33.33333333%;
              height: 100%;
              float:left
          }
          .container .row .col-s-5{
              width: 41.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-s-6{
              width: 50%;
              height: 100%;
              float:left
          }
          .container .row .col-s-7{
              width: 58.3333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-s-8{
              width:66.66666666666% ;
              height: 100%;
              float:left
          }
          .container .row .col-s-9{
              width: 75%;
              height: 100%;
              float:left
          }
          .container .row .col-s-10{
              width: 83.333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-s-11{
              width: 91.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-s-12{
              width: 100%;
              height: 100%;
              float:left
          }

      }
      @media screen and (min-width:1200px){
          .container{
              width:1200px;
          }
          .container .row .col-l-1{
              width: 8.3333333%;
              height: 100%;
              float:left
          }
          .container .row .col-l-2{
              width: 16.66666666%;
              height: 100%;
              float:left
          }
          .container .row .col-l-3{
              width: 25%;
              height: 100%;
              float:left
          }
          .container .row .col-l-4{
              width: 33.33333333%;
              height: 100%;
              float:left
          }
          .container .row .col-l-5{
              width: 41.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-l-6{
              width: 50%;
              height: 100%;
              float:left
          }
          .container .row .col-l-7{
              width: 58.3333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-l-8{
              width:66.66666666666% ;
              height: 100%;
              float:left
          }
          .container .row .col-l-9{
              width: 75%;
              height: 100%;
              float:left
          }
          .container .row .col-l-10{
              width: 83.333333333%;
              height: 100%;
              float:left
          }
          .container .row .col-l-11{
              width: 91.66666666666%;
              height: 100%;
              float:left
          }
          .container .row .col-l-12{
              width: 100%;
              height: 100%;
              float:left
          }
      }
  </style>
  <body>
      <div class="container">
          <div class="row">
              <div class="col-l-3 col-m-6 col-s-4"></div>
              <div class="col-l-3 col-m-6 col-s-4"></div>
              <div class="col-l-3 col-s-4"></div>
              <div class="col-l-3"></div>
          </div>
      </div>
  </body>
  </html>
  ```

  var 声明一个新的变量

  ​	var 变量=xx    在函数外是全局变量，在函数内是局部变量

  ​				在函数内部不用var声明，直接赋值，也是全局变量，当函数引用后就存在这个全局变量

  为什么要使用局部变量：

  1.语言的使用层面：防止全局变量的污染

  2.节省内存的使用，局部变量运行完就销毁

  为了在函数的外部能够访问到函数内部的变量，**闭包函数**

  在函数的里面引用外层函数的变量，当里层函数调用的时候形成闭包