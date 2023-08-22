
<template>
    <div class="container">
        <h2> Mes tickets encours ... </h2>
        <CTicket v-for="(ticket, index) in tickets"  :key="index"
            :ticket="ticket" >
            <p>{{ticket.title}}</p>
        </CTicket>
    </div>
</template>

<script>

import 'bootstrap/dist/css/bootstrap.min.css'
import CTicket from "../components/CTicket.vue"
import {  mapState,  } from "vuex" 

export default {
    name : "IncidentList",
    components : { CTicket },
    computed:{
        //...mapGetters(['getTickets', 'isLoading',])
        ...mapState(['tickets', 'isLoading', ])
    },

}
</script>