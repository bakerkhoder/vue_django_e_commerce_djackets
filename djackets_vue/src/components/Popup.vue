<template>
   <transition name="fade">
      <div class="vue-modal" v-show="open">
         <transition name="drop-in">
            <div class="vue-modal-inner" v-show="open">
                <div class="vue-modal-content">
                    <slot />
                     <form @submit.prevent="submitForm">
                       <div class="flex">
                          <input class="name" type="text" v-model="name">
                          <label for="pic"><img :src="get_profile_pic()" class="profile_pic" /></label>
                          <input class="input_image" id="pic" type="file" @change="handleFileUpload( $event )">

                      </div> 
                      <button class="button" type="button" @click="$emit('close')"> close</button>
                      <button class="button">update</button>
                   </form>
                </div>
            </div>
         </transition>    
      </div>
   </transition>

</template>

<script>
import axios from 'axios'
 export default{
   data() {
      return {
         name:this.profile.name,
         profile: {},
         file:''
         
      }
   },
   beforeCreate(){
      this.profile = this.$store.state.profile

   },
   mounted() {
   
      this.profile = this.$store.state.profile
   },
   methods: {
 
      submitForm() {
       
            const formData = {
               username:this.profile.name,
               name: this.name,
               file: this.file,

            }

            axios
               .post("/api/v1/updateprof/", formData, {
                  headers: {
                     'Content-Type': 'multipart/form-data'
                  }
               })
               .then(response => {
                 
                  this.$router.push('/')
                  console.log(response.data.profileimg)
                  console.log(JSON.stringify(response.data))
                  localStorage.removeItem("profile")
                  localStorage.setItem("profile", JSON.stringify(response.data))
                  window.location.reload()

               })
               .catch(error => {
                  if (error.response) {
                    console.log(error)
                  }
               })
         
      },


      handleFileUpload(event) {
         this.file = event.target.files[0];
      },

      get_profile_pic() {
         return 'http://127.0.0.1:8000' + this.profile.profileimg
      }
   },
    props:{
        open:{
            type:Boolean,
            required: true
        }
    }
 
 }
</script>

<style scoped>
::after{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
 }

 .vue-modal{
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    background-color: rgba(0,0,0,0.4);
    z-index: 11;
    height: 100%;
 }
 .vue-modal-inner{
    max-width: 500px;
    margin: 2rem auto;
 }
 
 .vue-modal-content{
    margin-top: 30%;
    position: relative;
    background-color: rgb(51, 48, 48);
    border: 1px solid rgba(0,0,0,0.3);
    padding: 1 rem;
    background-clip: border-box;
    border-radius: 0.3rem;

 }
 .fade-enter-active,
 .fade-leave-active{
     transition: opacity 0.5s;

 }
 .fade-enter-from,
 .fade-leave-to{
    opacity: 0;
 }
 
 .profile_pic{
   width: 50%;
   border-radius: 50px;
  
 }
 .name{
   width: 70px;
   height: 10%;
   margin-top: 15%;
   margin-left: 10px;
   margin-right: 20%;
   color: rgb(248, 247, 247);
   background-color: black;
   font-size: large;
 }

 .flex{
   display: flex;
 }

 .button{
   height: 30px;
   width: 55px;
   margin-left: 10px;
   margin-bottom: 5px;
   color: aliceblue;
   background-color: rgb(14, 13, 13);
   box-shadow: 3px 2px 1px rgb(66, 65, 65);
 }

 .input_image{
   display: none;
 }



 /* .drop-in-enter-acive,
 .drop-in-leave-acive{
    transition: all 0.3s ease-out;
   
 }

 .drop-in-enter-from,
 .drop-in-leave-to{
    opacity: 0;
    transform: translateY(-50px);

 } */
</style>