from flask import Blueprint,request
from serves.sql import cur,db

head=Blueprint("head",__name__)

@head.route("/addhead")
def addhead():
    cid=request.args.get("cid")
    chead = request.args.get("chead")
    cur.execute("update cat set chead=%s where cid=%s",(chead,cid))
    db.commit()
    return "ok"


@head.route("/selecthead")
def selecthead():
    cid=request.args.get("cid")
    cur.execute("select chead from cat where cid=%s",(cid))
    result=cur.fetchone()
    result=result["chead"]
    return result