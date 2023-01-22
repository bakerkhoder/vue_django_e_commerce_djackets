<template>
    <div  class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                     <img v-bind:src="product.get_image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>
                <p>{{ product.description }}</p>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>Price:</strong>${{ product.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                         <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                          <a class="button is-dark" @click="addToCart">Add to cart </a>
                    </div>

                </div>
                <div class="field has-addons mt-6">
                  
                    <div class="control">
                        <a  v-if="isInWhishlist(product)" class="button is-dark" @click="addToWhishList">Add to whishlist </a>
                        <a v-else class="button is-dark" @click="removeFromWhihList(product)">Remove from whishlist </a>

                    </div>
                            

                </div>

            </div>

        </div>
    </div>


</template>
<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

// data: function () {
//     return {
//         currentUrl: "",
//     };
// },
// created() {
//     this.currentUrl = window.location.href;
// },

export default{
    name:'Product',
    data(){
        return{
            whishlist:{
                items:[]
            },
            product:{},
            quantity:1,
            currentUrl:""
        }
    },
    mounted(){
        this.getProduct()
        
    },
    created() {
     this.currentUrl = window.location.href;
     this.whishlist = this.$store.state.whishlist;
 },

    methods:{
        
        removeFromWhihList(product) {
                this.whishlist.items = this.whishlist.items.filter(i => i.product.id !== product.id)
                localStorage.setItem('whishlist', JSON.stringify(this.$store.state.cart))
            },
       
        isInWhishlist(product){
            
            // console.log(this.whishlist)
            // console.log(this.whishlist.items)
            // for (item in (this.whishlist.items)){
            //     console.log(item.product)
            //       if(item.product.id == product.id){return true}
                  
            // } 
              var state =true
            this.whishlist.items.forEach(element => {
              
                if (element.product.id == product.id) 
                    state=false
            });
            return  state
        },
        async getProduct(){
            this.$store.commit('setIsLoading',true)
            const category_slug=this.$route.params.category_slug
            const product_slug= this.$route.params.product_slug
            await axios
            .get(`/api/v1/products/${category_slug}/${product_slug}`)
            .then(response=>
            {this.product=response.data
             document.title=this.product.name +' |Djackets'
            } )
            .catch(error=>{
                console.log(error)
            })
            this.$store.commit('setIsLoading', false)
        },
        addToCart(){
            if(isNaN(this.quantity) || this.quantity <1){
                this.quantity =1
            }

            axios
        
            const item ={
                product: this.product,
                quantity:this.quantity
            }
            this.$store.commit('addToCart',item)
            
            toast({

                message:'the product was added to the cart',
                type: 'is-success',
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right',
            })
        },
        addToWhishList() {
               if (isNaN(this.quantity) || this.quantity < 1) {
                   this.quantity = 1
               }

               const item = {
                   product: this.product,
            
               }
               
               this.$store.commit('addToWhishList', item)

               toast({

                   message: 'the product was added to the whishlist',
                   type: 'is-success',
                   dismissible: true,
                   pauseOnHover: true,
                   duration: 2000,
                   position: 'bottom-right',
               })
        }


    }
}
</script>