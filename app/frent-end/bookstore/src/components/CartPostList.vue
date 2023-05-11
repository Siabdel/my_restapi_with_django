<template>
    <div>
        <h3> {{msg}}</h3>
        <div>
            <button @click.prevent="import_data"> Importer les posts </button>
        </div>
        <div  v-if="isLoading" class="spinner">
            <img src="" alt="">
            <div class="spinner-border text-danger" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <ul>
            <li v-for="(post, index) in posts" :key="index" class="list-unstyled"> 
            <div class="row">
                <div class="col-md-3">
                    <div class="card card-body">
                    <img :src="(post.thumbnail)?post.thumbnail:'#'"  />
                    </div>
                        
                </div>
                <div class="col-md-7">
                    <div class="card">
                        <div class="card-header">
                            <router-link 
                                :to="{'name': 'post-details', 'params': {'id' : post.id }}"> 
                                {{ post.author}} </router-link>
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
                <div class="col-md-2">
                    <button class="btn btn-warning btn-large">Ajouter au panier</button>
                </div>
            </div> 
            <hr/>
            </li>
        </ul>
    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.min.css';
    import { mapState, mapActions} from "vuex" 

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
            ...mapActions([ 'addPosts', ]),
        }

    }

</script>