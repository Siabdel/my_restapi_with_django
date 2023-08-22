<template>
  <div class="container">
    <div class="row">
        <div class="col-md">
          <div class="jumbotron">
            <img alt="Vue logo" src="../assets/koutoubia.jpg"/>
            <p class=""> Menara Marrakech *** </p>
            <hr>
          </div>
        </div>
        <div class="col-md">
          <h3>Menu</h3>
          <ul>
            <li class="group-list-item">
              <router-link class="nav-link" to="/tlist"> 
                Liste des Incidents
              </router-link> 
            </li>
             <li class="group-list-item">
              <router-link class="nav-link" to="/add"> 
                Enregistre un ticket sur un incident constaté
              </router-link> 
            </li>
             <li class="group-list-item">
              <router-link class="nav-link" to="/"> 
                Appel de fond
              </router-link> 
            </li>
             <li class="group-list-item">
              <router-link class="nav-link" to="/"> 
                les documents
              </router-link> 
            </li>
          </ul>
        </div>
    </div>
   
  </div>
</template>


<script>
    export default {
        name: "HomePage",
        props : {
            msg:String,
        },
        created() {
        },
        methods:{
        }
    }
</script>