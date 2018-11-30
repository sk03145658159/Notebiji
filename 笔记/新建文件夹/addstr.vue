<template>
    <div>
        <el-button type="primary" @click="addhead()">添加文件结构</el-button>
        <div v-for="item in heads" class="con">
                <el-input
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
              v-model="item.head"  @blur="aa" class="input">
            </el-input>
            <el-button type="danger" class="del" @click="del(item)">删除</el-button>
            <!--<el-button type="danger" icon="el-icon-delete" circle></el-button>-->
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                heads:[],
                id:"",
            }
        },
        mounted(){
            this.id=this.$route.params.id
            fetch("http://127.0.0.1:5000/selecthead?cid="+this.id).then(function (e) {
                return e.text()
            }).then((e)=>{
                var arr=e.split("|")
                for (var i=0;i<arr.length;i++){
                    var obj={head:arr[i]}
                    this.heads.push(obj)
                }
            })
        },
        methods:{
            addhead(){
                var chead=this.gethead()?this.gethead()+"NoName|":"NoName"
                var parmas="cid="+this.id+"&chead="+chead
                fetch("http://127.0.0.1:5000/addhead?"+parmas).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    if(e=="ok"){
                         var obj={head:"NoName"}
                         this.heads.push(obj)
                    }
                })

            },
            aa(){
                var chead=this.gethead()
                var parmas="cid="+this.id+"&chead="+chead
                fetch("http://127.0.0.1:5000/addhead?"+parmas).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    if(e=="ok"){
                         console.log("aaa")
                    }
                })

            },
            del(item1){
                var aaa=this.heads.filter(function (item) {
                    if(item1!=item){
                        return item1
                    }
                })
                var chead=this.gethead(aaa)
                var parmas="cid="+this.id+"&chead="+chead
                fetch("http://127.0.0.1:5000/addhead?"+parmas).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    if(e=="ok"){
                         this.heads=aaa
                    }
                })
            },
             gethead(aaa){                //???
                 var str1=""
                 var data=aaa || this.heads
                data.forEach(function (val) {
                    str1+=val.head+"|"
                })
                str1=str1.slice(0,-1)
                return str1
            },
        },
        watch:{
            $route(){
                this.id=this.$route.params.id
                 fetch("http://127.0.0.1:5000/selecthead?cid="+this.id).then(function (e) {
                return e.text()
            }).then((e)=>{
                var arr=e.split("|")
                 var newarr=[]
                for (var i=0;i<arr.length;i++){
                    var obj={head:arr[i]}
                    newarr.push(obj)
                }
                this.heads=newarr
            })
            }
        }

    }
</script>

<style scoped>
    .con{
        display: flex !important;
    }
    .input,.del{
        margin:10px !important;
    }
</style>