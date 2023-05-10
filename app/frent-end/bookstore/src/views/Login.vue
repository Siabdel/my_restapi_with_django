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
        <form method="post" @submit.prevent="onLogin" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />

          <input type="user.name" v-model="user.name" placeholder="Name" 
            required class="form-control input-lg"   />
          
          <input type="user.password" v-model="user.password" class="form-control input-lg"  
            placeholder="Password" required="" />
          
          
          <div class="pwstrength_viewport_progress"></div>
          
          
          <button type="submit" name="go" 
          class="btn btn-lg btn-primary btn-block">Se conneter</button>
          <div>
            <a href="#">Create account</a> or <a href="#">reset password</a>
          </div>
          
          
        </form>
        
        <div class="form-links">
          <a href="#">www.website.com</a>
        </div>
      </section>  
      </div>
      
      <div class="col-md-4"></div>
      

  </div> </template>
<script>
import axios from "axios";
// Regular expression from W3C HTML5.2 input specification:
var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

export default ({
    name : "VLogin",
    data : () => ({
        message : "",
        user :{
          name : null,
          email : null,
          password: null,
        },
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    methods :{
        
        onLogin(){
          if(this.user.name && this.isPassword(this.user.password) ){
            this.apiLogin()
          }else{
            console.log("votre email  n'est pas valide !!!")
            this.errors = "votre email  n'est pas valide !!!"
          }
        },

        apiLogin(){
            //validate saisie email, passwd 
            //authAPI.login(this.email, this.password)
            let url = 'http://localhost:8000/api/v1/rest-auth/login/'
            let headers = {
                    "Content-Type": "application/json",
                    //"withCredentials": true,
                    //'Authorization': `Bearer ${localStorage.getItem(access_token)}`,
                    //'Authorization': `token ${access_token}`
            }
            console.log(headers)
            const data = axios.post(url, { 
                  headers : headers,
                  method : 'POST',
                  body : JSON.stringify(this.user)

            })
            .then(res => res.json())
            .then( data =>  {
                localStorage.getItem('token', data)
                this.$router.push("/")
                console.log("Connected !!" + this.user.name + " et " + this.user.password)
                this.errors = []
            })
            .catch( () => {
                this.errors = []
                console.log("Api Erreur de connexion !!" + this.user.name + this.user.password)
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
          if(!this.user.password || this.user.password.length < 5){
            this.errors.push("password non valide nbre car < 5 !!") 
            console.log("password non valide nbre car < 5 !!" + passwd)
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