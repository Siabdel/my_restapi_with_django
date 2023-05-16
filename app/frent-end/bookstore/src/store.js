import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({

    state : {
        posts : [],
        post : {},
        isLoading : false,
        selectedPostId : false,
        postSaved : false,
    },

    getters : {
        getPostSelected : state => {
            state.post
            console.log("getters : getPostSelected" + state.post)
        },
        //get post
        getPost : state => state.post

    },

    mutations : {
        setPost(state, {post}){
            state.post = post;
        },
        setPosts(state, {posts}){
            state.posts = posts;
        },
        setPostAdded(state){
            state.postSaved = true;
        },
        setIsLoading(state, bool){
            state.isLoading = bool;
        },
        setSelectedPost(state, id){
            state.selectedPostId = id;
        },
    },
    actions : {

        async loadPosts( {commit }, ){
            
            //let url = `https://www.googleapis.com/posts/v1/volumes?q=search+vue.js&key=AIzaSyDCdbg3vdrRVokCr6E2-ADtbWT80NqMV_0`
            //let url = 'http://atlass.fr:93/apipro/directories/'
            //let url = 'https://randomuser.me/api/?nat=fr,Fr&results=10&seed=abc'
            let url = 'http://localhost:8000/api/v1/'
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

            commit("setIsLoading", true)
            // fetch 
            let data = axios.get(url,
                { 
                  headers : headers,
                })
            .then(response => response.data)
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
        //-- add post
        async addPost({commit}, post)
        {
            //validate saisie email, passwd 
            //authAPI.login(this.email, this.body)
            let url = 'http://localhost:8000/api/v1/'
            let headers = {
                    //'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8; multipart/form-data',
                    //'Content-Type': 'multipart/form-data',
                    'Content-Type': 'application/json',
                    //'withCredentials': true,
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    //'Authorization': `token ${access_token}`
            }
            console.log(headers)
            //Axios
            commit("setIsLoading", true)
            await axios.post(url, post)
            .then( () =>  {
                console.log("Add data :" + post.title)
                commit("setPostAdded", true )
            })
            .catch( (error) => {
                this.errors = []
                console.log("Api Erreur add post !!" + post.body + error)
            });
            // Initialize the access & refresh token in localstorage.      
            localStorage.clear();
            //localStorage.setItem('access_token', data.access);
        },
        // delete post
        async deletePost({commit}, post_id )
        {
            let url = 'http://localhost:8000/api/v1/' + `${post_id}`
            commit("setIsLoading", true)
            await axios.delete(url, post_id)
            .then( () =>  {
                console.log("Delete post !!" )
                this.errors = []
            })
            .catch( (error) => {
                this.errors = []
                console.log("Api Erreur post not deleted!!" + error)
            });
            // Initialize the access & refresh token in localstorage.      
        },
        // update post
        async updatePost({commit}, post)
        {
            let url = 'http://localhost:8000/api/v1/' + `${post.id}/`
            commit("setIsLoading", true)
            await axios.put(url, post)
            .then( () =>  {
                console.log("post updated !!" )
            })
            .catch( (error) => {
                console.log("Api Erreur not updated!!" + error)
            });
            // Initialize the access & refresh token in localstorage.      
        },
        // get post
        async loadPost({commit}, post_id){
            let url = 'http://localhost:8000/api/v1/' + `${post_id}/`
            commit("setIsLoading", true)
            return axios.get(url, post_id)
            .then(response => response.data) 
            .then(post => {
                commit("setSelectedPost", post.id)
                commit("setPost", {post})
                console.log("post title get == " +  post.title)
            })
            .catch( (error) => {
                console.log("Api Erreur not load ...!!" + error)
                console.log("Api Erreur not load ...!!" + post_id)
            });
            // Initialize the access & refresh token in localstorage.      
        }
    
    }
})