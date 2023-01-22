<template>
    <div class="home">
        <section class="hero is-meduim is-dark mb-6">
            <div class="hero-body  has-text-centered">
                <p class="title mb-6">
                    welcome to Whishlist Djackets
                </p>
                <p class="subtitle">
                    The best jacket store online
                </p>
            </div>
        </section>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">Favorite Products</h2>
            </div>
            <!-- <tr v-for="item in whishlist.items" v-bind:key="item.product.id">
                <td>{{ item.product.name }}</td>
                <td>${{ item.product.price }}</td>
                 <img  :src="item.product.get_image">
            </tr> -->
            

            <ProductBox v-for="item in whishlist.items" v-bind:key="item.product.id" v-bind:product="item.product"  v-on:removeFromWhishList="removeFromWhishList" />
             
            <!-- <CartItem v-for="item in whishlist.items" v-bind:key="item.product.id" v-bind:initialItem="item" /> -->

        </div>

    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
    name: "HomeView",
    data() {
        return {
            whishlist: {
                items: []
            }
        };
    },
    mounted() {
        this.whishlist = this.$store.state.whishlist;
    },
    methods: {
        removeFromWhishList(item) {
            this.whishlist.items = this.whishlist.items.filter(i => i.product.id !== item.product.id)
        }
    },
    components: { ProductBox }
}
</script>


