<template>
  <div class="container">
    <div class="jumbotron">
      <img alt="Vue logo" src="../assets/koutoubia.jpg"/>
      <p class=""> Menara Marrakech</p>
      <hr>
      <h3> Mes tickets encours ... </h3>
      <div class="cardbox">

      </div>
      <CTicket v-for="(ticket, index) in getTickets"  :key="index"
        :ticket="ticket" >
        <p>{{ticket.title}}</p>
      </CTicket>
    </div>
  </div>
</template>


<script>
    import 'bootstrap/dist/css/bootstrap.min.css'
    import CTicket from "../components/CTicket.vue"
    import {  mapGetters, mapActions, } from "vuex" 

    export default {
        name: "HomePage",
        props : {
            msg:String,
        },
        components : { CTicket },
    
        mounted(){
            // load  all Tickets
            this.loadTickets();
        },
        computed:{
            ...mapGetters(['getTickets', 'isLoading',])
        },
        methods: {
            // load Tickets is now access as method
            ...mapActions(['loadTickets', ]),
        }
    }
</script>