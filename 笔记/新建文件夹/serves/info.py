from flask import Blueprint,request
from serves.sql import cur,db
import json
info=Blueprint("info",__name__)

@info.route("listadd")
def listadd():
    cid=request.args.get("cid")
    ucon = request.args.get("ucon")
    cur.execute("insert into info(ucon,cid) VALUES (%s,%s)",(ucon,cid))
    db.commit()
    return "ok"


@info.route("listselect")
def listselect():
    cid=request.args.get("cid")
    cur.execute("select * from info where cid=%s",(cid))
    result=cur.fetchall()
    return json.dumps(result)