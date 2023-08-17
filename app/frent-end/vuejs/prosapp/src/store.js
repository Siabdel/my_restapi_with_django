import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({

    state : {
        tickets : [],
        isLoading : false,
    },

    getters :{
        getTickets : state => state.tickets,
    } ,

    mutations : { 
        setIsLoading(state, bool){
            state.isLoading = bool;
        },
        setTickets(state, {tickets} ){
            state.tickets = tickets;
        },
        
    },
    //--
    actions : {
        async loadTickets( {commit }, ){
            let url = 'http://localhost:8000/api/v2/incident'
            const access_token =  'd3340738633cdbfb8a74ef96423008f01c425e76'
            let headers = {
                    "Accept"  : "application/json",
                    "Content-Type": "application/json",
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    'Authorization': `token ${access_token}`
                } 
            // save token
            // Initialize the access & refresh token in localstorage.      
            localStorage.clear();
            localStorage.setItem('token', access_token)
            //localStorage.setItem('refresh_token', data.refresh);
            console.log("header = ", headers)

            commit("setIsLoading", true)
            // fetch 
            let data = axios.get(url,)
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
            // Initialize the access & refresh token in localstorage.      
            localStorage.clear();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            //axios.defaults.headers.common['Authorization'] = `Bearer ${data.access}`;

        },       
    
    }
})