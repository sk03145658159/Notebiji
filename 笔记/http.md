http

无状态协议

### cookie

存在硬盘上的一条数据

默认生命周期：浏览器关闭

res=make_response(render_template("index.html"))      res为Response-headers响应头

res.headers[“Set-cookie"]="aa=bb"   设置cookie值

res.set_cookie('username', 'the username')      (设置cookie值，flask中的方法)

返回对应页面 return res

username = request.cookies.get('username')    获取cookies

不可逆的加密方式（哈希算法，如md5(),sha512()....）

```py
import hashlib
md5=hashlib.md5()     32位  声明一个hashlib对象
md5.update(b"zhangsan") ||   md5.update(password.encode("utf-8"))当明确加密的字符时，用第一种。当加密传过来的数据时用第二种
upass=md5.hexdigest()
```

### session  （更加安全）  加密版的cookie

简单session知识将cookie加密，也不是很安全,cookie生命周期也默认为页面关闭

```py
app.secret_key=("123456")    #设置保密样式

session["login"]="yes"  设置session值

username=session.get("login")  获取session的值
```

#### flask_session     安全

```
pip install Flask-Session   安装flask_session 
```

**运用到了flask_session**，使cookie如一把钥匙，但没有真正的数据，真正的数据保存在服务器中，可保存的位置

- **null**: NullSessionInterface (default)

- **redis**: RedisSessionInterface

- **memcached**: MemcachedSessionInterface

- **filesystem**: FileSystemSessionInterface    保存在一个文件中

  ```py
  from flask import Flask,request,render_template,make_response,redirect,session
  import pymysql
  import json
  import hashlib
  from flask_session import Session    引入
  app=Flask(__name__)
  app.permanent=True   是不是要长久保存
  app.permanent_session_lifetime=10     #设置session的生命周期及保存的时间
  app.secret_key=("123456")    #设置保密样式
  app.config["SESSION_FILE_DIR"]="\\home\\shenkuo\\PycharmProjects\\aaaaaa\\serve"    #目标文件的位置 ，转义
  app.config["SESSION_TYPE"]="filesystem"  #保存在服务器的文件中
  Session(app)

  res=make_response(redirect("/"))  设置session值
  # res.set_cookie("login","yes")
  session["login"]="yes"
  return res

  username=session.get("login")  获取session的值

  session.pop()  清除session的值
  ```

  ​

- **mongodb**: MongoDBSessionInterface

- **sqlalchemy**: SqlAlchemySessionInterface


#### jQuery Validate  为表单提供了强大的验证功能

```py
异步验证
remote：URL
使用 ajax 方式进行验证，默认会提交当前验证的值到远程地址，如果需要提交其他的值，可以使用 data 选项。

remote: "check-email.php"
remote: {
    url: "check-email.php",     //后台处理程序
    type: "post",               //数据发送方式
    dataType: "json",           //接受数据格式   
    data: {                     //要传递的数据
        username: function() {
            return $("#username").val();
        }
    }
}
```

file://  在本地直接打开的文件，地址由file开头




