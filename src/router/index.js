import Vue from "vue";
import VueRouter from "vue-router";
import homepageView from '../views/HomepageView.vue'
import loginView from '../views/LoginPage.vue'
import loginnewView from '../views/LoginPagenew.vue'
import database from '../views/databases.vue'

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
    {
        path: '/login',
        name: 'login',
        component: loginnewView,
        
    },
    {
        path: '/database',
        name: 'database',
        component: database,
        
    },
    
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router