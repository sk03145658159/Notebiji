# BOM（浏览器对象模型）

完成窗口与窗口之间的通信：`window`对象是核心对象

- history
- location
- dom
- screen
- frames
- navigation

## window对象：

#### 属性：

- 获取浏览器的宽高
  - [ ] window.innerWidth  获取浏览器的宽度
  - [ ] window.innerHeight  获取浏览器的高度
  - [ ] document.documentElement.clientWidth   ie8及以下的版本获取宽度
  - [ ] document.documentElement.clientHeigth   ie8及以下的版本获取高度
- 获取浏览器左上角距屏幕左上角的偏移量
  - [ ] window.screenTop  垂直偏移量
  - [ ] window.screenLeft  水平偏移量
- 注：windowing可以省略不写

### 方法：

- alert()  弹出框

- prompt()  输入框

- confirm()  提示框

- close()  关闭页面

- open(”url路径“，"width=300,height=200")  打开页面 （设置属性）

- setInterval(fn函数名，1000) ;  隔一定的时间重复不断的执行一个函数     毫秒为时间单位

- clearInterval(t)   清楚时间函数    let t=window.setInterval();

- setTimeout(fn函数名,1000时间间隔)  隔一定的时间只执行一次函数

- clearTimeout(t)  清楚时间函数 

  ```js
  	console.log(window.innerWidth);
      console.log(innerWidth);
      console.log(window.innerHeight);
      console.log(window.screenTop);
      console.log(window.screenLeft);
      let div=document.getElementsByTagName("div")[0];
      /*div.onclick=function(){
          window.close();
      }*/
      div.onclick=function(){
          window.open("dom.html");
      }
      let t=0;
      function sk() {
          console.log(1);
          t=t+1;
          if(t==3){
              window.close();
          }
      }
      let s=window.setInterval(sk,1000);
      window.clearInterval(s);
  ```

## history对象：

### 属性：

- history.length   用来显示历史记录的长度

### 方法：

- history.forward()前进
- history.back()后退
- history.go(0)刷新

## location对象：

### 属性：

- location.href   设置（赋予新值）或获取页面地址的
- location.host  获取主机名加端口号
- location.hostname   主机名
- location.port  端口号
- location.protocol   协议
- location.pathname  路径
- location.serach  问号后的搜索字段

### 方法：

- location.reload()重新加载
- location.replace(“替换页面地址”)页面替换，不会增加历史记录
- location.assign("替换页面地址")页面替换，能够增加历史记录

