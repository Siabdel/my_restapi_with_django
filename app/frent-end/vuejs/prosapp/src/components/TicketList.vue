<template>
    <div class="container">
        <div class="header">
            <a href="localhost:8080" class="btn btn-warning">
                <i class="glyphicon glyphicon-plus-signe"></i>
            <router-link class="nav-link" to="/add"> Ajouter article </router-link></a>|
        </div>
        <div  v-if="isLoading" class="spinner">
            <img src="" alt="">
            <div class="spinner-border text-danger" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <ul>
            <li v-for="(Ticket, index) in getTickets" :key="index" class="list-unstyled"> 
                <div class="row">
                    <div class="col-md-1">
                        <div class="card card-body">
                        <img :src="(Ticket.photo)?Ticket.photo:'#'"  />
                        </div>
                    </div>
                    <div class="col-md-7">
                        <div class="card">
                            <div class="card-header">
                                <router-link 
                                    :to="{'name': 'Ticket-details', 'params': {'id' : Ticket.id }}"> 
                                    {{ Ticket.id}} 
                                </router-link>
                            </div>
                            <div class="card-body">
                                <router-link 
                                    :to="{'name': 'Ticket-details', 'params': {'id' : Ticket.id }}"> 
                                    <h4 class="card-title">{{ Ticket.title }}</h4>
                                </router-link>
                                <p> {{ Ticket.created_at }}</p> 
                                <p> {{ (Ticket.comment)?Ticket.comment.slice(1, 300):''}} </p>
                            </div>
                            <div class="card-footer">
                                <p> <span>
                                    {{ Ticket.author.username }}
                                    </span> </p> 
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <button class="btn btn-warning">
                            <a href="#" @click.prevent=""> Update </a>
                        </button>
                        <button class="btn btn-warning">
                            <a href="#" @click.prevent=""> Delete </a>
                        </button>
                        <button class="btn btn-warning">
                            <a href="#" @click.prevent=""> Show </a>
                        </button>
                    </div>
                </div> 
                <hr/>
            </li>
        </ul>
    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.min.css';
    import {  mapGetters, mapActions, } from "vuex" 

    export default {
        name : "TicketList",
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