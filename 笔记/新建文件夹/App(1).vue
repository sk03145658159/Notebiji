<template>
    <div id="app">
        <el-container class="container">
            <el-header class="header"></el-header>
            <el-container class="main">
                <div @contextmenu.prevent.stop="addmenu($event)">
                <el-aside class="left">

                    <el-row>
                        <div class="block">
                            <el-tree
                              :data="data5"
                              node-key="id"
                              default-expand-all
                              :expand-on-click-node="false">
                              <span class="custom-tree-node" slot-scope="{ node, data }">
                                  <span v-if="data.type==1" @contextmenu.prevent.stop="addmenu1($event,data,node)">
                                      <span v-if="data.state==1">文件夹：{{ node.label }}</span>
                                      <input v-else type="text" v-model="data.label" @blur="change1()" v-focus>
                                  </span>
                                  <span v-else>
                                      <span v-if="data.state==1">文件：<a :href="'#/list/'+data.id" @contextmenu.prevent.stop="addmenu2($event,data,node)">{{ node.label }}</a></span>
                                      <input type="text" v-else v-model="data.label" @blur="change2()" v-focus>
                                  </span>
                              </span>
                            </el-tree>
                          </div>
                    </el-row>
                </el-aside>
                    <!--左边框-->
                    <div class="hidden" ref="hidden" @mouseleave="disappear()">
                        <div @click="newdir()">新建文件夹</div>
                        <div @click="newfile()">新建文件</div>
                    </div>
                    <!--文件夹-->
                    <div class="hidden1" ref="hidden1" @mouseleave="disappear1()">
                        <div @click="newdir1()">新建文件夹</div>
                        <div @click="newfile1()">新建文件</div>
                        <div @click="changestate1()">重命名</div>
                        <div @click="del1()">删除</div>
                    </div>
                    <!--文件-->
                    <div class="hidden1" ref="hidden2" @mouseleave="disappear2()">
                        <div @click="changestate2()">重命名</div>
                        <div @click="addstr2()">创建结构</div>
                        <div @click="del2()">删除</div>
                    </div>
                    </div>
                <el-main class="right">
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>

</template>

<script>
   export default {
    data(){
        return {
        datas:[],
        node:[],
        data5:[]
        }
    },
       mounted(){
        fetch("http://127.0.0.1:5000/selectcat").then(function (e) {
            return e.json()
        }).then((e)=>{
            this.data5=e
        })
    },

    methods: {
        //文件右击
        addmenu2(e,data,node){
            this.node=node
            this.datas=data || []
            this.$refs.hidden2.style.display="block"
            var left=e.clientX-3
            var top=e.clientY-3
            var selfw=this.$refs.hidden2.offsetWidth
            var selfh=this.$refs.hidden2.offsetHeight
            var leftw=document.querySelector(".left").offsetWidth
            var lefth=document.querySelector(".left").offsetHeight
            var headh=document.querySelector(".header").offsetHeight
            if(left>leftw-selfw){
                left=leftw-selfw
            }
             if(top>lefth-selfh+headh){
                top=lefth-selfh+headh
            }
            this.$refs.hidden2.style.left=left+"px"
            this.$refs.hidden2.style.top=top+"px"
        },

        disappear2(){
            this.$refs.hidden2.style.display="none"
        },

        del2(){
            fetch("http://127.0.0.1:5000/delcat?cid="+this.datas.cid).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e=="ok"){
                    const parent = this.node.parent;
                    const children = parent.data.children || parent.data;
                    const index = children.findIndex(d => d.id === this.datas.id);
                    children.splice(index, 1);
                    this.$refs.hidden2.style.display="none"
                }
                else{
                    alert("非空文件，不能删除")
                }
            })
        },

        changestate2(){
             this.datas.state=2
            this.$refs.hidden2.style.display="none"
        },

        change2(){
             var parmas="cid="+this.datas.id+"&cname="+this.datas.label
             fetch("http://127.0.0.1:5000/updatecat?"+parmas).then(function (e) {
                 return e.text()
             }).then((e)=>{
                 if(e=="ok"){
                     this.datas.state=1
                 }
             })
        },

        addstr2(){
          this.$router.push("/addstr/"+this.datas.id)
            this.$refs.hidden2.style.display="none"
        },


        //文件夹右击
        addmenu1(e,data,node){
            this.node=node
            this.datas=data || []
            this.$refs.hidden1.style.display="block"
            var left=e.clientX-3
            var top=e.clientY-3
            var selfw=this.$refs.hidden1.offsetWidth
            var selfh=this.$refs.hidden1.offsetHeight
            var leftw=document.querySelector(".left").offsetWidth
            var lefth=document.querySelector(".left").offsetHeight
            var headh=document.querySelector(".header").offsetHeight
            if(left>leftw-selfw){
                left=leftw-selfw
            }
             if(top>lefth-selfh+headh){
                top=lefth-selfh+headh
            }
            this.$refs.hidden1.style.left=left+"px"
            this.$refs.hidden1.style.top=top+"px"
        },

        newdir1(){

            var parmes="cname=newdir&chead=&uid=1&ctype=1&pid="+this.datas.id
            fetch("http://127.0.0.1:5000/addcat?"+parmes).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e){
                     const newChild = {id:e,label: 'newdir', children: [],type:"1",state:1};
                    if (!this.datas.children) {
                      this.$set(this.datas, 'children', []);
                    }
                    this.datas.children.push(newChild);
                    this.$refs.hidden1.style.display="none"
                }
            })


        },

        newfile1(){

            var parmes="cname=newfile&chead=&uid=1&ctype=2&pid="+this.datas.id
            fetch("http://127.0.0.1:5000/addcat?"+parmes).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e){
                     const newChild = {id:e,label: 'newfile', children: [],type:"2",state:1};
                    if (!this.datas.children) {
                      this.$set(this.datas, 'children', []);
                    }
                    this.datas.children.push(newChild);
                    this.$refs.hidden1.style.display="none"
                }
            })
        },

        disappear1(){
            this.$refs.hidden1.style.display="none"
        },

        del1(){
            fetch("http://127.0.0.1:5000/delcat?cid="+this.datas.cid).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e=="ok"){
                    const parent = this.node.parent;
                    const children = parent.data.children || parent.data;
                    const index = children.findIndex(d => d.id === this.datas.id);
                    children.splice(index, 1);
                    this.$refs.hidden1.style.display="none"
                }
                else{
                    alert("非空文件夹，不能删除")
                }
            })

        },

        changestate1(){
             this.datas.state=2
             this.$refs.hidden1.style.display="none"
        },

        change1(){
            var parmas="cid="+this.datas.id+"&cname="+this.datas.label
             fetch("http://127.0.0.1:5000/updatecat?"+parmas).then(function (e) {
                 return e.text()
             }).then((e)=>{
                 if(e=="ok"){
                     this.datas.state=1
                 }
             })

        },


        //左边框右击
        newdir(){
            var parmes="cname=newdir&chead=&uid=1&ctype=1&pid="+0
            fetch("http://127.0.0.1:5000/addcat?"+parmes).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e){
                    console.log(e)
                    this.data5.push({id:e,"label":"newdir","type":"1",state:1})
                    this.$refs.hidden.style.display="none"
                }
            })

        },

        newfile(){
            var parmes="cname=newfile&chead=&uid=1&ctype=2&pid="+0
            fetch("http://127.0.0.1:5000/addcat?"+parmes).then(function (e) {
                return e.text()
            }).then((e)=>{
                if(e){
                    this.data5.push({id:e,"label":"newfile","type":"2",state:1})
                    this.$refs.hidden.style.display="none"
                }
            })

        },

        disappear(){
            this.$refs.hidden.style.display="none"
        },

        addmenu(e){
            this.$refs.hidden.style.display="block"
            var left=e.clientX-3
            var top=e.clientY-3
            var selfw=this.$refs.hidden.offsetWidth
            var selfh=this.$refs.hidden.offsetHeight
            var leftw=document.querySelector(".left").offsetWidth
            var lefth=document.querySelector(".left").offsetHeight
            var headh=document.querySelector(".header").offsetHeight
            if(left>leftw-selfw){
                left=leftw-selfw
            }
             if(top>lefth-selfh+headh){
                top=lefth-selfh+headh
            }
            this.$refs.hidden.style.left=left+"px"
            this.$refs.hidden.style.top=top+"px"
        },

    },

  };
</script>

<style scoped>
    html,body{
        width:100%!important;
        height:100vh!important;
    }
    #app{
        width:100%!important;
        height:100vh!important;
    }
    .container{
        width:100%;
        height:100%!important;
    }
    .header{
        width:100%;
        height:20%!important;
        background: tan;
    }
    .main{
        width:100%;
        height:80%!important;
    }
    .left{
        width:30%;
        height:100% !important;
        border-right:5px solid #ccc;
    }
    .right{
        width:70%;
        height:100% !important;

    }
    .hidden{
        width:100px;
        border:1px solid #ccc;
        padding:10px;
        border-radius: 5px;
        position: absolute;
        top:0;
        left:0;
        display: none;
        background: #ddd;
        cursor:pointer;
    }
    .hidden1{
        width:100px;
        border:1px solid #ccc;
        padding:10px;
        border-radius: 5px;
        position: absolute;
        top:0;
        left:0;
        display: none;
        background: #ddd;
        cursor:pointer;
    }
     .hidden2{
        width:100px;
        border:1px solid #ccc;
        padding:10px;
        border-radius: 5px;
        position: absolute;
        top:0;
        left:0;
        display: none;
        background: #ddd;
         cursor:pointer;
    }
</style>