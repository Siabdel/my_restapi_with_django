import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({

    state : {
        posts : [],
        isLoading : false,
        selectedpostId : null,
    },

    getters : {
        getpostselected : state => {
            return state.posts.find( post => post.id === state.selectedpostId )
            //console.log("getpostselected : " + bb.volumeInfo.title)
        }
    },

    mutations : {
        setPosts(state, {posts}){
            state.posts = posts;
        },

        setIsLoading(state, bool){
            state.isLoading = bool;
        },
        setSelectedpost(state, id){
            state.selectedpostId = id;
        },

    },
    actions : {

        loadPosts( {commit }, ){
            
            //let url = `https://www.googleapis.com/posts/v1/volumes?q=search+vue.js&key=AIzaSyDCdbg3vdrRVokCr6E2-ADtbWT80NqMV_0`
            //let url = 'http://atlass.fr:93/apipro/directories/'
            //let url = 'https://randomuser.me/api/?nat=fr,Fr&results=10&seed=abc'
            let url = 'http://localhost:8600/api/v1/'
            const access_token =  'd3340738633cdbfb8a74ef96423008f01c425e76'
            // save token
            // Initialize the access & refresh token in localstorage.      
            localStorage.clear();
            localStorage.setItem('token', access_token)
            //localStorage.setItem('refresh_token', data.refresh);

            commit("setIsLoading", true)
            // fetch 
            let data = axios.get(url,
                { 
                  headers : {
                    "Accept"  : "application/json",
                    "Content-Type": "application/json",
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    'Authorization': `token ${access_token}`
                  },
                  method : 'GET',
                })
            .then(res => res.data)
            .then(data => {
                    commit("setIsLoading", false)
                    commit("setPosts", { posts : data })
                    // save token 
                    localStorage.setItem('token', access_token)
                    console.log("  posts loaded ..." +  data)
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
    
      // add post to base
    }
})