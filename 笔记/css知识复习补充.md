#    css知识复习补充

## 浮动

1. 左浮动  float:left;

2. 右浮动  float:right;

3. 浮动的bug:问题：父元素不设置高度，子元素都浮动时，浮动子元素撑不开父元素的高度。（浮动的元素会脱离文档流）

4. 解决方法

   - 父元素能设置高度的尽量设置高度。

   - 给父元素添加  overflow:hidden;

   - ```css
     给父元素添加最后一个子元素
     .box::after{
       content:"";
       display:block;
       clrar:box；
       width:0;
       height:0;
       line-height:0;
       clear:both;
     }
     ```

## 定位

1. 分类：
   - 相对定位： position:relative;
   - 绝对定位： position:absolute;
   - 固定定位： position：fixed;
     - 调整层级  z-index:999;    层级只能在有定位属性的元素上调整层级。

## 文本模型

1. 文本换行

   ~~~css
   word-break:break-all;   使非中日韩文本换行
   ~~~

2. 单行文本溢出

   ~~~css
   white-space:nowrap;
   overflow:hidden;
   text-overflow:ellipsis;
   ~~~

   1. 禁止换行

      ~~~css
      white-space:nowrap;
      ~~~

   2. 超出部分隐藏

      ~~~css
      overflow:hidden;
      ~~~

   3. 超出文本以省略号显示

      ~~~css
      text-overflow:ellipsis;
      ~~~

   3.多行文本溢出

            ~~~css
   display:-webkit-box;   指定为弹性盒子
   -webkit-box-orient:vertical;  在弹性盒模型中指定元素的排布顺序
   -webkit-line-clamp:3;  指定文本溢出的行数
   line-height:   ;  heigh要是line-height的倍数
   overflow:hidden;

## 表单控件

~~~css
<form action="index.php" method="get">
			action:表单信息提交的位置(为空提交到本页面，相当于刷新)
			method:提交的方式
					get:地址栏，信息量少，安全性低
					post:信息量多，比较安全
	1.输入框    input行内块标签,使用时需转化为块元素
		用户名：<input type="text" placeholder="请输入用户名.." maxlength="10" value="" name="username">
			placeholder:默认提示文本
			maxlength:规定输入的最大字符数
			value:进行数据交互
			name:和而后台进行数据交互
			text-indent:10px 改变默认文本间距
			readonly只能读
	.text:focus{获取焦点
		outline:none; 外边线消失
	}
	2.密码框
		密&nbsp;码<input type="password" placeholder="请输入密码" name="psw">
	3.单选按钮   name值需相同
		请选择你的性别：
		<label for="man"></label>   for后面存放idname
		男：<input type="radio" name="sex" id="man" checked="">   checked默认选中
		</label>  id需要和for的值保持一样
		<label for="woman">  label实现点击文字产生相同效果
		女：<input type="radio" name="sex" id="woman">
		</label>
	4.多选按钮
		请选择你喜欢的音乐：
		摇滚：<input type="checkbox">
		摇滚：<input type="checkbox">
		摇滚：<input type="checkbox">
	5.下拉框
		请选择你的学历：
		<select name="" id="">
			<option value="">学士</option>
			<option value="">学士</option>
			<option value="">学士</option>
		</select>
	6.文件
		请上传文件：<input type="file">
	6.隐藏域
		<input type="hidden">用户看不见，后台能获取
	7.文本域
		<textarea name="" id="" cols="30" rows="10"></textarea>
		textarea{
			resize:none;不允许用户拖动
			       vertical;只能在垂直方向拖动
			       horizontal; 只能在水平方向拖动
			       both;水平竖直方向均可以
			     }
     8.重置按钮
     	<input type="reset">
     9.提交按钮
     	<input type="submit">
 	10.自定义按钮
 		<input type="button" value="按钮">
 		<button>搜索</button>
 	11.颜色
 		<input type="color">
	12.时间日期
		年月：<input type="month">
		年周：<input type="week">
		时分：<input type="time">
		年月日：<input type="date">
		年月日时分：<input type="datetime-local">
	13.验证
		<input type="email">
		<input type="tel" autofocus>  autofocus自动获取焦点
	14.音频控件
		音频标签
      <audio src"文件路径" controls  loop  autoplay></audio>
      controls:控件向用户显示
      loop:循环播放
	  autoplay:当页面加载完毕后自动播放
		视频标签
      <vidio src="" controls loop autoplay></vidio>
 </form>
	
	16.h5语义化标签  块标签
		<header>头部</header>
		<nav>导航</nav>
		<aside>侧导航</aside>
		<section>页面中的某一个部分</section>
		<main>主体</main>
		<footer>底部·</footer>
获取表单的值
obj.value  //重置的话将他赋为空字符串

~~~

## 动画

~~~css
第一步：定义动画规则
@keyframes   animation1{ 动画样式}     animation1为动画规则名字    @keyframes为关键字
样式
@keyframes   animation1｛
	from{
		
		   } （不写默认为初样式）
		   to{
		   
		   }    从某个样式到另一个样式
｝
@keyframes   animation1｛
	0%｛
	
	｝
	50%｛
	
	｝
	100%｛
	
	｝
｝
 第二步：挂载动画
 animation: 动画规则名字   1s  ease时间函数  0.5s延迟;              类似过渡
 animation-direction:alternate/normal;   指定下一次动画是否为逆向     
 animation-fill-mode:backwards;     动画后保持一开始状态
                                 forwards;        动画后保持当前状态
 animation-play-state:paused;          停止动画
                                  running;          运行动画
animation-duration:  1s;    时间
animation-iteration-count:  次数；   infinite无限次
animation-timing-function:linear 匀速;   定义时间函数
animation-delay:0s;    定义延迟
指定动画分几步完成steps
~~~

<a href="" title="天气"  target="_blank"></a>

		target:用来控制新页面打开的位置
				_self:在本窗口打开（默认值）
				_blank:在新窗口打开
caniuse:查询各个浏览器对属性的支持情况。（兼容表）

**去掉table里面的边框**：border-collapse: collapse;

去掉a链接的下划线：text-decoration：none；

将div设可编辑属性：contenteditable

letter-spaces  增加字间距