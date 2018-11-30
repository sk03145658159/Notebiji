## mvc和mvvm架构

### mvvm基于mvc   m---model数据      v---view视图    C控制器

### mvvm 在mvc的基础上实现了双数据绑定

mvvm  model--模型---数据   view---视图--模板---html和css

数据到试图   视图到数据   **双向数据绑定**（数据和视图一个改变均改变）

框架代表：angular和vue外哦（基于nodejs）

#### Vue框架

缺点：首页加载速度慢，需要加载完所有所需文件，其后加载速度很快，不适合做大的页面

##### 引入vul.js文件

```vu
<div class="app">   在html中定义vul的作用范围块
    <input type="text" v-model="one">+<input type="text" v-model="two">=<span>{{one*1+two*1}}		</span>
     或者 <input type="text" v-model="one">+<input type="text" v-model="two">=<span                       v-text="one*1+two*1"></span>
    或者 <input type="text" v-model="one">+<input type="text" v-model="two">=<span>{{result()}}		</span>
     或者 <input type="text" v-model="one">+<input type="text" v-model="two">=<span                       v-text="result()"></span>
   <span v-text="three"></span>
</div>
<script>
    new Vue({    实例化vul对象
        el:".app",  确定作用范围
        data:{    为定义的属性赋值,json格式，表单内用v-model,表单外用{{}}(可以用v-text代替)
            one:0,   每个定义的属性都要赋值
            two:0,
            three:0
        }
        methods：{放逻辑部分，json格式（一个属性值改变，所有属性都会刷新一遍走一遍，效率差,当three值改变时，也会走一遍）
          result（）{
          	if(this.one>10){
               return this.one*1 + this.two*1
          	}else{
               return this.one*1 - this.two*1
          	}
          }
        }
         
         
         
       computed：{   放动态数据
          result（）{   不是方法，是动态数据，只有里面相关联的数据改变时才走一遍。当three值改变时，不会																					走一遍）
          	if(this.one>10){
               return this.one*1 + this.two*1
          	}else{
               return this.one*1 - this.two*1
          	}
          }
       }
       
       
       
       watch：{    自己监控属性值的变化，手动去监控某一个数据的变化(vul自动检测)
         one（after，before）{  参数before为修改前的值，after为修改后的值。
           console.log(111)
         }
       }
    })
     
     
    mounted（）{      生命周期函数，想要在页面渲染前就获取数据(当数据和视图绑定时执行，当多个路由使用一个视图时只执行一次，需要用watch自己监控)
      	ajax....
    }
</script>
<tr v-for="item in dates"> 循环
<input type="button" @click="result">点击事件
<input type="button" v-on:click="result">点击事件
<input type="button" @click="result($event)">返回事件对象
<div v-if="Math.random() > 0.5">   流程控制
  Now you see me
</div>
<div v-else>
  Now you don't
</div>
v-text
v-html
v-model：表单上的指定，目的是实现双向数据绑定
v-show
v-on=@
```

#### 自定义指令

```vu
 Vue.directive("focus",{   //自定义指令     focus自定义指令名
        inserted:function(ele,val){        inserted为指令发生的事件
            ele.focus()
        }
    })
自定义指令的调用v-focus    
    
    
// 注册
Vue.directive('my-directive', {
  bind: function () {},
  inserted: function () {},
  update: function () {},
  componentUpdated: function () {},
  unbind: function () {}
})

// 注册 (指令函数)
Vue.directive('my-directive', function () {
  // 这里将会被 `bind` 和 `update` 调用
})

// getter，返回已注册的指令
var myDirective = Vue.directive('my-directive')
```

#### 组件的制作  要有完整的结构、数据、逻辑

```vu
 Vue.component("car"函数名,{
        props:["dates"],接受参数(传参时传入列表型)         组件的制作,相当于函数
        template模板:`<div class="container">         template只能有一个根元素
        <table class="table table-bordered table-striped">
             <tr>
                <th>商品编号</th>
                <th>商品名称</th>
                <th>商品单价</th>
                <th>购买数量</th>
                <th>消费金额</th>
                <th>操作</th>
            </tr>
            <ul v-for="item in datas">
                <tr>
                    <td v-text="item.id"></td>
                    <td>{{item.name}}</td>
                    <td>{{item.grade}}</td>
                    <td>
                        <select class="form-control" v-model="item.num">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </td>
                    <td>{{item.grade*item.num}}</td>
                    <th><button class="btn btn-danger" type="button">删除</button></th>
                </tr>
            </ul>
            <tr>
                <td>商品总量：</td>
                <td></td>
                <td>消费总金额：</td>
                <td colspan="3"> </td>
            </tr>
        </table>
       
    </div>`,
    data(){    为函数格式
        return{
            datas:[
                {
                    id:1,
                    name:'安踏球鞋',
                    grade:260,
                    num:1
                },
                {
                    id:2,
                    name:'安踏球鞋',
                    grade:260,
                    num:1
                }
            ]}
        }
})
```

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div>zhangsan</div>
</body>
</html>
<script>
    //Vue实现双向绑定的核心原理
    var temp=""
    var obj={}
    Object.defineProperty(obj,'name',{  //定义对象属性的方法
        // value:100,
        // writable:true,   //可更改,可设置(不设置，默认为不可更改)
        configurable:true,  //可删除（不设置，默认为不可删除）
        enumerable:true, //可枚举，遍历（不设置，默认为不可枚举）
        set:function(val){  //为属性设置值，一设置马上调用
            if(temp!=val){
                document.querySelector("div").innerHTML=val;            //这两个函数不能和语句一二一起使用
            }
            temp=val
        },
        get:function(){  //获取属性的值，一获取就调用。  属性最后的值取决于temp
            return temp
        }
    })
    obj.name="zhangsan"
   console.log(obj.name)
   obj.name="lisi"
   console.log(obj.name)
</script>
```



努力是有目标的自觉奋斗，而忙碌是被别人毫无目地的拖着走

#### localStorage本地存储     （Application中）

localStorage.aa="bb"  /[1,2,3,4]/fubction/{}/[{}]          添加存储变量

localStorage.aa="cc"    修改

localStorage.setItem("aa","bb")          添加存储变量

localStorage.removeItem("aa","bb")    删除存储变量

localStorage.clear()  清楚所有数据

均已字符串的形式存储

- [ ] 存储是转换为字符串形式JSON.stringify()      js中转化为字符串
- [ ] 读取是转换会json格式JSON.parse()    js中转化成json格式
- [ ] json.loads        python中转化为json格式
- [ ] json.dumps()     python中转化为字符串

在ubuntu中首先下载nodejs，在官网中利用源码下载的方法得到下载源码链接=>将node和npm命令改成全局命令（找到命令位置与usr/bin/node|npm设置）=>在利用npm下载vue

vue是基于nodejs的，在安装vue之前要首先安装nodejs和npm

2.0vue版本的安装

npm install -g  vue-cli

vue-V

vue init  webpack aaaa

cd aaaa

npm run serve

sudo npm uninstall -g vue-cli  卸载

3.0vue版本

npm install -g  @vue/cli

vue create bbbbb创建开发环境

babel将es6语言=>es5,vuex处理数据,router路由(空格选择)

history：No

where do  you    ：  Y

选package.json 

地址栏锚链接显示    N

保存配置并命名   Y



cd aaaa    进入到创建的开发环境

npm run serve    运行开发环境

npm run build   开发完后将所有组件打包成一个html、css、js文件



首先为了解决跨域问题需要首先引入vue-config.js

vue中route是局部的路由，router是全局路由

$route为当前router跳转对象里面可以获取name、path、query、params等

$router为VueRouter实例，想要导航到不同URL，则使用$router.push方法

返回上一个history也是使用$router.go方法

用this.$router.push("/")实现页面跳转

var id=this.$route.query.id       vue文件中获取传递的数据

var id=this.$route.params.id

params相对应的是name（通过/传的值，router文件中路径后需加上:id）              query相对应的是path（通过？传的值）

**注意:params传参，push里面只能是 name:'xxxx',不能是path:'/xxx',因为params只能用name来引入路由，如果这里写成了path，接收参数页面会是undefined！！！**

##### **另外，二者还有点区别，直白的来说query相当于get请求，页面跳转的时候，可以在地址栏看到请求参数，而params相当于post请求，参数不会再地址栏中显示**



@contextmenu.prevent.stop=“aaaa($event) ”  右击事件，prevent组织浏览器默认行为,stop阻止冒泡行为  ,event确定事件源

在一个组件中引用另一个组件

    <template>
      <form1></form1>     组件的使用
    </template>
    
    <script>
    // import form1 from '@/views/add.vue'   引用组件
    export default {
       name:"add",
        // components:{form1:form1},   生明它为一个组件
        data(){
           return{
               name:"",
               sex:"",
               age:"",
           }

### 对应知识点见笔记mysql




Vue实现路由的步骤：1.定义组件2.定义路由对应的组件3.通过router配置参数注入路由

开发环境中的文件夹意义：src工作区间/assets存放资源|components存放组件|views存放大的组件|.gitignore上传git时，设定不必上传的内容|babel.config.js设定需要用babel将css语言转换的内容|package.json意义同python打包中的__ init __.py文件

####  饿了吗出的一套vue.js后台组件库，可以快速轻松的开发后台项目

vue中使用插件  Vue.use(插件名)

vue 写入插件

vh设置高度，占窗口高度的几份(默认平均分成100份)     !import（设置在样式后，表示最重要，优先级最高）

current() 函数返回数组中的当前元素的值。

insertid=str(db.insert_id())  获取当前插入数据的id

**Vuex管理组件之间的数据**，共享数据（vue的插件）

```js
在store.js中
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
       num:10             //放数据
  },
  mutations: {              //放方法
       setnum(state,val){
         this.state.num=val

       }
  },
  actions: {
            //异步更新的数据
  }
})
其他组件的引用方法
computed:{
           num(){
               return this.$store.state.num
           }
       }
其他组件的引用改变其值的方法
this.$store.commit('setnum',100)


<template>
  <div id="app">
    {{num}}<input type="button" value="确定" @click="sss">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>
<script>
  export default{
      methods:{
          sss(){
              alert(1)
              this.$store.commit('setnum',100)
          }
      },
      computed:{
          num(){
              return this.$store.state.num
          }
      }
  }
</script>
```

### 将后台的文件分开写

- 首先在新建文件

  from flask import  Blueprint

  head=Blueprint("head",__ name __)     

  @head.route("/addhead"）

  def  addhead(){}

- 然后在主文件中

  from url.head(新建文件位置user中的head文件)  import  head      引入

  app.register_blueprint(head,url_prefix="/ajax/head/")


### **在**vue开发框架中使用自定义组件

- 建一个js文件

  ```py
  建在assets文件中
  var obj=[]
  obj.install=function (Vue) {
      Vue.directive("focus",{
      inserted:function (obj) {
          obj.focus()
      }
      })
  }
  module.exports=obj
  ```

- 将js文件引入并运行

  ```js
  在route.js文件中
  import focus from '@/views/focus.js'
  Vue.use(focus)
  ```

- 最后就可以使用v-focus组件


#### 当路由跳转到未指定的路由时，可以设置跳到一个设定的组件

```py
{
      path: '*',
      name: 'index',
      component: Index
    }
 凡是为定义的路由都会都转到此路由
```

### 在falsk中，跳转到一个未指定的路径时，可以设置跳到一个设定页面

```py
@app.errorhandler(404)   指定跳转页面地址出错时，出现的内容
def error(error):
     return "error!"/return render_template()  返回错误语句或者是一个特定的页面
```

#### iframe内框标签（实现vue路由跳转的效果）

​	target=  (和frame中的name对应)    _self    在自己窗口打开

​	_top 在父窗口打开      

```py
<div class="left">
            <ul>
                {%for item in datas.menu%}
                    <li>
                        {{item.label}}
                        <ul>
                            {% for item1 in item.children%}
                                <li><a href="/select" target="main">{{item1.label}}
                            {% endfor %}
                        </ul>
                {%endfor%}
            </ul>
        </div>
        <div class="right">
            <iframe src="" frameborder="0" name="main"></iframe>
        </div>
```

设置在npm run serve运行时网页自动打开   在package.js中的serve中添加 --open

当5000端口访问8080端口是，使用fetch/ajax挈带cookie时

```
fetch(url, options).then(function(response) { 
// handle HTTP response
}, function(error) {
 // handle network error
})
options中有这几个属性可以设置
method(String): HTTP请求方法，默认为GET
body(String): HTTP的请求参数，传数据
headers(Object): HTTP的请求头，默认为{}
credentials(String): 默认为omit,忽略的意思，也就是不带cookie;还有两个参数  include为携带

服务器需要设置
res = make_response(redirect("/"))
res.headers["Access-Control-Allow-Credentials"]=True 任何请求都接受cookie
```
动态的添加内容，视图会随着响应

动态的添加属性，视图不会随着响应（利用Vue.set(obj,属性名，属性值)/this.$set(obj,属性名，属性值)来添加属性，视图会随着响应）

路由的嵌套使用，多重路由

```py
在非App.vue的组件中定义一个路由视图<router-view></router-view>
{
      path: '/addrole',
      component: Addrole,
      children:[
        {
           path: '',   定义子路由，path为空时表示显示父路由时，子路由也一同显示
           component: Addrole,
        },{
          path:
          component:
          }
      ]
    }
```

在同一个vue开发环境中实现多个入口文件

- 修改main.js中的import App from './App.vue'     改为自己另开发的
- 复制一份router.js文件，里边定义另一个开发使用的路由