<template>
  <div class="jumbotron">
    <img alt="Vue logo" src="../assets/logo.png">
    <hr>
    <h3>CartPostList</h3>
    <CartPostList msg="Welcome to Your Vue.js Post Store"/>
  </div>
</template>


<script>
    import 'bootstrap/dist/css/bootstrap.min.css'
    import CartPostList from '../components/CartPostList.vue'

    import { mapMutations } from 'vuex';

    export default {
        name: "HomePage",
        props : {
            msg:String,
        },
        components : {CartPostList, },
        data: () => ({
            searchBy : true,
        }),
        methods:{
         ...mapMutations(['setTermToSearch']), 
         // chercher une cle
        },
    
    }
</script>