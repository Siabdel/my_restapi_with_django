<template>
  <div class="jumbotron">
    <img alt="Vue logo" src="../assets/logo.png">
    <hr>
    <h3>CartPostList *** </h3>
    <TicketList />
  </div>
</template>


<script>
    import 'bootstrap/dist/css/bootstrap.min.css'
    import TicketList from "../components/TicketList.vue"

    export default {
        name: "HomePage",
        props : {
            msg:String,
        },
        components : {TicketList},
        data: () => ({
            searchBy : true,
        }),
        methods:{
         // 
        },
    
    }
</script>