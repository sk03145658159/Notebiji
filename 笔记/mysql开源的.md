# 关系型数据库 (IDMS）  mysql（开源的）端口为3306

navicat数据库应用链接软件

有条理的，快速的处理数据

向数据库中存入数据：命令行、软件、程序存入数据

### 架构  

c/s架构    依赖于下载客户端

b/s架构    不依赖于客户端，在浏览器中实现

### 安装

windows中命令行启动数据库

找到mysql安装目录下的bin目录   C:\Program Files\MySQL\MySQL Server 8.0\bin

mysql   -uroot  -p     (mysql -uyueyingjun -p)

//net start mysql  开始运行

//net stop mysql  停止运行

## 命令

### 数据库的基本操作

 sql语句中#和--空格表示注释

SQL注入  uname=""or 1=1;-- "and upass="12234444"

mysql   -uroot  -p  进入数据库  （-h(localhost本地地址)，-u(username用户名)，-p(password密码)）  -P服务器端mysql端口号  -D数据库名

show databases;  查看里边的库

create database 名字;   创建库

use 库名;   选择用的库

show tables;  查看库中的表

create table stu表名(        **创建表 **                      create table if not exists user

id  int(10)   auto_increment(自增)  primary key(主键),

name  varchar(255),

age varchar(10),

sex  varchar(10)

)default charset=utf8;

###  **对列进行增删改查**

#### 　　- 14.1  增加一列

#### 　　　　- alter table tablename add 列名 数据类型   [first|after已有列   定义添加的位置]

#### 　　- 14.2  删除一列

#### 　　　　- alter table tablename drop column 列名

#### 　　- 14.3 修改列的数据类型

#### 　　　　- alter table tablename modify 列名 数据类型

#### 　　-14.4 修改列的数据类型并且改名

#### 　　　　- alter table tablename change old_colname new_colname 数据类型

****desc 表名;   查看表的结构****

insert into 表名 (name,sex,age) values('张三','男','20')    向表中插入内容

（insert into stu (name,sex,age) values('%s','%s','%s')%(name,sex,age)/insert into stu (name,sex,age) values(%s,%s,%s),(name,sex,age)）第二种方法安全，mysql自动提供的删选功能

select * from 表名;        查看表的内容

select * from stu where name="" and password=""

select * from stu where name is null       |    select * from stu where name is not null

update stu(表名) set sex='女'  where id=1；  更改表的内容

delete from stu(表名) where id=1;    删除表的内容

drop table tablename表名        删除表

drop database 库名;     删除库



truncate table 表名;   清空表中的内容   （id会重置）

​	不带where参数的delete语句可以删除mysql表中所有内容，使用truncate table也可以					清空mysql表中所有内容。效率上truncate比delete快，但truncate删除后不记录mysql日志，不可以恢复数据。delete的效果有点像将mysql表中所有记录一条一条删除到删完，而truncate相当于保留mysql表的结构，重新创建了这个表，所有的状态都相当于新表。



pip uninstalled 包名    利用pip下载包

### 创建虚拟环境·：

在终端执行以下口令

python3 -m  venv  abc名字

cd abc名字

cd bin

source ./activate

利用pip下载flask，pymysql等包

#### 步骤

安装pip（官网源码安装）

创建虚拟环境

在终端执行以下口令

python3 -m  venv  abc名字

cd abc名字

cd bin

source ./activate

sudo apt-get install python3.4-venv(安装使python)

升级pip版本pip install -U pip



**退出虚拟环境**：deactivate



**问题：python包的上传**

**虚拟文件的创建**

**客服端的创建**

### ajax(async(异步) javascript and xml(数据))    MDN查看相关知识

**ajax产生的原由**：

​	架构  

​	c/s架构    依赖于下载客户端，更新不及时（不基于网络，操作流畅）

​	b/s架构    不依赖于客户端，在浏览器中实现，可以随时访问最新的内容，免去用户的下载（基于网络，会有					延迟，不能够流畅的操作，体验性不好）

ajax结合了这两点。

**ajax要解决的问题：**

​	1.页面无刷新操作数据

​	2.按需获取的问题

​	3.让基于b/s架构的软件能够同基于c/s架构的软件，操作流畅

var ajax=new XML HttpRequest()    定义ajax对象，让他去进行操作

ajax.onr eadystatechange=function(){     当ajax对象状态发生改变时执行的语句

​	if(ajax.readyState==4)   ajax.readState  1接到要求  2出发  3找到地址 4取到数据

​	if(ajax.state==200)    200--节点任务成功完成

}

```py
ajax.onload=function(){   等同于上面的语句（监听）
  ajax.response   获取的内容
}
```

ajax.open('post/get','2.html')   #到哪调取，以什么方式取    取数据的方式：get、post    open(方式，地址，同步/异步(true/false),服务器的用户名和密码)后两个参数一般不写

ajax.send()  可以去了



### 注意的问题

#### ajax的返回值：

ajax的返回值： document   text  json  blod(二进制)   ....(默认text)          ajax.responseType='document'控制类型

#### ajax中post 与 get传递的区别

post传递数据

​	ajax.open('post','/')

​	ajax.setRequestHeader('content-type','application/x-www-form-urlencoded')   指定内容传递类型

​	ajax.send('name=zhangsan')   在此处传数据

get传递数据

​	ajax.open('get','/?name=zhangsan&sex=nan')  通过地址栏传递  ?+{name:name,age:age}

​	ajax.send( )



#### ajax的封装函数

```py
function ajax(parames) {
        if (typeof (parames)!='object'){
            console.error('参数错误')
            return;
        }
        //参数初始化
        let type = parames.type || 'get'
        let url = parames.url
        if (url==''){
            console.error('输入操作地址')
            return;
        }
        let gettype = parames.gettype || 'text'
        let date = parames.date || ''
        let atr1=''
        if (typeof date=='object'){
            for(let i in date){
                atr1+=i+'='+date[i]+'&'
            }
        }
        date=atr1.slice(0,-1)
        // }else{
        //     date=parames.date
        // }
        let ajax = new XMLHttpRequest()
        ajax.responseType = gettype
        ajax.onload = function () {
            parames.success(ajax.response)


        }
        if (type == 'get') {
                ajax.open(type, url + '?' + date)
                ajax.send()
            } else if (type == 'post') {
                ajax.open(type, url)
                ajax.setRequestHeader('content-type', 'application/x-www-form-urlencoded')
                ajax.send(date)
            }
    }
    引用
    ajax({
       ajax({
        url:'/select',
        gettype:'json',
        success:function(date){     date为获取的结果，也就是response
            for(var i=0;i<date.length;i++){
                let tr=document.createElement('tr')
                let atr=`<td class="aa">${date[i].id}</td><td>${date[i].name}</td><td>${date[i].sex}</td><td>${date[i].age}</td><td class="aa"><button type="submit" class="remove">删除</button></td>`
                tr.innerHTML=atr
                table.childNodes[1].appendChild(tr)
            }
        }
    })
    })
```

向数据库中导入sql文件：source  path(文件位置 )

fetch同ajax,可实现相同的功能

```js
fetch("2.html").then(function(e){
  return e.text()
}).then(function(e){
  console.log(e)
})
```



**ajax，fetch不被允许跨域访问（浏览器不允许，限制，因为安全）**跨域的安全限制都是对浏览器端来说的，服务器端是不存在跨域安全限制的。

#### 解决跨域问题

- [ ] **jsonp      快捷一点，访问速度快，诸多限制（要求两个服务器都能由你自己编写代码或者需要两方配合）**

      原理：script可以跨域，script拿到的东西都当作js解析执行（与后缀名无关，内容是js即可解析，不是则不会报错，但无法解析）

      JSONP是一种使用JSON数据的方式，返回的不是JSON对象，是包含JSON对象的javaScript脚本。

      应用：jquery


      ```py
      //sk1.html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <div></div>
      </body>
      </html>
      <script>
          function bb(val) {
              document.querySelector("div").innerHTML = val
          }
      </script>
      <script src="http://127.0.0.1:8585/aaa?fn=bb"></script>
      //sk2.py
      from flask import Flask,render_template,request;
      app=Flask(__name__)
      @app.route("/")
      def index():
          return render_template("sk1.html")
      app.run()
      //sk3.py
      from flask import Flask,render_template,request;
      app=Flask(__name__)
      @app.route("/aaa")
      def aaa():
          fn=request.args.get("fn")
          print(fn)
          return fn+"('ccc')"
      app.run(port="8585")


      jquery实现??????????????????????????????????????
      //sk1.html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <div></div>
      </body>
      </html>
      <script src="/static/jquery-3.2.1.js"></script>
      <script>
          function sk(val) {
              document.querySelector("div").innerHTML = val
          }
          $.ajax({
              url:"http://127.0.0.1:8585/aaa",
              dataType:"jsonp",
              callback:"sk",
              success(e){
                  console.log(e)
              }
          })
      </script>
      <script src="http://127.0.0.1:8585/aaa?fn=bb"></script>
      //sk2.py
      from flask import Flask,render_template,request;
      app=Flask(__name__)
      @app.route("/")
      def index():
          return render_template("sk1.html")
      app.run()
      //sk3.py
      from flask import Flask,render_template,request;
      app=Flask(__name__)
      @app.route("/aaa")
      def aaa():
          return "sk('ccc')"
      app.run(port="8585")
      ```
    
      ​

- [ ] **代理        流程比较复杂，效率慢，开发慢，几乎没有限制（python构建为一个客户端代理去访问** ）

      原理：puthon具有客户端的能力

      应用：爬虫、动态跨域获取信息

      ```
      //sk1.html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <div></div>
      </body>
      </html>
      <script src="/static/jquery-3.2.1.js"></script>
      <script>
         var ajax=new XMLHttpRequest()
         ajax.onload=function(){
             console.log(ajax.response)
         }
          ajax.open("get","/ajax?url=http://www.sxuek.com/")
          ajax.send()
      </script>
      //sk2.py
      from flask import Flask,render_template,request as request1
      from urllib import request
      app=Flask(__name__)
      @app.route("/")
      def index():
          return render_template("sk1.html")
      @app.route("/ajax")
      def index1():
          url=request1.args.get("url")   #获取地址
          res=request.urlopen(url)       #通过地址打开目标返回一个http.client.HTTPResponse对象
          con=res.read().decode("utf8")  #.red读取里边的内容，内容为未解码   .decode解码
          return con

      app.run()
      //sk3.py
      from flask import Flask,render_template,request;
      app=Flask(__name__)
      @app.route("/aaa")
      def aaa():
          return "ccc"
      app.run(port="8585")
      ```

      ```py
      vue开发环境中，利用ajax跨域连接数据库，从数据库中导出数据
      //home.vue
      <template>
        <div class="container">
          <table class="table table-bordered">
            <tr>
              <th>id</th>
              <th>name</th>
              <th>sex</th>
              <th>age</th>
              <th>编辑</th>
            </tr>
            <tr v-for="item in datas">
              <td>{{item.id}}</td>
              <td>{{item.name}}</td>
              <td>{{item.sex}}</td>
              <td>{{item.age}}</td>
              <td><router-link :to="'/change?id='+item.id"><input type="button" value="编辑"></router-link><input type="button" value="删除"></td>
            </tr>
          </table>
        </div>
      </template>
      <script>
        export default {
             name:"home",
            data(){
            return{
                  datas:[]
            }
        },
        mounted(){   //生命周期函数，在渲染也面前调用数据

              var ajax=new XMLHttpRequest()
              ajax.onload=()=>{
                  this.datas=JSON.parse(ajax.response)
              }
              ajax.open("get","/ajax/select")
              ajax.send()
      ```


        }
      }
      </script>
      <style>
    
      </style>
      //vue.config.js
      module.exports = {
        devServer: {
          proxy: {
            '/ajax': {      //出现ajax就产生配置
              target: 'http://localhost:5000',   //跨域访问的地址
              ws: true,
              changeOrigin: true
            },
        }
      }
      }
      //serve  利用python导出数据库数据
      from flask import Flask
      import pymysql
      import json
      app=Flask(__name__)
      @app.route("/ajax/select")
      def select():
          db= pymysql.connect(host='localhost',
                                   user='root',
                                   password='03145658159shen',
                                   db='stu',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
          cursor=db.cursor()
          cursor.execute("select * from stu")
          result=cursor.fetchall()
          return json.dumps(result)
      app.run()  
      ```
    
      ​



### 函数

地址、方式、返回的类型、传递的数据、





seo搜索引擎优化



### 业务逻辑（开发方式）

一.放在服务器

- 优点
  - [ ] 业务逻辑清晰
  - [ ] 人的工作量少
  - [ ] 首页加载速度快
- 缺点
  - [ ] 用户体验差
  - [ ] 服务器压力大
  - [ ] 不利于协同工作

二.ajax

-  优点
  - [ ] 用户的体验比较流畅
  - [ ] 减轻服务器的压力
  - [ ] 有利于协同工作
-  缺点
  - [ ] 业务逻辑不清晰
  - [ ] 人的工作量大

三.mvvm  model--模型---数据   view---视图--模板---html和css

​     数据到试图   视图到数据   双向数据绑定

​     框架代表：angular和vue外哦（基于nodejs）



uri资源的定位方式，其中url为最常用的一种（地址的方式）

tcp/ip 协议：http，https....

协议://【用户名:密码@】主机：端口/路径/文件名？查询字符串#锚链接（很少有？和锚链接同时出现）

#### 锚链接：实现页面不跳转，形成历史纪录，不向服务器发送请求，在本地找资源

​	**进行本地资源定位，不会向服务器发送请求**

​	<a href="#one"></a>  <a name="one"></a>

js中操作地址location（location.href获取操作地址，location.hash获取锚链接值）

ajax和锚链接结合起来实现路由原理

```py
<script>
    var hash=location.hash.slice(1)
    if(hash){
        var ajax=new XMLHttpRequest();
        ajax.onload=function(){
            
            let div=document.querySelector("div")
            div.innerHTML=ajax.response
        }
        ajax.open("get",hash+".html")
        ajax.send()
    }
    let but=document.querySelector("button")
    but.onclick=function(){
         var ajax=new XMLHttpRequest();
        ajax.onload=function(){
            
            let div=document.querySelector("div")
            div.innerHTML=ajax.response
            location.href=location.href+"#1"
        }
        ajax.open("get","1.html")
        ajax.send()
    }
   

</script>
```



路由：控制器                       m(数据模型)v(视图)c(控制器)      mvvm前端框架

vue中route是局部的路由，router是全局路由

用this.$router.push("/")实现页面跳转

var id=this.$route.query.id       vue文件中获取传递的数据

**关联查询  **

select * from user,role where user.rid=role.rid  所有关联的

select * from user inner join role on  user.rid=role.rid  交集（所有关联的）

select * from user left join  role on  user.rid=role.rid   以左表为主（user），除了关联的，还有左表未关联的

select * from user right join  role on  user.rid=role.rid   以右表为主（role），除了关联的，还有右表未关联的

GROUP BY cname  分组    Group_concat(step)



**flask中后台获取列表 arr=request.args.getlist()**

**数据库值可以存储字符串 ，将列表转化成字符串  tring.join(seq) 将列表(string)对象用string进行分隔组合为字符串    arr=[1,2,3,4]    =>   ",".join(arr)**

### 子查询和分页

select * from logs where id in (1,2,3)  枚举
select * from logs where phone in (select phone from student where classid in (select id from classes where fid in (9课程方向))) 子查询
课程方向=》班级=》学生
date.format(login.time,"%Y-%m-%d")  mysql的一个语句，将时间对象格式化为一种形式
select logs.*,stu.name as sname,classes.name as cname from logs left join stu on logs.phone=stu.phone left join classes on stu.classid=classes.id where logs.phone in (select phone from stu where classid in (select id from classes where fid in (10)) and date_format(logs.time,"%Y-%m-%d")="2018-11-11") limit  0,5  limit分页处理，从哪个位置取几条，		

```py
分页处理
if request.url.find("?")<0:
        url=request.url+"?page="
    else:
        if request.url.rfind("page")<0:
            url=request.url+"&page="
        else:
            url=request.url[0:request.url.rfind("=")+1]
    currentpage=int(request.args.get("page") or 0)
    pageNums=math.ceil(total/pageNum)
    pagestr=""
    pagestr+="共%s页"%(pageNums)
    pagestr+="<a href='%s'>首页</a>"%(url+"0")
    last=currentpage-1 if currentpage-1>0 else 0
    pagestr+="<a href='%s'>上一页</a>" %(url+str(last))
    start=currentpage-2 if currentpage-2>0 else 0
    end=currentpage+2 if currentpage+2>pageNums else pageNums
    for item in range(start,end):
        if(currentpage==item):
            pagestr+="<a href='%s' style='color:red'>[%s]</a>"%(url+str(item),item+1)
        else:
            pagestr += "<a href='%s'>[%s]</a>" % (url + str(item), item + 1)
    next=currentpage+1 if currentpage+1<pageNums else pageNums-1
    pagestr+="<a href='%s'>下一页</a>" %(url+str(next))
    pagestr += "<a href='%s'>尾页</a>" % (url + str(pageNums-1))
    return pagestr
```

### DCL(Database Controll Language)数据控制语言

用来设置或更改数据库用户、角色权限

#### 访问控制和权限

#### 当客户端连接到服务器时，mysql访问控制有两个阶段

连接验证：验证用户名和密码

请求验证：验证权限

#### 安装完MySOL后MySQL库默认表

- user表：包含用户账户和全局权限列
- db表
- table_priv和columns_priv表

#### 创建用户

create user 账户名字(username@hostname) identified by 'password'     

其中：账户名字@作用域名地址

例：create user yueyingjun@localhost identified by ‘123456’  

username@%  任何域名下都可访问到，或者（-）

username@%.baidu.com

#### 删除用户

drop user username@hostname

也可以在默认用户表中删除

#### 查看用户权限

1.show grants for yueyingjun@localhost

2.在默认的user表中查看

#### 设置权限

一：

grant  权限名1,权限名2,..   on  库名/库名.表名   to   username(yueyingjun@localhost)   With grant option;

with grant option   别人可以更改你的权限

grant指定被赋予的权限   grant all  privileges赋予全部权限

grant  select,update,delete on alibaba.*   to  rfc With grant option;;

二：

在默认的user表中修改

#### 允许远程链接

一：

grant  all  privileges on * . * to "root"@"%"  identified by 'mysql' with grant option;

flush privileges;   ----刷新权限

二：

在默认的user表中修改

#### 删除权限REVOKE

一：

REVOKE  权限名1,权限名2,..   on    库名/库名.表名   FROM   user

REVOKE  all  privileges  on  库名/库名.表名   FROM   user

二：

在默认的user表中修改

#### 修改密码

- use mysql

  updata  user set password=“123”  where  user=username  and   host="localhost"

- set password for 用户名@localhost = '新密码';

- **mysqladmin** -u用户名 -p旧密码  password 新密码

- 在忘记root密码或者初始密码

  - [ ] 关闭正在运行的maysql
  - [ ] 打开dos窗口，转到mysql\bin目录
  - [ ] 输入mysql  --skip-grant-tables  跳过权限检查
  - [ ] 再打开一个dos窗口，转到mysql\bin目录
  - [ ] 输入mysql回车
  - [ ] 链接权限数据库：use  mysql
  - [ ] 改密码  update user set password("123") where user="root";
  - [ ] 刷新权限  flush privileges;
  - [ ] quit 退出
  - [ ] 注销，重启电脑

#### 数据库备份

##### mysqldump命令

```my
mysqldump -u[username] -p[password] [database_name] > [dump_file.sql]     >为重定向
仅备份mysql数据库结构
mysqldump -u[username] -p[password] --no-data [database_name] > [dump_file.sql]  
仅备份mysql数据库数据
mysqldump -u[username] -p[password] --no-create-info [database_name] > [dump_file.sql]  
导出多个数据库
所有库
mysqldump -u[username] -p[password] --all-database [database_name] > [dump_file.sql] 
指定那几个库
mysqldump -u[username] -p[password] [dbname1,dbname2...] [database_name] > [dump_file.sql]  
```

#### 查看表

show tables

show full tables

#### 查看表中的字段，列

desc 表名

show columns from 表名

show columns from 表名 like "id"   查看某个字段

show columns from 表名  where  

#### 查看用户信息

use mysql

select user from user   查看所有用户

select user()   查看当前用户

select     查看正在登陆用户的信息

​	user,

​	host,

​	db,

​	command

​	form

​	information_schema.processlist

#### 数据库维护（过程中会对表加一个只读锁，锁住）    ！重要

- 分析表语句

  分析索引并修正

  ANALYZE TABLE  表名1[,表名2..]

- 优化表语句

  优化插入、删除产生的碎片

  OPTIMIZE TABLE 表名

- 检查表

  CHECK TABLE table_name表名

  只检查不管修复，需执行下面的修复语句

- 修复表语句（尝试性修复，不一定修复好）

  PEPAIR TABLE 表名

### DDL（Data Definition Language）数据定义语言

#### 创建数据库

CREATE  DATABASE  IF NOT EXISTS  database_name库名

#### 删除数据库

DROP DATABASE IF EXISTS database_name

#### 创建表

```my
CREATE TABLE [IF NOT EXISTS] table_name(
列名   属性(长度)   [NOT NULL|NULL是否为空]  [auto_increment自增]  [None什么都没有,不占位置]  
                    [default默认值] [UNIQUE索引,唯一的]
)ENGINE=InnoDB引擎 DEFAULT CHARSET=utf8可识别中文 comment='xxx'注释;

其中int(11)显示宽度
sex ENUM('男','女') not null 定义枚举类型，只能是男或女，当插入不传sex值时，默认为男。当插入传sex值但不为男或女时，值为None。与set的区别是，一个为枚举单选，一个为集合多选
例子：
create table if not exists user_table(
    -> id int(11) auto_increment,
    -> name varchar(20) default null,
    -> phone varchar(11) unique,
    -> aihao set('睡觉','打游戏')    set设置默认选项    ENUM("0","1","2")default '2' 定义枚举类型
    	primary key(id)
    -> )default charset=utf8 comment='用户表';
show create table table_name;  查看建好的表
```

#### 修改表

```my
队列的各种修改见上面
添加主键
ALTER TABLE table_name primary key(id)
删除主键
alter table user drop
添加唯一索引
ALTER TABLE 'table_name' ADD UNIQUE('column')
添加全文索引
ALTER TABLE 'table_name' ADD FULLTAXT('column')
添加普通索引
ALTER TABLE 'table_name' ADD INDEX('column')
删除索引
ALTER TABLE 'table_name' drop index 列名
修改引擎
ALTER TABLE my_table ENGINE=InnoDB
show ENGINEs   查看mysql支持的所有引擎
show create table 表名
修改自增值
alter TABLE tablename auto_increment=1
```

#### 数据类型（具体见书签）

主要包括以下五大类：

整数类型：BIT、BOOL、TINY INT、SMALL INT、MEDIUM INT、 INT、 BIG INT

浮点数类型：FLOAT、DOUBLE、DECIMAL

字符串类型：CHAR、VARCHAR、TINY TEXT、TEXT、MEDIUM TEXT、LONGTEXT、TINY BLOB、BLOB、MEDIUM BLOB、LONG BLOB

日期类型：Date、DateTime、TimeStamp、Time、Year

其他数据类型：BINARY、VARBINARY、ENUM、SET、Geometry、Point、MultiPoint、LineString、MultiLineString、Polygon、GeometryCollection等

#### 数值类型

UNSIGNED无符号(默认有符号)

int(11)表示显示宽度而不是数值范围，数值范围由int决定

zerofill定义用0将显示宽度补齐   

有符号和无符号的范围区别:因为需要有一位来表示符号。  

| MySQL数据类型    | 含义（有符号）                                  |
| ------------ | ---------------------------------------- |
| tinyint(m)   | 1个字节  范围(-128~127)    -127~128(有正负号）   0~255(无符号) |
| smallint(m)  | 2个字节  范围(-32768~32767)                   |
| mediumint(m) | 3个字节  范围(-8388608~8388607)               |
| int(m)       | 4个字节  范围(-2147483648~2147483647)         |
| bigint(m)    | 8个字节  范围(+-9.22*10的18次方)                 |
| float(m,d)   | 单精度浮点型    8位精度(4字节)     m总个数，d小数位        |
| double(m,d)  | 双精度浮点型    16位精度(8字节)    m总个数，d小数位        |

设一个字段定义为float(6,3)，如果插入一个数123.45678,实际数据库里存的是123.457，但总个数还以实际为准，即6位。整数部分最大是3位，如果插入数12.123456，存储的是12.1234，如果插入12.12，存储的是12.1200.

##### 字符串类型

除了CHAR为定长，其他全为变长

CHAR  0~255字节   定长字符串(长度确定255，不可变）  读取速度快,小数据浪费

VARCHAR   0~65535字节  变长字符串    读取速度慢        varchar(20)规定最大存储字节

TEXT   0~65535字节   长文本数据

| MySQL数据类型  | 含义                 |
| ---------- | ------------------ |
| char(n)    | 固定长度，最多255个字符      |
| varchar(n) | 固定长度，最多65535个字符    |
| tinytext   | 可变长度，最多255个字符      |
| text       | 可变长度，最多65535个字符    |
| mediumtext | 可变长度，最多2的24次方-1个字符 |
| longtext   | 可变长度，最多2的32次方-1个字符 |

char和varchar：

1.char(n) 若存入字符数小于n，则以空格补于其后，查询之时再将空格去掉。所以char类型存储的字符串末尾不能有空格，varchar不限于此。 

2.char(n) 固定长度，char(4)不管是存入几个字符，都将占用4个字节，varchar是存入的实际字符数+1个字节（n<=255）或2个字节(n>255)，

所以varchar(4),存入3个字符将占用4个字节。 

3.char类型的字符串检索速度要比varchar类型的快。
varchar和text： 

1.varchar可指定n，text不能指定，内部存储varchar是存入的实际字符数+1个字节（n<=255）或2个字节(n>255)，text是实际字符数+2个字

节。 

2.text类型不能有默认值。 

3.varchar可直接创建索引，text创建索引要指定前多少个字符。varchar查询速度快于text,在都创建索引的情况下，text的索引似乎不起作用。

##### 日期类型

DATE  3字节  

TIME   3字节

DATETIME

TIMESTEMP

| MySQL数据类型 | 含义                        |
| --------- | ------------------------- |
| date      | 日期 '2008-12-2'            |
| time      | 时间 '12:25:36'             |
| datetime  | 日期时间 '2008-12-2 22:06:44' |
| timestamp | 自动存储记录修改时间                |

##### 空间数据类型

#### 引擎类型

show engines查看数据库中的引擎

##### MyISAM

它不支持事务，也不支持外键，尤其是访问速度快。

每个MyISAM存储三个文件

- .frm(存储表结构)
- .MYD(存储数据)
- .MYI(存储索引)

##### InnoDB

它是一个健壮的事务型存储引擎

每个InnoDB存储两个文件

.frm（存储表结构）

.ibd（存放索引）

.ibdata(存放数据)

#### 索引类型

目的：使查询更加快速

##### 主键索引 primary

一个表中只能有一个·

主键的值只能是唯一的，不能重复，auto_increment

##### 唯一键 unique

一个表中能够给多个字段设置唯一键

在本字段当中不能出现相同的内容，出了null除外

##### 普通的索引 index

一个表中能够多个字段设置普通索引，他会在查询本字段

##### 文本索引 fulltext         mysql5.7版本后有效

文本编辑器

快速的在大批文本当中，有序查找内容

##### 外键

使两个表发生关联

定义：一个副表的非主键字段和主表的主键字段发生关联

外键的默认作用有两点：

​      1.对子表(外键所在的表)的作用：子表在进行写操作的时候，如果外键字段在父表中找不到对应的匹配，操作就                会失败。

​      2.对父表的作用：对父表的主键字段进行删和改时，如果对应的主键在子表中被引用，操作就会失败。

外键的定制作用----三种约束模式：

​      district：严格模式(默认), 父表不能删除或更新一个被子表引用的记录。

​      cascade：级联模式, 父表操作后，子表关联的数据也跟着一起操作。

​      set null：置空模式,前提外键字段允许为NLL,  父表操作后，子表对应的字段被置空。

使用外键的前提：

​      1. 表储存引擎必须是innodb，否则创建的外键无约束效果。

​      2. 外键的列类型必须与父表的主键类型完全一致。

​      3. 外键的名字不能重复。

​      4. 已经存在数据的字段被设为外键时，必须保证字段中的数据与父表的主键数据对应起来。

在副表中设置：

[CONSTRAINT  constraint_name约束名字]

FOREIGN KEY [foreign_key_name外键名字]  (columns副表字段) REFERENCES  tablename主表名字  (column主表字段) 

```my
 create table if not exists student(
    -> id int(10) auto_increment primary key,
    -> sname varchar(20),
    -> cid int(10),
    -> constraint aaa foreign key bbb (cid) references classes (id)
    -> )default charset=utf8;
```

### DML（Manipulation）数据操作语言。

增、删、改

### DQL（Data Query Language）数据库查询语言

### TCL事务控制语言

### 数据库锁

### 主从配置

### 数据库优化操作