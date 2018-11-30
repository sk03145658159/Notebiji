from flask import Flask,render_template,request,redirect,make_response,session
from serves.sql import cur,db;
from flask_cors import CORS
import json
import hashlib
from flask_session import Session
from serves.head import head
from serves.info import info

app=Flask(__name__)
CORS(app, resources=r'/*')

app.config["SESSION_TYPE"]="filesystem"
app.config["SESSION_FILE_DIR"]="C:/Users/hyh/PycharmProjects/untitled/serve/session"
app.permanent=True
app.permanent_session_lifetime=20
app.secret_key='hyh'
Session(app)
app.register_blueprint(head,url_prefix="/head")
app.register_blueprint(info,url_prefix="/info")

@app.route("/")
def index():
    if session.get('login')=="aaa":
        res=make_response()
        return render_template("index.html",data={"name":session.get('uname')})
    else:
        return redirect("/login")

@app.route("/login")
def login():
    return  render_template("login.html")

@app.route("/logup")
def logup():
    return render_template("logup.html")


@app.route("/del")
def delete():
    id=request.args.get("id")
    cur.execute("delete from stu where id="+id);
    db.commit()
    return "ok"



@app.route("/update")
def update():
    name=request.args.get("name")
    age = request.args.get("age")
    sex = request.args.get("sex")
    id = request.args.get("id")
    cur.execute("update stu set name=%s,sge=%s,sex=%s where id=%s",(name,age,sex,id))
    db.commit()
    return "ok"


#注册
@app.route("/submit",methods=["POST"])
def submit():
    uname=request.form["uname"]
    upsd = request.form["upass"]
    md5=hashlib.md5()
    md5.update(upsd.encode())
    upsd=md5.hexdigest()
    cur.execute("insert into user(uname,upsd) values (%s,%s)",(uname,upsd))
    db.commit()
    return redirect("/login")


#登录
@app.route("/login1",methods=["POST"])
def login1():
    uname = request.form["uname"]
    upsd = request.form["upass"]
    md5 = hashlib.md5()
    md5.update(upsd.encode())
    upsd = md5.hexdigest()
    cur.execute("select * from user where uname=%s and upsd=%s",(uname,upsd))
    result=cur.fetchone()
    global uid
    uid=result["id"]
    if(result):
        session["login"] = "aaa"
        session["uid"] = result["id"]
        session["uname"] = result["uname"]
        res=make_response(redirect("/"))
        return res
    else:
        return redirect("/logup")

@app.route("/all")
def all():
    id=session.get('uid')
    print(id)
    cur.execute("select * from stu where uid=%s",(uid))
    result = cur.fetchall()
    db.commit()
    return json.dumps(result)


@app.route("/add")
def add():
    name=request.args.get("name")
    age = request.args.get("age")
    sex = request.args.get("sex")
    print(session.get("uid"))
    cur.execute("insert into stu(name,sge,sex,uid) values(%s,%s,%s,%s)",(name,age,sex,uid));
    db.commit()
    return "ok"


#验证是否重名
@app.route("/jian",methods=["POST"])
def jian():
    uname=request.form["uname"]
    cur.execute("select * from user where uname=%s",(uname))
    result=cur.fetchone()
    if(result):
        return "false"
    else:
        return "true"

#退出
@app.route("/exit")
def exit():
    session.pop("login",None)
    return redirect("/login")


@app.route("/addcat")
def addcat():
    cname=request.args.get("cname")
    chead = request.args.get("chead")
    ctype = request.args.get("ctype")
    uid=request.args.get("uid")
    pid=request.args.get("pid")
    cur.execute("insert into cat(cname,chead,ctype,uid,pid) values(%s,%s,%s,%s,%s)",(cname,chead,ctype,uid,pid))
    cid=str(db.insert_id())  #在db.commit上边获取
    db.commit()
    return cid

@app.route("/selectcat")
def selectcat():
    global arr
    arr=[]
    cur.execute("select * from cat")
    result=cur.fetchall()
    results=digui(result,0)
    return json.dumps(results)



arr=[]
def digui(data,pid,now=None):
    global arr
    for item in data:
        if item["pid"]==pid:
            if not "children" in item:
                item["children"]=[]
            if item["pid"]==0:
                item["state"]=1
                item["type"]=item["ctype"]
                item["label"]=item["cname"]
                item["id"] = item["cid"]
                arr.append(item)
            else:
                item["label"] = item["cname"]
                item["type"] = item["ctype"]
                item["state"] = 1
                item["id"] = item["cid"]
                now.append(item)
            digui(data,item["cid"],item["children"])
    return arr

@app.route("/delcat")
def delcat():
    cid=request.args.get("cid")
    cur.execute("select * from cat where pid=%s",(cid))
    result=cur.fetchone()
    if(result):
        return "no"
    else:
        cur.execute("delete from cat where cid=%s",(cid))
        db.commit()
        return "ok"


@app.route("/updatecat")
def updatecat():
    cid=request.args.get("cid")
    cname = request.args.get("cname")
    cur.execute("update cat set cname=%s where cid=%s",(cname,cid))
    db.commit()
    return "ok"


app.run()
CORS(app)