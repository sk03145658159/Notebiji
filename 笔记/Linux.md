# Linux   ubuntu（乌邦图）多用户，多任务操作系统

架构  

c/s架构    依赖于下载客户端，更新不及时（不基于网络，操作流畅）

b/s架构    不依赖于客户端，在浏览器中实现，可以随时访问最新的内容，免去用户的下载（基于网络，会有延迟，不能够流畅的操作，体验性不好）

### 运行软件

找到软件的位置

sh.软件文件

## 浏览器的功能

- 呈现内容          谷歌-webkit-解析内容和样式(html,css)
- 实现交互逻辑       谷歌   v8引擎   解析js
- 进行数据传递         谷歌  charm  net引擎(互联网数据传递)

linux是指一种操作系统，也可指操作系统的内核。Ubuntu是最受欢迎的发行版(永久免费，开源分享，定期更新和发布，六个月发布一个版本)。还有CentOS，redcat,Fedora等版本。是多用户多任务的支持远程操作的系统。

ctrl+shift+加号  调节字体的大   ctrl+减号  调节字体变小

ctrl+t分屏

alt+1/2/3切屏

cd切换目录

cd/ 进根目录

cd ~      home目录

cd -  返回进入上一次的目录

/   根目录（linuex只有一个根目录）

ls查看目录的内容

ls --help  查看ls的帮助

ls -a查看目录所有文件

ls -l 查看目录文件详细信息

ls -al     查看目录所有文件详细信息

cd ..返回上一级目录

cd.当前目录

cd ../../  上上曾目录

cd /home/shenkuo  路径，从根目录开始找

cd home/shenkuo  从当前目录开始找

### 根目录（包含的各个文件的含义）

- /**bin  重要的二进制应用程序**（命令）
- sbin  重要的系统二进制文件（超级管理员）
- /dev  设备文件
- /boot  启动的配置文件
- /**etc  配置文件、启动脚本等(系统的)**
- /**home 本地用户主目录(普通用户)**
- /lib 系统库文件，bin/sbin中应用程序代码
- /media  管理移动设备
- /mnt   挂载文件系统
- /opt  提供一个可选的应用程序安装目录
- /proc(process)特殊的动态目录（不要动）
- /root 关于超级管理员的东西
- /temp  临时文件
- /**usr   配置文件（用户自定义的命令）包含绝大部分所有用户都可以**
- lost+found  临时存储（不要动）

### 查看帮助文档

- man command    （f翻页q退出）   例man ls
- command --help     (一下打出所有信息)  例 ls --help

### 查看命令位置 which command（window中为where）

### 查看当前在什么目录 pwd

### 写入新建文件和查看文件内容

1.echo hello > 1.txt

cat 1.txt   查看文件内容

echo 123 > 1.txt 会覆盖旧内容

echo 456 >> 1.txt 追加

gedit 1.txt    (ubuntu自带编辑器，window系统用vim-gtk编辑器:   功能模式：dd删除 （按i切换到）插入模式：（按esc退出插入模式，:wq!保存退出） )

2.touch 2.txt   (有就不创建，没有创建)

   gedit 2.txt

   cat 2.txt

3.直接通过编辑器新建  

   gedit 3.txt

   cat 3.txt

### 删除文件

​    rm 1.txt

​    rm  *.txt  

### 创建目录，文件夹

创建a目录  mkdir a                mkdir -p a/b/c创建层级

### 删除目录

**rm -rf  a 什么目录均可**

rmdir a   只能删除空目录      rmdir -p a/b/c  连续删除空目录

### mv（重命名和剪切）

- 将目录重命名 mv a  aaa

- 剪切

  有两个目录a和b，将a剪切到b中:mv a b

### cp拷贝

拷贝文件

cp 1.txt 2.txt

拷贝目录

cp -r a b

### histoty   查看历史

### history -c 清空历史纪录    

### 链接（改变一个，链接的也跟着改变）

#### 文件链接

**软链接**  基本不占内存空间  

**ln -s**  1.txt 2.txt 同一目录

**ln -s**  /home/shenkuo/1.txt    /home/shenkuo/sugeest/2.txt      不同目录下的文件链接，需要用绝对路径

**硬链接**  拷贝出来的具有联系的文件，占内存空间

**ln**  1.txt  2.txt

#### 文件夹链接

**软链接**    方法同文件链接

**无硬链接**

### 查找 find

find 查找文件（ * ）         find nig*

sudo find nig* > 1.txt  将查找的内容放到文件里   （**sudo 没有权限时加上**）

sudo find neg* | grep con    (find查找文件，grep查找内容)  **sudo 没有权限时加上**     | 通过管道进一步查找

grep con(内容)   *.txt  (在文件中查找包含con内容的)

### *压缩

**打包:** tar -cvf  目标文件  源文件         tar -cvf  b  a（-c创造文件，-v显示打包过程，-f指定打包后的文件名，-x解包，-z压缩格式（gzip），-j压缩格式（bz2））

**解包:** tar -xvf b  **-C**  c     

**压缩：** tar -zcvf 目标文件  源文件    (gzip压缩模式,windows用zip压缩模式）tar -zcvf b a

**解压：**tar -zxvf  b **-C** c 解压文件

zip解压  zip dest目标文件  source源文件

unzip (-d)(path)解压  unzip dest

### 两台电脑联互（<u>文件的传输</u>）putty

全局变量：我的电脑右键属性->高级选项->环境变量PATH

ifconfig查看获取各种地址和

需要利用相同的协议

http协议

Ftp协议

get协议（基于ssh）

#### ssh协议（secure shell ）

特点：先压缩速度快，加密安全，对口令

##### 将本电脑和虚拟机利用ssh协议联互

虚拟机中ctrl alt+t 输入sudo apt-get install openssh-server，下完之后输入ifconfig

打开windows cmd 输入ssh 你的虚拟机用户名@虚拟机inet地址 回车（在windows上登陆Ubuntu系统）

输入虚拟机密码

exit退出

#### linux和linux传输文件

scp [-r] aa.html shenkuo@192.168.188.182:/home/shenkuo/a     将本地的文件上传到远地电脑（如果是文件夹需加-r）

scp [-r] shenkuo@192.168.188.182:/home/shenkuo/a b   将远地的文件拷贝到本地电脑（如果是文件夹需加-r）

**windows和linux传输文件**

下载pxcp.exe  ，配置windows的环境变量path

pscp [-r] aa.html shenkuo@192.168.188.182:/home/shenkuo/a  将本地的文件上传到远地电脑（如果是文件夹需加-r）

pscp [-r] shenkuo@192.168.188.182:/home/shenkuo/a b  将远地的文件拷贝到本地电脑（如果是文件夹需加-r）

### 磁盘管理

cd 切换目录

df 查看磁盘使用情况      df -h更利于查看

du  查看某目录下，文件所占的信息情况

### 网路通讯

ifconfig查看或设置网卡

修改地址

- ifconfig ^c
- ifconfig etho  172....新地址

上网的协议

- udp协议:netstat -aup(所有正在使用udp协议联网的的软件的端口)
- tcp协议:netstat -atp(所有正在使用tcp协议联网的的软件的端口)

可以去万网买域名，阿里买地址

### 软件的安装和处理

- apt_get(只适用于ubuntu)方式安装
  - [ ] 更新软件库sudo apt-get update
  - [ ] 添加包地址sudo add-apt-repository ppa:webupd8team/java(官方仓库没有该软件时，在个人仓库中下载，添加个人仓库后更新软件库sudo apt-get update）
  - [ ] 包的删除
        - [ ] sudo apt-get remove packagename  卸载包，卸载不干净（不采取）
        - [ ] 1.sudo apt-get  --purge remove mysql-server mysql-client(删除软件包包括配置文件)
        - [ ] 2.sudo apt -get autoremove mysql-server mysql-client(删除软件的依赖包)
        - [ ] 3.sudo apt-get clean && sudo apt-get autoclean(删除该软件的无用包)
  - [ ] sudo apt-get install mysql-server mysql-client数据库的安装（mysql-server服务端，存储数据，mysql-client客户端，运行mysql命令）
  - [ ] sudo apt-get install tree  使文件目录成树形结构显示

- **源码安装**

  - [ ] 下载源码

        ```py
        sudo wget url(源码地址)
        wget -o fillname url
        ```

  - [ ] 找到压缩包进行解压 sudo  tar -zxvf fillname

  - [ ] 进入解压文件，找到config文件,运行下面代码进行配置

        ./configure --prefix=/usr/local/test(安装地址)

  - [ ] 编译sudo  make all

  - [ ] 安装sudo  make install

  - [ ] 多版本共存 

        sudo update-alternatives --install   /usr/bin/python3(命令的位置)  python3(设置命令名称)   /opt/python/bin/python3.7(命令执行的位置)  500(优先级)

        update-alternatives --install link name path priority[]

        其中link为系统中功能相同的公共链接目录

  ### 关机

  $halt 立刻关机

  $poweroff 立刻关机

  $shutdown -h now 立刻关机（root用户使用）

  $shutdown -h 10   10分钟后自动关机

  ### 重启

  $reboot

  $shutdown -r now

  $shutdown -r now 10  

  $shutdown -r 20:35

  ### 进程

  ps -aux 显示所有包含使用者的进程   ps -aux  | grep mysql查看某个进程（top   查看当前整个程序的运行情况，按q退出查看）

  top 动态显示所有进程

  kill pid  杀死进程  （pid为进程号）

  kill -9 pid  强制杀死进程

  杀不掉为守护进程

  cd   /etc/init.d/(守护进程的通常位置)

  sudo /etc/init.d/mysql  stop(将mysql停止)   sudo /etc/init.d/mysql  start(开启)  sudo /etc/init.d/mysql  restart(重启)

  ### pycharm的破解

  idea.lanyus.com获取注册码

  修改host文件 0.0.0.0 accout.jetbrains.com（host在/etc/hosts）

  （umake --remove ide pycharm） 

  ### 权限管理


  sudo -s

  whoami 查看当前用户

  who  查看多少人在操作该系统

  添加用户sudo useradd  -m  first(新建用户名)   (-m加上使home主动创建)

  【查看是否添加成功，进入/home或进入/etc/passwd】

  设置新用户的密码sudo passwd  first(新建用户名)

  删除用户sudo userdel -f firsrt

切换用户： su   用户名

  usermod修改用户

  ​	指定用户的登陆起始目录sudo  usermod  first  -d  /home/first/demo

  ​	usermod first -g aaa  将用户指定一个组(主组,无法删除)   （-G给用户追加一个组(父组)）

  查看组 cat /etc/group          ||      groups  first(用户名)

  创建组（先有组才有用户）

  ​	groupadd  组名

  删除组中的用户

  ​	sudo gpasswd -d 用户名  组名

  组中追加用户

  ​	sudo gpasswd -a  用户名  组名

  删除组

  	sudo groupdel demo(组名)

  修改组

  ​	sudo groupmod  组名  -n  新组名

  让新用户拥有sudo的权限

  ​	sudo usermod -a -G sudo 用户名

  	sudo usermod -a -G adm 用户名

  ### 日志位置：/var/log/

## 权限的修改和设置

###   **ls -l**

- 第一部分：  d表示目录     |       -表示文件

- 第二部分  所属者的权限、所属组的权限（组内其他对象）、所有用户的权限     （一个权限占三位）

  r 可读  w可写  x可执行

  读取文件里的数据     可以改变和删除文件     可以执行该程序

  可以列出目录的文件      可以删除/增添文件         列出文件的详细信息

- 第三部分  文件的硬链接数量/目录所含文件数

- 第四部分   文件所属用户，用户所属组

- 第五部分  大小及修改时间等

#### chown  (文件所属用户的更改)

sudo chown -R  用户名(被给予权限用户):组名    文件名              没有-R，只能更改指定的文件或目录，里面的内容不会随这改动

sudo chown -R  用户名:组名   /home/(文件路径或目录的绝对路径路径)

#### chmod（修改文件的权限）

#### chmod   u=rwx,g=rwx,o=rw 文件名/目录名       user,group,other

#### chmod  【-R】 777  ccc.txt(目标文件名/目录名)1->x  2->w   4->r    5->rx  6->wr 7->rwx

   将python文件改为可执行文件   #!/usr/bin/env python（在vim最上面写入） 

  ​