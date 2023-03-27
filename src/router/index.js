import Vue from "vue";
import VueRouter from "vue-router";
import homepageView from '../views/HomepageView.vue'
import loginView from '../views/LoginPage.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/home',
        name: 'homepageView',
        component: homepageView,
        meta: {
            title: "Login",
            icon:"../assets/img/Rovericon.svg" 
          }
    },
    {
        path: '/',
        name: 'loginView',
        component: loginView,
        
    },
    
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router