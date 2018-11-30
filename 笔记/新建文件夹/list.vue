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
        watch:{
           $route(){
                this.id=this.$route.params.id
                console.log(this.id)
                fetch("http://127.0.0.1:5000/selecthead?cid="+this.id).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    var arr=e.split("|")
                    for (var i=0;i<arr.length;i++){
                        var obj={head:arr[i]}
                        this.heads.push(obj)
                    }
                })
           }
        }

    }
</script>

<style scoped>

</style>