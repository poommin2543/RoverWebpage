import Vue from "vue";
import VueRouter from "vue-router";
import homepageView from '../views/HomepageView.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'homepageView',
        component: homepageView
    },
    
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router