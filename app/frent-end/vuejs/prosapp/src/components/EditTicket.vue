
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
        <form v-if="showForm" method="ticket" @submit.prevent="saveTicket" >
          <img src="http://i.imgur.com/RcmcLv4.png" class="img-responsive" alt="" />
          <div class="form-control"> 
            Author : <input type="number" v-model="getSelectedTicket.author" placeholder="author" 
            required class="form-control input-lg"   />
          </div>
          <div class="form-control">
            Title :
            <input type="getSelectedTicket.title" v-model="getSelectedTicket.title" placeholder="title" 
            required class="form-control input-lg"   />
          </div>

          <div class="form-control">
            Description  :<textarea  v-model="getSelectedTicket.comment" rows="10" class="form-control input-lg"  
            placeholder="comment" required="" /> 
          </div>
          
          <button type="submit" name="go" 
          class="btn btn-lg btn-primary btn-block">Enregistrer</button>
        </form>
      </section>  
    </div>
  </div> 
</template>

<script>
import { mapActions, mapGetters, } from "vuex"


export default ({
    name : "EditTicket",
    data : () => ({
        message : "",
        ticket : {},
        errors : [], 
        showForm : true,
        isSaved : false,
        loggedIn : false,
    }),
    //computed
    computed :{
      ...mapGetters(['getSelectedTicket', ])
    },
    //created
    created() {
      const ticket_id = this.$route.params.ticketId
      this.loadTicket(ticket_id)
      //console.log("mon ticket = ", this.getSelectedTicket.title)
    },

    //Methods
    methods :{
      ...mapActions(["loadTicket", "updateTicket", ]),

      saveTicket(){
        // save ticket
        if(this.validateForm()){
          console.log("Ajout ticket  ...", this.getSelectedTicket)
          this.updateTicket(this.getSelectedTicket)
        }
          // return to home
          this.$router.push("/")
      },

      // check for valid email adress

      validateForm(){
        if(!this.getSelectedTicket.title || this.getSelectedTicket.comment.length < 1){
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