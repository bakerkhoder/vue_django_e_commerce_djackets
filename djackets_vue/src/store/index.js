import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      items:[],

    },
    profile:{},
    whishlist:{
      items:[],
    },
    isAuthenticated:false,
    token:'',
    isLoading:false
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('cart')){
        state.cart=JSON.parse(localStorage.getItem('cart'))
      }
      else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
      }
       if(localStorage.getItem('whishlist')){
        state.whishlist=JSON.parse(localStorage.getItem('whishlist'))
      }
      else{
        localStorage.setItem('whishlist',JSON.stringify(state.whishlist))
      }

      if(localStorage.getItem('token')){
        state.token= localStorage.getItem('token')
        state.isAuthenticated= true
      }
      else{
        state.token='',
        state.isAuthenticated=false
      }
       if(localStorage.getItem('profile')){
        state.profile=JSON.parse(localStorage.getItem('profile'))
      }
    },
    addToCart(state,item){
      const exists=state.cart.items.filter(i => i.product.id === item.product.id)

      if(exists.length){
        exists[0].quantity=parseInt(exists[0].quantity)+parseInt(item.quantity)
      }else{
        state.cart.items.push(item)
      }
      localStorage.setItem('cart',JSON.stringify(state.cart))
    },
    addToWhishList(state,item){
      const exists=state.whishlist.items.filter(i => i.product.id === item.product.id)

      if(exists.length){
        exists[0].quantity=parseInt(exists[0].quantity)+parseInt(item.quantity)
      }else{
        state.whishlist.items.push(item)
      }
      localStorage.setItem('whishlist',JSON.stringify(state.whishlist))
    },
    setIsLoading(state,status){
      state.isLoading =status
    },
    setToken(state,token){
      state.token=token
      state.isAuthenticated=true
    },
    removeToken(state){
      state.token=''
      state.isAuthenticated=false
    },
    clearCart(state){
      state.cart={items:[]}
      localStorage.setItem('cart',JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
