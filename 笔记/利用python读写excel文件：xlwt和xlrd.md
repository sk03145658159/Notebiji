#### 利用python读写excel文件：xlwt和xlrd

#### 查询http的一些相关请求/转义/常见端口....（搜索http content-type）

#### 获取表单的值： let values=$('form').serializeArray()



### python中实现文件的下载，利用flask中的make_response和send_from_directory

##### python中的make_response模块：自理解将模板转成一个可操作的对象，设置类似cookies信息

##### python中的send_from_directory模块:首选在application下建立一个upload目录，构造upload目录的绝对路径。#然后通过浏览器输入指定文件的文件名来下载。

```py
res=make_response(send_from_directory('.','demo.xls',as_attachment=True))
res.headers['content-disposition']='attachment;filename=1.xls'
return res
```

book=xlrd.open_workbook(a.xlsx)   保存的文件利用python中的xlrd读取操作(首先下载xlrd，方法查看官网)

sheet=book.sheet_by_index(0)

 sheet = sheet.row_values(1)

**xlrd.xldate_as_datetime(info[2],0)  读取时间数据，返回时间对象**

python中的datetime模块处理   .strftime("%Y-%m-%d %H:%M:%S")

xlrd.xldate_as_datetime(con[2], 0).strftime("%Y-%m-%d %H:%M:%S")