# jQuery（解决了兼容性问题）

本质：JavaScript框架

宗旨：write Less do More

作用：优化js的操作、dom操作、页面交互、事件、ajax、动效

#### 特性：隐式循环，链式调用。单线程异步机制的语言  

**目的：利用极少的资源，做更多的事情，单线程模拟多线程**

单线程：程序同一时间只能执行同一件事件

异步：把需要耗费时间以及不确定的时间的代码，放到异步执行

（从上到下执行，线程先执行正常线程的代码，遇到异步的代码将其一次放到后面的数组中，等正常线程代码执行完后线程再执行异步的代码）

### 队列：优雅的处理异步代码的执行顺序（javascript中没有，用回调函数实现）   [1,2,3,4,5...]

级别由高到低分为

- animate（不需命令，自己出队入队）

  ```py
  $('div').animate({width:400},1000,fn)  效果执行后执行的函数
  $('div').animate({height:400},1000)
  ```

  ​

- “fx"

  ```py
  $('div').queue(function(){   //队列名称默认为fx
    console.log(1)
    $('div').dequeue()  //出队
  })
  $('div').queue(function(){  
    console.log(2) 
  })
  例子
  let box=document.querySelector('div')
      function animate(obj,attrobj,duration,callback){
          var start={}
          var change={}
          for(var i in attrobj){
              start[i]=parseInt(getComputedStyle(obj,null)[i])
              change[i]=attrobj[i]-start[i]
          }
          var time=0
          var t=setInterval(function(){
              time+=40
              if(time>=duration){
                  clearInterval(t)
                  for(var i in attrobj){
                      obj.style[i]=attrobj[i]+'px'
                  }
                  callback()
              }else{
                  for(var i in attrobj){
                      obj.style[i]=start[i]+change[i]*time/duration+'px'
                  }
              }
  ```


          },40)
      }
  $('.box').click((e)=>{
          $(this).queue(function () {
              animate($('.box')[0],{width:400},1000,function () {
                  $(this).dequeue()
              })
          })
          $(this).queue(function () {
              animate($('.box')[0],{height:400},1000,function () {
                  $(this).dequeue()
              })
          })
          $(this).queue(function () {
              $('.box').css('border',"5px solid blue")
              $(this).dequeue()
          })
          $(this).queue(function () {
              $('.box').css('background',"pink")
              $(this).dequeue()
          })
          $(this).queue(function () {
              animate($('.box')[0],{height:200},1000,function () {
                  $(this).dequeue()
              })
          })
          $(this).queue(function () {
              animate($('.box')[0],{width:200},1000)
          })
      })
      用回调函数是为了让当前队列元素效果实现后再出队，下一条效果才会执行。不然会立刻出队，然后下一条进队执行，无法实现处理异步代码的执行顺序
  ```

  ​

- 自定义队列（每一步都需要自己去命令进队和出队）

  ### 操作队列的三条语句

  - $('div').stop()   停止当前的执行，继续进行下一条
  - $('div').stop(true)    全部停止
  - $('div').finish(‘fx’)   干掉前边的队列元素，直接执行最后一条队列元素

## jQuery核心函数   jQuery()

- 传入选择器：返回jQuery对象

- 传入函数:给document添加 ready(准备加载)事件

  ```js
  $(function(){
    
    })
  同
  window.onload=function(){    网页所有内容加载完
    
  }
  区别：jQuery在document中加载，第二个在window中加载并且首先加载，两个存在先后顺序。
  ```

  ```py
  document.addEventListener('DOMContentLoaded',function(){
      
  })   dom对象加载完毕 等同于$（function(){}）,可以代替window.onload
  ```

- 传入dom对象：返回jQuery对象

- 传入字符串“<div></div>”：创造新节点。   “<div><span></span><div>”

  ```js
   $("<div></div>").appendTo(".box")
  ```

  ​

## jQuery对象常用方法

css样式方法

- .css("样式属性","样式值")
- .css({})

筛选方法

- .eq(index)返回对应下标的jQyuery对象
- .get(index))返回对应下标的DOM对象
- .first（）
- .last（）
- .find()
- .hasClass("classname")    检查jquery对象数组中是否存在一个类名为***的对象，返回true和false
- .filter(”选择器“｜“元素”｜function(){})  筛选出符合条件的对象
- .is("选择器")   判断是否为某个标签
- .map(fn())  遍历对象生成一个新的数组
- .has("选择器")  选择具有某选择器的jquery对象，返回一个选中的juqery对象。
- .not("选择器")  从jquery数组中删除选中的元素
- .slice(start,end)   截取指定位置的jquery对象   end可以省略
- .each(function(index,item))  遍历jquery数组   index在前   item在后
- .index()  返回jquery对象在数组的下标

操作属性的方法（传入一个参数为获取属性，两个参数为设置属性）

- .attr()
- .removeAttr()
- .prop()      **
- .removeProp()      **    

操作类名的方法

- .addClass()   增加类
- .removeClass()   移除类
- .toggleClass()  切换 ，没有就增加，有就删除

操作内容的方法

- .text()
- .html()   可识别标签对
- .val()   表单

toArrary()将jQuery数组转换成原生数组。

## jQuery对象元素的位置信息

- .offset()  返回一个位置信息的对象（top:***,left:***）  相对于浏览器的位置   offset().left     offset().top
- .position()   返回一个位置信息的对象（x:***,y:***）  相对于定位的祖先元素的位置
- .scrollTop()     设置滚轮高度为0：.scrollTop(0) 
- .scrollLeft()
- .width()    元素的css所设宽度，不包括pangding值
- .height() 元素的css所设高度，不包括pangding值
- .innerWidth() 元素的真实宽度（不包括边框），包括padding值
- .innerHeiht()   元素的真实高度（不包括边框），包括padding值
- outerWidth()    包括边框的宽度
- outerHeight()     包括边框的高度

## 事件对象

- e.height()  获取元素的高度
- e.width()  获取元素的宽度
- e.offsetX
- e.offsetY
- e.pageX
- e.pageY
- e.target
- e.currentTarget==this 
- e.stopPropagation()
- e.preventDefault()

## 事件

- one()
- on()
- trigger()  自动触发事件
- triggerHandler  自动触发事件，并且清除浏览器默认行为
- hover(fn,fn)  传入两个函数，鼠标的移入和移出


json 没有面向对象的特质，使一种独有的存储数据的对象

用call改变this指针

### 补充

#### 目的：只专注于业务的逻辑，语法的问题

- 将原生的单个化操作，批量操作
- 将原生逐步操作的方式，链式操作
- 将原生操作负责的逻辑，提供简单的接口
- 将原生的复杂的查询方式（兼容 ），简单化

加载html文件，主动发出的请求

link、script、img、background:url、ajax、video、

数据缓存：

1.通过添加属性缓存

name='zhnagsan'

let div=document.querySelector('div')

div.name=name

2.存到jquery中的data中

name='zhnagsan'

$('div').date(name)

#### serializeArray() 方法

serializeArray() 方法通过序列化表单值来创建对象数组（名称和值）。

您可以选择一个或多个表单元素（比如 input 及/或 textarea），或者 form 元素本身。

serializeArray() 方法序列化表单元素（类似 [.serialize() 方法](http://www.w3school.com.cn/jquery/ajax_serialize.asp)），返回 JSON 数据结构数据。

注意：此方法返回的是 JSON 对象而非 JSON 字符串。需要使用插件或者第三方库进行字符串化操作。

返回的 JSON 对象是由一个对象数组组成的，其中每个对象包含一个或两个名值对 —— name 参数和 value 参数（如果 value 不为空的话）。举例来说：

```py
[ 
  {name: 'firstname', value: 'Hello'}, 
  {name: 'lastname', value: 'World'},
  {name: 'alias'}, // 值为空
]
```

实例

```py
$("button").click(function(){
  x=$("form").serializeArray();
  $.each(x, function(i, field){
    $("#results").append(field.name + ":" + field.value + " ");
  });
});
```

### 插件的制作：插件：能够让功能进行扩展的一个术语

其中运用的**extend原理**为：（利用了浅拷贝和深拷贝） 数据类型分为基本型和引用型，因为数据类型的不同导致存储位置的不同（基本型[简单型数据]存储在栈中，引用型[数组、对象等复杂型数据]存储在堆中[头指针地址数据存储在栈中]） 。所以赋值分为浅拷贝（传址）和深拷贝（传值）。深拷贝需要拷贝到每一项。

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

插件的制作

```py
 开始   function drag(selector){
        this.each(function(index,obj){
                $(obj).on('mousedown',selector,function(e){
                let ox=e.offsetX
                let oy=e.offsetY
                $(this).css({'position':'absolute'})
                e.preventDefault()
                $(document).on('mousemove',(e)=>{
                    let ox1=e.clientX
                    let oy1=e.clientY
                    $(this).css({'left':ox1-ox+'px','top':oy1-oy+'px'})
                })
                $(document).on('mouseup',function(){
                    $(document).off('mousemove')
                    $(document).off('mouseup')
                })
            })
        })
        
    }
    $.fn.extend({"drag":drag})     结束
    $('.forms').drag('.opt')
 插件制作完毕后可以装进一个js文件内，然后直接引用（引用时要注意先引用完jQuery文件）
```



函数本身分为：

函数本身、构造函数（类）、对象

队列控制



### 事件：

- [ ] onmouseenter   移入   不会引发事件流
- [ ] onmouseleave   移出    不会引发事件流
- [ ] onmouseover    移入   会引发事件流
- [ ] onmouseout     移出     会引发事件流
- [ ] js中用hover事件     $().hover(function(){},function(){})