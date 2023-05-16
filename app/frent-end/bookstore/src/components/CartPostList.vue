<template>
    <div>
        <h3> {{msg}}</h3>
        <a href="localhost:8080" class="btn btn-warning">
        <router-link class="nav-link" to="/add"> Ajouter article </router-link></a>|
        <div  v-if="isLoading" class="spinner">
            <img src="" alt="">
            <div class="spinner-border text-danger" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <ul>
            <li v-for="(post, index) in posts" :key="index" class="list-unstyled"> 
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
                </div>
            </div> 
            <hr/>
            </li>
        </ul>
    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.min.css';
    import { mapState, mapActions, mapMutations} from "vuex" 

    export default {
        name : "CartPostList",
        props : {
                msg : String 
                },
                
        created(){
            console.log("Mon Contacte ici")
        },
        computed:{
            ...mapState([ 'isLoading', 'posts']),
        },
        methods: {
            ...mapMutations(['setSelectedPost', ]),
            ...mapActions(['deletePost', ]),
            // suppression post
            delPost(postId){
                this.deletePost(postId);
                this.$router.push("/")

            },
            getPost(post_id){
                console.log("getPost : selected post = " + post_id)
                this.setSelectedPost(post_id)
                this.$router.push("/get/" + post_id)
            }
        }

    }

</script>