<template>
    <div>
        <table class="table table-bordered">
            <tr>
                <td v-for="item in heads">{{item.head}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
       data(){
           return {
               id:"",
               heads:[]
           }
       },
        mounted(){
           this.id=this.$route.params.id
            console.log(this.id)
            fetch("http://127.0.0.1:5000/head/selecthead?cid="+this.id).then(function (e) {
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
        },
        watch:{
           $route(){
                this.id=this.$route.params.id
                console.log(this.id)
                fetch("http://127.0.0.1:5000/head/selecthead?cid="+this.id).then(function (e) {
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

</style>