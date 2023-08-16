<template>
    <div class="container">
        <a class="btn btn-success" href="#" onclick="window.history.back();">return </a>
        <article class="cs_article"> 
            <h2> {{ getPost.title }}</h2>
            <br>
            <h4>Author :  {{ getPost.author }}</h4>
            <h4> Created le {{ getPost.created }}</h4>

            <p> {{ getPost.body }}</p>
        </article>
    </div>
</template>

<script>

import { mapActions, mapGetters, mapMutations} from "vuex"

export default {
    name : "DPost",
    data : () => ({
       msg:"",
    }),
    // created
    created(){
        const postId = this.$route.params.postId
        if(postId){
            this.loadPost(postId)
            this.setSelectedPost(postId)
        }

    },
    // Computed
    computed : {
      ...mapGetters(["getPost", ]),
    },
    //methodes
    methods:{
        ...mapActions(["loadPost"]),
        ...mapMutations(["setSelectedPost",]),
    }

}
</script>

<style>
.cs_article, {
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    font-family: "Open Sans",Lato,sans-serif !important;
    font-weight: 300;
    color: #454c55;
    -moz-font-feature-settings: "liga" 0;
}
:root {
    --sash-size: 4px;
}
*, *:before, *:after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -webkit-overflow-scrolling: touch;
}
*, *:before, *:after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -webkit-overflow-scrolling: touch;
}

</style>