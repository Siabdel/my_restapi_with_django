import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({

    state : {
        tickets : [],
        selectedTicket : {},
        isLoading : false,
        ticketInsert : false,
        selectTicketId : null,
    },

    getters :{
        getTickets : state => state.tickets,
        // get selected tick
        getSelectedTicket:  state => state.selectedTicket
    } ,

    mutations : { 
        setIsLoading(state, bool){
            state.isLoading = bool;
        },
        setTicketInsert(state, bool){
            state.ticketInsert = bool;
        },
        setTickets(state, {tickets} ){
            state.tickets = tickets;
        },
        setSelectedTicketId(state, id){
            state.selectTicketId = id
        },
        setSelectedTicket(state, {ticket}){
            state.selectedTicket = ticket
        }
        
    },
    //--
    actions : {
        // get Ticket selected
        async loadTicket( {commit }, ticket_id ){
            // URL via Ticket,  URL  end in a slash 
            let url = 'http://localhost:8000/api/v2/incident/' + ticket_id
            const access_token =  'd3340738633cdbfb8a74ef96423008f01c425e76'
            let headers = {
                    "Accept"  : "application/json",
                    "Content-Type": "application/json",
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    'Authorization': `token ${access_token}`
                } 
            // save token
            console.log("header = ", headers)

            commit("setIsLoading", true)
            // fetch 
            axios.get(url,)
            .then(response => response.data)
            .then(data => {
                    commit("setIsLoading", false)
                    commit("setSelectedTicket", { ticket : data })
                    // save token 
                    console.log("  Tickets loaded and commited ..." + data.title )
                    }
            )
            .catch(error => {
                console.log("Erreur loading data from " + error)
                commit("setIsLoading", false)
                }
            );
        },
        // load all ticket
        async loadTickets( {commit }, ){
            // URL via Ticket,  URL  end in a slash 
            let url = 'http://localhost:8000/api/v2/incident/'
            const access_token =  'd3340738633cdbfb8a74ef96423008f01c425e76'
            let headers = {
                    "Accept"  : "application/json",
                    "Content-Type": "application/json",
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    'Authorization': `token ${access_token}`
                } 
            // save token
            console.log("header = ", headers)

            commit("setIsLoading", true)
            // fetch 
            axios.get(url,)
            .then(response => response.data)
            .then(data => {
                    commit("setIsLoading", false)
                    commit("setTickets", { tickets : data })
                    // save token 
                    localStorage.setItem('token', access_token)
                    console.log("  Tickets loaded and commited ..." + data.length )
                    }
            )
            .catch(error => {
                console.log("Erreur loading data from " + error)
                commit("setIsLoading", false)
                }
            );
        },       
    
          //-- add ticket
        async addTicket({commit}, ticket)
        {
            //authAPI.login(this.email, this.body)
            let url = 'http://localhost:8000/api/v2/incident/'
            let headers = {
                    'Content-Type': 'application/json',
            }
            console.log(headers)
            console.log("ticket data = ", ticket)
            //Axios
            await axios.post(url, ticket)
            .then( () =>  {
                console.log("Add data :" + ticket.title)
                commit("setTicketInsert", true )
            })
            .catch( (error) => {
                console.log("Api Erreur add ticket !!" + ticket.comment + error)
            });
        },
        // Delete
        // delete Ticket
        async deleteTicket({commit}, ticket_id )
        {
            let url = 'http://localhost:8000/api/v2/incident/' + `${ticket_id}`
            commit("setIsLoading", true)
            await axios.delete(url, ticket_id)
            .then( () =>  {
                console.log("Delete Ticket !!" )
                commit("setIsLoading", false)
            })
            .catch( (error) => {
                commit("setIsLoading", false)
                console.log("Api Erreur Ticket not deleted!!" + error)
            });
            // Initialize the access & refresh token in localstorage.      
        },
         // update ticket
        async updateTicket({commit}, ticket)
        {
            let url = 'http://localhost:8000/api/v2/incident/' + `${ticket.id}/`
            commit("setIsLoading", true)
            await axios.put(url, ticket)
            .then( () =>  {
                console.log("ticket updated !!" )
                commit("setIsLoading", false)
            })
            .catch( (error) => {
                console.log("Erreur ticket not updated!!", ticket.title)
                console.log("Api Erreur not updated!!", error)
                commit("setIsLoading", false)
            });
            // Initialize the access & refresh token in localstorage.      
        },
    }
})