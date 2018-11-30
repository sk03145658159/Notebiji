# python

## turtle 海龟画图模块

```py
import turtle   导入turtle模块
turtle.showturtle()   显示箭头
turtle.color('red')  调颜色
turtle.width(10)   调粗细
turtle.write('沈括')  写字符串
turtle.forward(300)  前进300像素
turtle.left(90)  箭头左转90度  right右转
turtle.goto(0,50) 去坐标（0，50）
turtle.penup()  抬笔，这样路径就不会画出来
turtle.pendown()  下笔，这样路径就会画出来
turtle.circle(100)  画圆，设置半径大小
(1)画笔运动命令
turtle.forward(distance)
向当前画笔方向移动distance像素长度
turtle.backward(distance)
向当前画笔相反方向移动distance像素长度
turtle.right(degree)
顺时针移动degree°
turtle.left(degree)
逆时针移动degree°
turtle.pendown()
移动时绘制图形，缺省时也为绘制
turtle.goto(x,y)
将画笔移动到坐标为x,y的位置
turtle.penup()
提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.circle()
画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
setx( )
将当前x轴移动到指定位置
sety( )
将当前y轴移动到指定位置
setheading(angle)
设置当前朝向为angle角度
home()
设置当前画笔位置为原点，朝向东。
dot(r)
绘制一个指定直径和颜色的圆点

(2) 画笔控制命令
turtle.fillcolor(colorstring)
绘制图形的填充颜色
turtle.color(color1, color2)
同时设置pencolor=color1, fillcolor=color2
turtle.filling()
返回当前是否在填充状态
turtle.begin_fill()
准备开始填充图形
turtle.end_fill()
填充完成
turtle.hideturtle()
隐藏画笔的turtle形状
turtle.showturtle()
显示画笔的turtle形状

(3) 全局控制命令
turtle.clear()
清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()
清空窗口，重置turtle状态为起始状态
turtle.undo()
撤销上一个turtle动作
turtle.isvisible()
返回当前turtle是否可见
stamp()
复制当前图形
turtle.write(s [,font=("font-name",font_size,"font_type")])
写文本，s为文本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项

(4) 其他命令
turtle.mainloop()或turtle.done()
启动事件循环 -调用Tkinter的mainloop函数。
必须是乌龟图形程序中的最后一个语句。
turtle.mode(mode=None)
设置乌龟模式（“standard”，“logo”或“world”）并执行重置。如果没有给出模式，则返回当前模式。
模式
初始龟标题
正角度
standard
向右（东）
逆时针
logo
向上（北）
顺时针
turtle.delay(delay=None)
设置或返回以毫秒为单位的绘图延迟。
turtle.begin_poly()
开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
turtle.end_poly()
停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
turtle.get_poly()
返回最后记录的多边形。

3.命令详解
3.1turtle.circle(radius,extent=None,steps=None)
描述：以给定半径画圆
参数：
radius(半径)：半径为正(负)，表示圆心在画笔的左边(右边)画圆；
extent(弧度)(optional)；
steps(optional)(做半径为radius的圆的内切正多边形，多边形边数为steps)。
举例:
circle(50)#整圆;
circle(50,steps=3)#三角形;
circle(120,180)#半圆
```

### python中的json模块

- 1、json字符串转为字典

  json.load / json.loads

  两个方法功能类似，可选参数也相同，最大的区别在于，json.load方法接受的输入，即第一个参数，是包含json数据的文件对象，如open方法的返回对象，

  json.loads接受的输入是json字符串，而非文件对象。从输入类型的区别也可以看出两者的使用场合。

- 2、字典转换为json

  json.dump / json.dumps

  对应于load和loads，dump的第一个参数是对象字典，第二个参数是文件对象，可以直接将转换后的json数据写入文件，dumps的第一个参数是对象字典，其余都是可选参数。dump和dumps的可选参数相同，这些参数都相当实用，现将用到的参数记录如下：

  ensure_ascii 默认为True，保证转换后的json字符串中全部是ascii字符，非ascii字符都会被转义。如果数据中存在中文或其他非ascii字符，最好将ensure_ascii设置为False，保证输出结果正常。

  indent 缩进，默认为None，没有缩进，设置为正整数时，输出的格式将按照indent指定的半角空格数缩进，相当实用。

  separators 设置分隔符，默认的分隔符是(',', ': ')，如果需要自定义json中的分隔符，例如调整冒号前后的空格数，可以按照(item_separator, key_separator)的形式设置。

  sort_keys 默认为False，设为True时，输出结果将按照字典中的key排序。

python中的pillow模块，python中处理图片的插件