## nodejs  ------- less

### 安装步骤：

- 安装nodejs（下载.msi)

- node -v   查看node下载

- npm -v 

- npm install -g less

- 在pycharm中配置

  打开pycharm --> settings

  file watchers

  点击  +

  点击 less

  programe --> node安装目录    where node查看路径

  params -->lessc的安装路径  c://user/admin/

- 在Visual Studio code 中配置

  直接在Visual Studio code 中扩展easy less 插件

### 变量

不分数据类型

@ 变量名 :  值

@color=red；

### 函数

. 函数名（）{}

```le
@color:red;   变量
@width:200px;
@height:200px;
div{
  width:@width;  变量的调用
  height:@height;
  border:1px solid @color;
  .shadow(10px,10px,100px,red,2)   函数的引用
}
.shadow(@x:0,@y:0,@s:100px,@c:#000,@type:1) when (@type=1){       函数（流程控制）
  box-shadow:@x @y @s @c;
}
.shadow(@x:0,@y:0,@s:100px,@c:#000,@type:1) when (@type=2){
  box-shadow:@x @y @s @c inset;
}
利用循环结构实现12栅格化
@cols:12;    
.a(@i:1) when (@i<=@cols){   循环结构
  .col-m-@{i}{
    width:@i/@cols*100%;
  }
  .a(@i:@i+1)
}
.a()
```

**固定布局**：width：200px；

**流式布局**：width：100%；  

用require引用包

nodejs中有path包，处理路径