<template>
    <div class="container">
        <div class="header">
            <a href="localhost:8080" class="btn btn-warning">
            <router-link class="nav-link" to="/add"> Ajouter article </router-link></a>|
        </div>
        <div  v-if="isLoading" class="spinner">
            <img src="" alt="">
            <div class="spinner-border text-danger" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <ul>
            <li v-for="(post, index) in getPosts" :key="index" class="list-unstyled"> 
            <div class="row">
                <div class="col-md-1">
                    <div class="card card-body">
                    <img :src="(post.thumbnail)?post.thumbnail:'#'"  />
                    </div>
                        
                </div>
                <div class="col-md-7">
                    <div class="card">
                        <div class="card-header">
                            <router-link 
                                :to="{'name': 'post-details', 'params': {'id' : post.id }}"> 
                                {{ post.id}} </router-link>
                        </div>
                        <div class="card-body">
                            <router-link 
                                :to="{'name': 'post-details', 'params': {'id' : post.id }}"> 
                                <h4 class="card-title">{{ post.title }}</h4>
                            </router-link>
                            <p> {{ post.publishedDate}}</p> 
                            <p> {{ (post.body)?post.body.slice(1, 300):''}} </p>
                        </div>
                        <div class="card-footer">
                            <p> <span 
                                v-for="createur, index in post.authors" :key="index">
                                {{createur}} , 
                                </span> </p> 
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-warning">
                        <a href="#" @click.prevent="getPost(post.id)"> Update </a>
                    </button>
                    <button class="btn btn-warning">
                        <a href="#" @click.prevent="delPost(post.id)"> Delete </a>
                    </button>
                     <button class="btn btn-warning">
                        <a href="#" @click.prevent="showPost(post.id)"> Show </a>
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
    import { mapState, mapActions, mapMutations, mapGetters} from "vuex" 

    export default {
        name : "CartPostList",
        beforeRouteLeave: (to, from, next) => {
            console.log("route beforeEnter ....");
            //this.url = to.path;
            next();
        },
        computed:{
            ...mapGetters(["getPosts", ]),
            ...mapState([ 'isLoading', 'posts']),
        },

        created(){
            this.loadPosts();
        },
        methods: {
            ...mapMutations(['setSelectedPost', ]),
            ...mapActions(['deletePost','loadPosts' ]),
            // suppression post
            delPost(postId){
                this.deletePost(postId);
                // reload post
                this.loadPosts()
                this.$router.push({ name: "Home"})
            },
            // get post to update
            getPost(post_id){
                console.log("getPost : selected post = " + post_id)
                this.setSelectedPost(post_id)
                this.$router.replace("/get/" + post_id)
            },
            // show post
            showPost(post_id){
                console.log("show : selected post = " + post_id)
                this.setSelectedPost(post_id)
                this.$router.push("/show/" + post_id)
            }
        }

    }

</script>