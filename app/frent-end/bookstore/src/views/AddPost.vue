<template>
  <div class="container-fluid">
    <div class="col-md-12">
      <section class="login-form">
        <div v-if="errors.length > 0" class="breadcrumb bg-white">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="(error, index) in errors"  :key=index class="text-warning"> {{ error }} !!</li>
          </ul>
        </div>
        <form v-if="showForm" method="post" @submit.prevent="savePost" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />
          <div class="form-control"> 
            Author : <input type="number" v-model="article.author" placeholder="author" 
            required class="form-control input-lg"   />
          </div>
          <div class="form-control">
            Title :
            <input type="post.title" v-model="article.title" placeholder="title" 
            required class="form-control input-lg"   />
          </div>

          <div class="form-control">
            Description  :<textarea  v-model="article.body" rows="10" class="form-control input-lg"  
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
import { mapActions, } from "vuex"


export default ({
    name : "VPost",
    beforeRouteLeave: (to, from, next) => {
     console.log("route beforeEnter ....");
     //this.url = to.path;
     next();
    },
    data : () => ({
        message : "",
        article : {
          title : "",
          body : "", 
          author : "",
        },
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    computed:{

    },
    //Methods
    methods :{
      ...mapActions(["addPost", "loadPosts", ]),

      savePost(){
        // save post
        if(this.validateForm()){
          this.addPost(this.article)
          //console.log("Ajout Ajout ...")
        }
          // return to home
          this.$router.push("/")
      },

      // check for valid email adress

      validateForm(){
        if(!this.article.title || this.article.body.length < 1){
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