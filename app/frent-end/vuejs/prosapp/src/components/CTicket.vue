<template>
    <div class="container">
        <div class="card">
            <div class="card-header">
                <router-link 
                    :to="{'name': 'Ticket-details', 'params': {'id' : ticket.id }}"> 
                    {{ ticket.id}} 
                </router-link>
            </div>
            <div class="card-body">
                <router-link 
                    :to="{'name': 'Ticket-details', 'params': {'id' : ticket.id }}"> 
                    <h4 class="card-title">{{ ticket.title }}</h4>
                </router-link>
                <p> {{ ticket.created_at }}</p> 
                <p> {{ (ticket.comment)?ticket.comment.slice(1, 300):''}} </p>
            </div>
            <div class="card-footer">
                <p> <span>
                    {{ ticket.author.username }}
                    </span> </p> 
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
        <hr/>
    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.min.css';
    export default {
        name : "CTicket",
        //props : ['id', 'title', 'created_at', 'comment',],
        props : {
            ticket : {},
        }
    }
</script>