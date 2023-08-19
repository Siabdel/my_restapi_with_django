<template>
  <div class="container">
    <div class="jumbotron">
      <img alt="Vue logo" src="../assets/koutoubia.jpg"/>
      <p class=""> Menara Marrakech</p>
      <hr>
      <h3> Mes tickets encours ... </h3>
      <div class="cardbox">

      </div>
      <CTicket v-for="(ticket, index) in tickets"  :key="index"
        :ticket="ticket" >
        <p>{{ticket.title}}</p>
      </CTicket>
    </div>
  </div>
</template>


<script>
    import 'bootstrap/dist/css/bootstrap.min.css'
    import CTicket from "../components/CTicket.vue"
    import {  mapState,  } from "vuex" 

    export default {
        name: "HomePage",
        props : {
            msg:String,
        },
        components : { CTicket },
        computed:{
            //...mapGetters(['getTickets', 'isLoading',])
            ...mapState(['tickets', 'isLoading', ])
        },
        created() {
        },
        methods:{
        }
    }
</script>