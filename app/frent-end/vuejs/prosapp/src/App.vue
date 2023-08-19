<template>
   <!-- Navigation-->
   <div class="container">
      <CHeader/>  
      <div class="jumbotron">
        <h1 class="display-4"> {{ msg }} </h1>
      </div>
      <hr> 
      <router-view> </router-view>
   </div>
  </template>

<script>

import CHeader from "./views/CHeader.vue"
import {mapActions, } from "vuex" 

export default {
  name: 'App',
  components: { CHeader },
  data(){
    return {
      msg : "PRO syndic Plateforme"
    }
  },
  created(){
    this.loadTickets()
  },
  methods:{
    // load Tickets is now access as method
    ...mapActions(['loadTickets', ]),
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
article {
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