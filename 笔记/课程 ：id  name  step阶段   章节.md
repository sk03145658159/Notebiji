课程 ：id  name  step阶段   章节

主表  cid  cname        

​          1     ai          

副表  id   stepname       章节         	cid

​	1     前端      html|css|js      1

​	2     python   基础|               1

alt+回车 excel在合并单元格中实现换行

http下载响应头，flask如何进行上传，xlwd写excel内容，xlrd如何解析excel内容

班级表

id   name  start(DATE日期,DATETIME日期时间,TIMESTAMP时间戳)默认值CURRENT_TIMESTAMP插入信息的时间     end   fid方向 



id  name  phone(varchar11)  classid      sex  school

老师的姓名  手机号   代课方向    代课班级   

id    name   phone   courseid  classid



title255   con3000   phone提交的人11   time(默认值)提交的时间timestamp(datetime)
select * from logs where id in (1,2,3)  枚举
select * from logs where phone in (select phone from student where classid in (select id from classes where fid in (9课程方向))) 子查询
课程方向=》班级=》学生
date.format(login.time,"%Y-%m-%d")  mysql的一个语句，将时间对象格式化为一种形式
select logs.*,stu.name as sname,classes.name as cname from logs left join stu on logs.phone=stu.phone left join classes on stu.classid=classes.id where logs.phone in (select phone from stu where classid in (select id from classes where fid in (10)) and date_format(logs.time,"%Y-%m-%d")="2018-11-11") limit  0,5  limit分页处理，从哪个位置取几条，
location.pathname  请求的地址内容
localtion.href("url")  向哪发送请求





**文件下载的两种方法**

一：利用python读文件

file=open("文件位置","r")  当文件为xlsx时用rb

con=file.read()

res=make_response(con)   设置响应头

res.headers[  res.headers['content-disposition'] = 'attachment;filename=2.xlsx']

return res

二：利用python中自带的模块

res = make_response(send_from_directory('./Download', '1.xlsx', as_attachment=True))

res.headers['content-disposition'] = 'attachment;filename=2.xlsx'
return res



**文件上传**

< input  type=“file” >   基本上传方式

后台flask用request.files[""]接收文件     前端form标名传递方式post    编码格式  （上传到服务器临时空间，）

file.save("a.xlsx"保存位置及命名)

book=xlrd.open_workbook(a.xlsx)   保存的文件利用python中的xlrd读取操作(首先下载xlrd，方法查看官网)

sheet=book.sheet_by_index(0)

 sheet = sheet.row_values(1)

```py
源码实现
前端
<form action="/ajax/course/shangchuan" method="post" enctype="multipart/form-data">
        <span>选择上传文件</span><input type="file" name="file" value="选择jar包">
        <button type="submit" class="btn btn-success">上传文件</button>
    </form>
    <a href="">下载文档模板</a>
后台
@course.route("/shangchuan",methods=["POST"])
def shangchuan():
    file=request.files["file"]
    file.save("a.xlsx")
    return "ok"
```



