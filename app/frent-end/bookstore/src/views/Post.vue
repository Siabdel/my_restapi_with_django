<template>
  <div class="row" id="pwd-container">
    <div class="col-md-8">
      <h2> {{ getPost.title }}</h2>
      <section class="login-form">
        <div v-if="errors.length" class="breadcrumb bg-white">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="(error, index) in errors"  :key=index class="text-warning"> {{ error }} !!</li>
          </ul>
        </div>
        <form method="post" @submit.prevent="updatePost(post)" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />

          <input type="number" v-model="getPost.author" placeholder="author" 
            required class="form-control input-lg"   />
          <input type="post.title" v-model="getPost.title" placeholder="title" 
            required class="form-control input-lg"   />
          
          <textarea  v-model="getPost.body" class="form-control input-lg"  
            placeholder="body" required="" /> 
          
          <button type="submit" name="go" 
          class="btn btn-lg btn-primary btn-block">Add</button>
        </form>
      </section>  
    </div>
  </div> 
</template>

<script>
import { mapActions, mapGetters, mapState} from "vuex"

// Regular expression from W3C HTML5.2 input specification:
var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default ({
    name : "VPost",
    data : () => ({
        message : "",
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    computed:{
      ...mapGetters(["getPost", "getPostSelected"]),
      ...mapState(["selectedPostId", "post", ]),

    },
    created(){
      this.loadPost(this.selectedPostId);
      console.log("load Post ...", this.post)
    },
    //Methods
    methods :{

      ...mapActions(["updatePost","loadPost" ]),

      // check for valid email adress
      isEmail(value) {
        if (emailRegExp.test(value)){
          return true
        }else {
              this.errors.push("Vote email n'est pas valide ")
        }
      },

      isPassword(passwd){
        if(!this.post.body || this.post.body.length < 5){
          this.errors.push("body non valide nbre car < 5 !!") 
          console.log("body non valide nbre car < 5 !!" + passwd)
          return false
        }else {
          return true
        }
      },
      // watching nested property
      validate_email(event) {
        console.log("computed validate email" + event.value )
        return this.isEmail("email", event.value) 
      },
    },
})
</script>