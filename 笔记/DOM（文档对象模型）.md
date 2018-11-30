# DOM（文档对象模型）

## 获取元素：

- 获取id名的元素

  ```js
  let obj=document.getElementById("idName");	
  ```


- 获取类名的元素    获取的是集合,通过下标访问，不是数组，可以遍历访问

  ```js
  let obj=document.getElementsByClassName("classname");
  ```


-  获取标签名的元素      集合，通过下标访问，也可遍历访问

  ```js
  let obj=document.getElementsByTagName("tagname");
  ```

  ```js
  //页面加载完成
  window.onload=function(){
      //获取id名
      let box=document.getElementById("box");
      console.log(box);
      box.style.background="pink";
      //获取类名
      let list=document.getElementsByClassName("list");
      console.log(list);
      list[0].style.background="green";
      //遍历
      for(let i=0;i<list.length;i++){
          list[i].style.background="pink";
      }
      //获取标签名
      let li=document.getElementsByTagName("li");
      li[0].innerText="这是第1个li";
      //遍历
      for(let i=0;i<li.length;i++){
          li[i].innerText=`这是第${i+1}个li`;
          li[i].innerHTML="<h3>这是第${i+1}个li</h3>"
      }

  }
  ```

- 指定范围获取元素

  ```js
  let obj=obj.getElementsByClassName("className");
  ```


-    获取选择器选中的第一个元素   

  ```js
  let obj=document.querySelector("选择器");
  ```


-   获取选择器选中的集合   下标   forEach （返回类数组的集合）

  ```js
  let obj=document.querySelectAll("选择器")；
  ```

  ```js
  let banner1=document.querySelector(".banner");
    console.log(banner1);
    let wraper1=document.querySelector(".banner .wraper");
    console.log(wraper1);
    let a2=document.querySelectorAll(".banner .wraper a");
    console.log(a2);
    a2.forEach(function(value,index){
    	console.log(value);
    })
  ```


-    获取id前面需要加#

-    获取属性：document.querySelector("[属性名]")

     ```js
      <input type="text" name="phone">
     let phone=document.querySelector("[name=phone]");
     ```

     ​

## 操作样式：

### 获取样式：

- 获取行内样式：obj.style.attr;   attr为样式
- 获取css样式和行内样式通用：getComputedStyle(obj,null).attr;

### 设置：

- 行内样式：

  ```js
  obj.style.属性名=属性值;
  window.onload=function () {
      let list=document.getElementsByTagName("li");
      for(let i=0;i<list.length;i++){
          list[i].onclick=function () {
              for(let j=0;j<list.length;j++){
                  list[j].style.background="none";
                  list[j].style.borderRadius=0;
              }
             list[i].style.background="pink";
              list[i].style.borderRadius="50%";
              list[i].style.transition="all 1s";
          }
      }

  }on+click点击事件   on+事件名（引用事件）onmouseenter鼠标移入  onmouseleave鼠标移出
  onkeydown=function(num){}键盘输入事件，num保存键盘输入数据。
  ondblclick双击事件  onblur失去焦点事件
  ```


- 批量操作样式：

  ```js
  obj.className="";
  批量设置
  window.onload=function () {
      let list=document.getElementsByTagName("li");
      for(let i=0;i<list.length;i++){
          list[i].onclick=function () {
              for(let j=0;j<list.length;j++){
                  list[j].className="";
              }
              list[i].className="hot";
          }
      }
  }
  .hot{
       background:#368297;
       border-radius: 50%;
    }
  obj.className="box"
  obj.classList.add("box") 添加类
  obj.classList.remove("box")删除类
  obj.classList.toggle("box") 切换类
  obj.id="box"
  ```

  ​

### 操作内容：

- innerText       obj.innerText
- innerHTML：可以识别标签对

#### 获取表单的值

obj.value  //重置的话将他赋为空字符串

//javascript:;在a标签内设置该行内样式，取消a标签的刷新效果。

### 双向轮播图制作

- 将下一个图片next位置就位
- 移动
- 赋值  now=next

### 操作属性：

#### 标准属性：obj.attr

#### 自定义属性：

- 获取：obj.getAttribute("name");
- 设置：obj.setAttribute("name",value);

### 元素的尺寸和位置

- obj.offsetWidth  获取元素的真实宽度（border+padding++width）

- obj.offsetHeight   获取元素的真实高度

- obj.offsetTop   该元素的外边框距具有定位属性父元素内边框的垂直距离

- obj.offsetLeft   该元素的外边框距具有定位属性父元素内边框的水平距离

- obj.scrollTop:   有滚动条的元素，浏览器滚动时在垂直方向的拉动距离。

  ```js
  window.onscroll=function{
  	document.body.scrollTop||document.documentElement.scrollTop  //兼容问题
  }
  例子
  window.onload=function() {
      //浏览器的高度+滚动的距离>该楼层的offsetTop
      let floor = document.querySelectorAll(".floor");
      // let arr=[];
      let wi = innerHeight;
      let search = document.querySelector(".search");
      let back = document.querySelector(".back");
      let item = document.querySelectorAll(".item");
      /*floor.forEach(function(element,index){
         arr[index]=element.offsetTop;
      })*/
      window.onscroll = function () {
          let wid = document.body.scrollTop || document.documentElement.scrollTop;
          floor.forEach(function (element, index) {
              if (wi + wid > element.offsetTop + 200) {   //按序加载
                  let img = element.querySelectorAll("img");
                  img.forEach(function (v) {
                      v.src = v.getAttribute("isrc");

                  })
                  for (let j = 0; j < item.length; j++) {
                      item[j].style.background = "#fff";
                  }
                  item[index].style.background = "pink";
              }
          })
          if (wid > 300) {     //上导航
              animate(search, {top: 0}, 200);
          }
          if (wid < 300) {
              animate(search, {top: -50}, 200);
          }
      }
      back.onclick = function () {     //回顶
          animate(document.body, {scrollTop: 0});
          animate(document.documentElement, {scrollTop: 0});
      }
       item.forEach(function (element,index) {   //侧导标
         element.onclick=function () {
             let newhei=floor[index].offsetTop;
             animate(document.body,{scrollTop:newhei});
             animate(document.documentElement,{scrollTop:newhei});
         }
     })
  }
  ```

- obj.scrollLeft：有滚动条的元素，浏览器滚动时在水平方向的拉动距离。

## 1.动态创建元素

```js
document.createElement("TagName标签名");
```

### 2.添加类名

添加随机效果的类名。

### 3.插入到页面

```js
父元素.appendChild(子元素)
document.body.appendChild(div);
....................................例
 function rgb() {
        let a=Math.floor(Math.random()*256);
        let b=Math.floor(Math.random()*256);
        let c=Math.floor(Math.random()*256);
        return "rgb("+a+","+b+","+c+")";
    }
    for(let i=0;i<100;i++){
        let d=Math.floor(Math.random()*30+30);
        let to=Math.floor(Math.random()*innerHeight-d);
        let lef=Math.floor(Math.random()*innerWidth-d);
        let color=rgb();
        let div=document.createElement("div");
        console.log(div);
        div.classList.add("div");
        div.style.width=d+"px";
        div.style.height=d+"px";
        div.style.top=to+"px";
        div.style.left=lef+"px";
        div.style.background=color;
        document.body.appendChild(div);
    }
```

### 倒计时的制作：

```js
<body>
距离2018年10月1日还有<span></span>月<span></span>天<span></span>小时<span></span>分钟<span></span>秒
</body>
</html>
<script>
    fn1();
    setInterval(fn1,1000);
    function fn() {
        let now=new Date();
        let future=new Date(2018,9,1);
        let time=Math.floor((future.getTime()-now.getTime())/1000);
        let arr=[];
        let month=Math.floor(time/(30*24*60*60));
        arr.push(month);
        time=time%(30*24*60*60);
        let day=Math.floor(time/(24*60*60));
        arr.push(day);
        time=time%(24*60*60);
        let hour=Math.floor(time/(60*60));
        arr.push(hour);
        time=time%(60*60);
        let minute=Math.floor(time/60);
        arr.push(minute);
        time=time%(60);
        let sec=time;
        arr.push(sec);
        console.log(arr);
        return arr;
    }
    function fn1() {
        let span=document.querySelectorAll("span");
        let arr1=fn();
        for(let i=0;i<span.length;i++){
            span[i].innerText=arr1[i];
        }
    }
</script>
```

### 字符串中对象的方法

```js
let str=new String;
```



- 查找对应的字符或字符编码

  - [ ] obj(str).charAt() //  查找某一个下标的字符
  - [ ] obj(str).charCodeAt()//查找某个下标的字符编码
  - [ ] string.fromCharCode(23321字符编码）//根据字符编码查找对应的字符

- 查找下标

  - [ ] obj(str).indexOf("")   //查找对应字符的下标，如果有返回下标，如果没有返回-1
  - [ ] obj(str).lastIndexOf("")//查找对应字符的下标，如果有返回下标，如果没有返回-1（从后往前查找）
  - [ ] obj(str).search("")  //正则，判定是否存在该字符
  - [ ] obj(str).match("")   //返回一个数组，如果没有，返回null。

- 字符串的截取

  - [ ] obj(str).substr();      substr(开始下标,截取长度(可以省略，默认截取的结尾))
  - [ ] obj(str).substring();    substring(start,end)  从start开始截取，到end前结束
  - [ ] obj(str).slice(2,5);  同上从start开始截取，到end前结束

- 字符串大小写转换

  - [ ] obj(str).tolowerCase()  //转换为小写
  - [ ] obj(str).toUpperCase()  //转换为大写

- 替换

  - [ ] obj(str).replace("山","陕");

- 转换

  - [ ] obj(str).split(",");

        ```js
        let arr1="1,2,3,4,5"
        arr2=arr1.split(",");
        ```

- **includes() **方法用于判断一个字符串是否包含在另一个字符串中，根据情况返回 true 或 false。

  - [ ] 语法 str.includes(searchString[, position])

  - [ ] 参数：`searchString`

        要在此字符串中搜索的字符串。

        `position`

        可选。从当前字符串的哪个索引位置开始搜寻子字符串，默认值为0。

  - [ ] 返回值：如果当前字符串包含被搜寻的字符串，就返回 true；否则返回 false。

### 数组中对象的方法

- obj.push()    在数组最后插入内容

- obj.pop()    删除数组最后一位

- obj.unshift()     在数组之前插入

- obj.shift()   删除数组的前一位

- 万能插入和删除

  - [ ] obj.splice(位置，删除的长度，“增加的元素”，“增加的元素”)

- obj.includes()  判断是否包含该元素

- obj.slice(开始位置，结束前位置)    截取一段元素

- newarr=arr.concat(["a","b","c"]);   连接

- obj.reverse()   取反

- obj.join(指示连接方式)   转换为字符串

- 排序

  - [ ] obj.sort((x,y)=>x-y);     升序排列
  - [ ] obj.sort((x,y)=>y-x);   降序排列

- obj.find( )找第一个符合要求的元素。

  ```js
  let arr=[1,2,3,4];
  let num=arr.find(item=>item>8)/let num=arr.find(function(item){
    											return item>8;
  										})
  ```

- obj.findIndex()  获取第一个符合要求的元素下标

- obj.some(item=>item>10)  判断数组中是否存在满足要求的元素，有返回true，没有返回false

- obj.every(item=>item>10)  判断数组中是否全部满足要求

- obj.filter(item=>item%2==0)    按要求筛选后的返回新的数组   过滤和筛选

- obj.forEach((item)=>{return item*10;})   让数组中每一个元素都执行一个函数，不会影响原数组

- obj.map((item)=>{return item*10;})     让数组中的每一个元素都执行一个函数，返回一个新数组

## 日期对象：

```js
日期的三种定义方式
let a=new Date("2018/8/8 12:00:00");
let a1=new Date("12:00:00 2018/8/8");
let a3=new Date(2018,8,8,12,0,0)  此种月份从0开始
let now=new Date()   获取当前时间
方法：
设置格尼日志时间
1.now.setFullYear(2020)  设置年
2.now.setMonth(5)   	设置月（从零开始）
3.now.setDate(26)		设置日
4.now.setHours(16)		设置小时
5.now.setMinutes(0)		设置分钟
6.now.setSeconds(0)
7.now.setMilliseconds(0)
设置世界协调时
1.now.setUTCFullYear
2.now.setUTC同上
获取
now.getFullYear()	获取年
now.getMonth(5)   	获取月（从零开始）
now.getDate(26)		获取星期
now.getHours(16)		获取小时
now.getMinutes(0)		获取分钟小时
now.getSeconds(0)
now.getMilliseconds(0)
**now.getTime()  从今到1970年一月一日零时零秒的时间，返回毫秒
获取世界协同时
方法同上
```



## 节点

#### 文档节点document：

节点的信息属性

- nodeName:#document
- nodeValue:null
- nodeType:9

#### 元素节点：

节点的信息属性

- nodeName:大写的标签名
- nodeValue:null
- nodeType:1

#### 属性节点：

节点的信息属性

- nodeName:大写的属性名
- nodeValue:属性值
- nodeType:2

#### 文本节点：

节点的信息属性

- nodeName:#text
- nodeValue:文本
- nodeType:3

#### 注释节点

节点的信息属性

- nodeName:#comment
- nodeValue:注释内容
- nodeType:8

### 节点的获取

- 节点.childNodes      获取子节点
- 节点.parentNode        获取父节点
- 节点.previousSibling  获取上一个兄弟节点
- 节点.nextSibling     获取下一个兄弟节点
- 节点.previousElementSibling   获取上一个兄弟元素节点
- 节点.nextElementSibling  获取下一个兄弟元素节点

### 节点的方法：

- 创建元素节点

  ```js
  let div=document.createElement("div");
  ```

- 在最后插入节点

  ```js
  给谁插入，先获取过来，然后调用节点方法:节点.appendChild()
  let box =document.querySelector("box");
  box.appendChild(div)
  ```

- 在之前插入节点

  ```js
  节点.insertBefore(要插入的元素，插入位置之后的元素)
  let span=document.createElement("span");
  box.insertBefore(span,div)
  ```

- 创建文本节点

  ```js
  let text1=document.createTextNode("这是sapn标签")；
  span.appendChild(text1);
  ```

- 创建注释节点

  ```js
  let comment1=document.createComment("这是注释节点");
  box.appendChild(comment1);
  ```

- 创建属性节点

  ```js
  let attr=document.createAttribute("id");
  attr.nodeValue="box";     //为id赋值
  //设置属性节点
  box.setAttributeNode(attr);
  ```

- 简单方式

  ```js
  div.innerText = "this is div"
  div.innerHTML = "<a href=\"\">百度</a>"
  div.setAttribute("attr","小明")
  ```

- 删除节点

  ```js
  删除节点
  box.removeChild(div)
  删除属性节点
  box.removeAttribute("id")

  ```

- 复制节点

  ```py
  aa=bb.cloneNode()
  ```

  ​

例子

```js
<body>
	<header class="tit">
		<div class="bigBox">
			<label for="todo">ToDoList</label>
			<input type="text" id="tex" placeholder="添加ToDo">
		</div>
	</header>
	<main>
		<div class="cont1">
			<h2>正在进行<span>5</span></h2>
		</div>
		<div class="cont2">
			<h2>已经完成<span>5</span></h2>
		</div>
	</main>
</body>
</html>
<script>
	let arr1=[];
	let arr2=[1,2,3];
	let cont1=document.querySelector("main .cont1");
	let tex=document.querySelector("#tex");
	tex.onkeydown=function(num){
		if(num.keyCode==13){
			arr1=[];
			arr1.push(tex.value);
			arr1.forEach(function(value,index){
				let li=document.createElement("li");
				cont1.appendChild(li);
				let checkbox=document.createElement("input");
				li.appendChild(checkbox);
				checkbox.type="checkbox";
				checkbox.id="check";
				let box=document.createElement("div");
				box.className="box";
				li.appendChild(box);
				let rig=document.createElement("div");
				rig.className="rig";
				li.appendChild(rig);
				box.innerText=value;
			})
			tex.value="";
		}
	}
</script>
```

## 事件：

### 事件的添加方式：

- 节点.onclick=function(){}

- 节点.addEventListener("事件","事件处理程序","事件类型");     实现一个事件具有多个处理程序    （事件不用加on）

- 节点 .removeEventListent(事件，添加的函数名)                 删除事件监听

  ```py
  def aa(){
    
  }
  节点.addEventListener('mousedowm',aa)
  节点.removeEventListener('mousedown',aa)
  ```

  ​

### 事件的构成：

- 事件源：谁去触发事件谁就是事件源
- 事件
- 事件处理程序

### 常用事件（web端）

- 鼠标事件：
  - [ ] onclick 单击

  - [ ] ondblclick  双击

  - [ ] onmousedown  按下

  - [ ] onmouseup   抬起

  - [ ] onmousemove  鼠标移动

  - [ ] onmouseenter   移入   不会引发事件流

  - [ ] onmouseleave   移出    不会引发事件流

  - [ ] onmouseover    移入   会引发事件流

  - [ ] onmouseout     移出     会引发事件流

  - [ ] oncontextmenu  右击事件

        ```js
        document.oncontextmenu=function(e){
          e.preventDefault();//阻止浏览器的默认行为
        } 
        ```

- 键盘事件

  - [ ] onkeydown 键盘按下
  - [ ] onkeyup  键盘抬起
  - [ ] onkeypress  键盘按下（当按下功能键时ctrl,shift,delete,esc等不会触发事件）

- 表单事件

  - [ ] oninput   输入事件
  - [ ] onchange （和输入前的内容相比） 内容发生改变，并且失去焦点
  - [ ] onblur     失去焦点
  - [ ] onfocus   获取焦点
  - [ ] onsubmit  提交表单
  - [ ] onselect    文本选中

- 窗口事件

  - [ ] onscroll   滚动条
  - [ ] onload    加载完成
  - [ ] onresize   窗口大小改变

事件发生顺序：mousedown-mousemove-mouseup-onclick

### 事件对象：用来保存事件触发时的信息

- w3c  ：事件处理程序的形参中    节点.事件=function(事件对象){}
- ie   ：window.event
- 鼠标事件对象中的常用属性：
  - [ ] clientX  距离浏览器的X偏移量
  - [ ] clientY  距离浏览器的Y偏移量
  - [ ] offsetX  距离事件源X轴的偏移量
  - [ ] offsetY  距离事件源Y轴的偏移量  
  - [ ] screenX  距离屏幕X轴的偏移量
  - [ ] screenY   距离屏幕Y轴的偏移量
- 键盘事件对象常用属性
  - [ ] keyCode  键盘码
  - [ ] ctrlKey  是否按下ctrl键
  - [ ] shiftKey 是否按下shift键
  - [ ] altKey  是否按下alt键
  - [ ] key  键盘名

### 移动端事件：

- ontouchstart   按下
- ontouchmove   移动
- ontouchend    抬起

## 事件流：

#### 当触发一个事件时，由这个事件的容器到整个文档都按照特定的顺序进行一次触发

#### 事件的分类：

- #### 捕获型事件  true     从不具体的事件源到具体的事件源 (document=>html=>body=>具体事件源)

- ####  冒泡型事件  false   从具体的事件源到不具体的事件源

####  所有事件都默认为冒泡型（通过addEventListener{‘click’，function,true}设置为捕获型）

#### 阻止事件流的发生：

```js
function(event)
let event=event||window.event  兼容性问题
event.stopPropagation()
event.returnValue=ture    ie浏览器
```

## 事件委派：

e.target  确定目标事件源

一般当box中的元素为动态添加的元素时使用。

```js
<style>
    .box{
        width:400px;
        height: 400px;
        border:1px solid red;
        margin: 0 auto;
    }
    .son{
        width:100px;
        height: 100px;
        border:1px solid blue;
        border-radius: 50%;
        float:left;
    }
    。tian{
        width=100px;
        height: 100px;
    }
</style>
<body>
    <div class="box">
        <div class="son"></div>
        <div class="son"></div>
    </div>
    <div class="tian">添加</div>
</body>
</html>
<script>
    let box=document.querySelector(".box");
    let son=document.querySelectorAll(".son");
    let tian=document.querySelector(".tian");
    
   
    box.onclick=function(e){   //通过委任使点击box实现点击son同样的目的
        console.log(e);
        if(e.target.className=="son"){
            e.target.style.background="pink";
        }
    }
    tian.onclick=function(){
        let div=document.createElement("div");
        div.className="son"
        box.appendChild(div);
    }
</script>
```

## 正则

用来描述或者匹配一系列符合某种规则的字符串

js中的正则是单行处理

### 作用：

- 数据验证
- 内容检索
- 内容替换
- 内容过滤

### 创建正则对象：

- 通过实例化对象

  ```js
  let reg=new RegExp("正则表达式","模式修正符")
  模式修正符：
  g全局   不是每一次都从开头开始匹配，从上一次的下标开始
  i不区分大小写
  m换行    具有多个开始和结束
  ```

- 通过字面量的方式

  ```js
  let reg=/\d/g        /正则表达式/模式修正符  （双斜杠//表示定界符，里面写正则表达式） 匹配多个字符串用｜隔开
  let con=document.querySelector("[name=con]");
  let reg=(/毒品|枪支|法轮功/g);
  con.oninput=function(){
          let arr=reg.exec(this.value);
          if(arr){
              this.value=arr[0].length==3?this.value=this.value.replace(arr[0],"***"):this.value=this.value.replace(arr[0],"**")
          }
      }
  ```

  ​

### 正则对象的常用方法

- test()    传入被匹配的字符串，作用检测正则对象是否能够匹配str ，返回值为true||false

- exec()   传入被匹配的字符串，作用检测正则对象是否能够匹配str ，返回值：如果能匹配，返回一个拥有特殊属性的数组，如果不能匹配，返回null。

  ```js
  let reg=new RegExp("正则表达式","模式修正符")
  let arr=reg.test("")
  ```

### 正则表达式

- 原子：正则表达式中最小的内容。  /d :可以匹配0-9     \w:可以匹配任意的数字、字母、下划线         \s:匹配空白（/n,/r,/t）      /D:匹配除了0-9以外的字符      \W:匹配除了数字、字母、下划线以外的字符      \S：匹配除了空白（/n,/r,/t）以外的字符串          原子匹配一个字符

- 原子表 [ ]    匹配一位字符（自己设定）在知道匹配结果满足条件下使用[]。

  ```js  
  [a-c]  匹配a-c
  [a-z]  匹配小写字母
  [A-Za-z0-9] 匹配大写字母，小写字母和0-9
  [a-zA-z0-9/s]匹配大写字母，小写字母和0-9和空白
  ```

- 元字符

  - [ ] .  匹配所有字符

  - [ ] ｜   或

        ```js
        let con=document.querySelector("[name=con]");
        let reg=(/毒品|枪支|法轮功/g);
        con.oninput=function(){
                let arr=reg.exec(this.value);
                if(arr){
                    this.value=arr[0].length==3?this.value=this.value.replace(arr[0],"***"):this.value=this.value.replace(arr[0],"**")
                }
            }
        ```

        ​

- 原子组   实现存储和调用,默认存储到内存中，可以使用\1  \2等方式调用。（？：）可以使原子组不在内存中存储，不可以调用。    进行分类时常使用。在已知结果情况选项下使用（｜ ｜）。

  ```js
  一。
  let str1="山西优逸客"；
  let str2="陕西优逸客";
  let reg=/(山西｜陕西)优逸客/g
  二。
  let str="<div>stop</div>";
  let reg=/<(div)>stop<\/ \1>/g;
  例子
  let arr1="陕西优逸客";
      let arr2="山西优逸客";
      let reg=/(山西|陕西)优逸客/g;
      console.log(reg.exec(arr2));
      let arr3="abdehgeyu";
      let reg1=/[a-z]/g;
      console.log(reg1.exec(arr3));
      let arr4="<div>stop</div>";
      let reg2=/<(div)>stop<\/\1>/g;   //   \1利用原子组  \转义字符
      console.log(reg2.exec(arr4));
      let str="<div>山西优逸客-山西</div>"
      let reg3=/<(div)>(山西|陕西)优逸客-\2<\/\1>/g;
      console.log(reg3.exec(str));
      let reg4=/<(div)>(?:山西|陕西)优逸客-\2<\/\1>/g;
      console.log(reg4.exec(str));
  ```

- 正则表达式使用场景：

  - [ ] 正则对象
  - [ ] str.split(正则对象)
  - [ ] str.replace(正则对象，替换的内容)
  - [ ] str.search;

## 正则中的数量

贪婪:尽可能多取

*零个或多个  >=0

```js
let phone="123456251423516";
let reg=/\d*/g;
```

+一个或多个 >=1

?零个或一个

{11}限制长度   ｛15，18｝15到18个     ｛n，｝n个或多个

吝啬：尽可能少取

*？

+？

？？

{n,}?

{15,18}?

## 边界判断

- ^   开始

- $  结束

  单用时为以什么开始，以什么结束

- \b单词边界

- \B  非单词边界

```js
电话、邮箱、身份证号 
<input type="text" name="phone">
 <input type="text" name="id">
 <input type="text" name="email">
  let phone=document.querySelector("[name=phone]");
let id=document.querySelector("[name=id]");
let email=document.querySelector("[name=email]");
phone.oninput=function(){
  let reg=/^1[3578]\d{9}$/g;
  let arr=reg.exec(this.value);
  if(arr){
    phone.style.border="2px solid green";
  }
  else{
    phone.style.border="2px solid red";
  }
}
id.oninput=function(){
  let reg=/^(\d{15}|\d{18}|\d{17}[xX])$/;
  let arr=reg.exec(this.value);
  if(arr){
    id.style.border="2px solid green";
  }
  else{
    id.style.border="2px solid red";
  }
}
email.oninput=function(){
  let reg=/^[0-9a-zA-Z][0-9a-zA-Z-_\.]*@(qq|1235|GWWD)\.(com|cn)$/g;
  let arr=reg.exec(this.value);
  if(arr){
    email.style.border="2px solid green";
  }
  else{
    email.style.border="2px solid red";
  } 
```

#### 取消浏览器默认样式

e.preventDefault() 

