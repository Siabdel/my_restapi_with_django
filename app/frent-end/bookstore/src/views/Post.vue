<template>
  <div class="container-fluid">
    <div class="col-md-12">
      <h2> {{ getPost.title }} {{ selectedPostId }} .. </h2>
      <section class="login-form">
        <div v-if="errors.length > 0" class="breadcrumb bg-white">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="(error, index) in errors"  :key=index class="text-warning"> {{ error }} !!</li>
          </ul>
        </div>
        <form v-if="showForm" method="post" @submit.prevent="savePost(getPost)" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />
          <div class="form-control"> 
            Author : <input type="number" v-model="getPost.author" placeholder="author" 
            required class="form-control input-lg"   />
          </div>
          <div class="form-control">
            Title :
            <input type="post.title" v-model="getPost.title" placeholder="title" 
            required class="form-control input-lg"   />
          </div>

          <div class="form-control">
            Description  :<textarea  v-model="getPost.body" rows="10" class="form-control input-lg"  
            placeholder="body" required="" /> 
          </div>
          
          <button type="submit" name="go" 
          class="btn btn-lg btn-primary btn-block">Enregistrer</button>
        </form>
      </section>  
    </div>
  </div> 
</template>

<script>
import { mapActions, mapGetters, mapMutations, mapState} from "vuex"


export default ({
    name : "VPost",
    beforeRouteLeave: (to, from, next) => {
     console.log("route beforeEnter ....");
     //this.url = to.path;
     next();
    },
    data : () => ({
        message : "",
        postId : "",
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    computed:{
      ...mapGetters(["getPost", "getSelectedPostId", ]),
      ...mapState(["selectedPostId", "post", ]),

    },
    created(){
      this.postId = this.$route.params.postId
      //-- toto
      if(this.selectedPostId){
        this.loadPost(this.selectedPostId)
        // si load post reussi
        if( this.getPost.title ){
          this.setSelectedPost(this.postId)
          //this.loadPost(this.selectedPostId);
          this.showForm = true
          // charger le poste a l'ecran
          console.log("load Post ...", this.postId)
          console.log("post title ...", this.post.title)
          // affichage
        }
      }else{
          console.log("Article non trouvé !")
          this.errors.push("Article non trouvé !")
          this.showForm = false
        }
    },
    //Methods
    methods :{
      ...mapMutations(["setSelectedPost",]),
      ...mapActions(["addPost", "updatePost","loadPost", ]),

      savePost(post){
        // save post
        if(this.postId && this.validateForm()){
          this.updatePost(post)
          console.log("il sagit dune mise a jour ...", post.id)
        }
          // return to home
          this.$router.push("/")
      },

      // check for valid email adress

      validateForm(){
        if(!this.getPost.title || this.getPost.body.length < 1){
          this.errors.push("form non valide ") 
          console.log("form not valid !!" )
          return false
        }else {
          return true
        }
      },
      // watching nested property
    },
})
</script>