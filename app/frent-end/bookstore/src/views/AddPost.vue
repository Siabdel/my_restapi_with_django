<template>
  <div class="row" id="pwd-container">
    <div class="col-md-4"></div>
    
    <div class="col-md-4">
      <section class="login-form">
        <div v-if="errors.length" class="breadcrumb bg-white">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="(error, index) in errors"  :key=index class="text-warning"> {{ error }} !!</li>
          </ul>
        </div>
        <form method="post" @submit.prevent="savePost" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />

          <input type="post.title" v-model="post.title" placeholder="title" 
            required class="form-control input-lg"   />
          
          <textarea  v-model="post.body" class="form-control input-lg"  
            placeholder="body" required="" /> 
          
          <button type="submit" name="go" 
          class="btn btn-lg btn-primary btn-block">Add</button>
        </form>
      </section>  
      </div>
      
      <div class="col-md-4"></div>
      

  </div> </template>
<script>
import axios from "axios";
// Regular expression from W3C HTML5.2 input specification:
var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default ({
    name : "VAddPost",
    data : () => ({
        message : "",
        post :{
          title : null,
          email : null,
          body: null,
        },
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    methods :{
        savePost(){
            //validate saisie email, passwd 
            //authAPI.login(this.email, this.body)
            let url = 'http://localhost:8000/api/v1/blog/'
            let headers = {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8; multipart/form-data',
                    //'withCredentials': true,
                    //'Content-Type' : 'multipart/form-data',
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    //'Authorization': `token ${access_token}`
            }
            console.log(headers)
            /**
            const data = axios.post(url, { 
                  headers : headers,
                  method : 'POST',
                  body : JSON.stringify(this.post)

            })
            **/
            const data = axios.post(url, 
            {
              title : this.post.title,
              body:this.post.body,
            },
            )
            .then(res => res.data)
            .then( data =>  {
                localStorage.getItem('token', data)
                this.$router.push("/")
                console.log("Connected !!" + this.post.title + " et " + this.post.body)
                this.errors = []
            })
            .catch( (error) => {
                this.errors = []
                console.log("Api Erreur de connexion login !!" + error)
                this.errors.push("Il y a une erreur dans votre adresse email ou le mot de passe")
            });
            // Initialize the access & refresh token in localstorage.      
            localStorage.clear();
            localStorage.setItem('access_token', data.access);
        },
    

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