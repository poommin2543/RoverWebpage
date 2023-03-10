import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ControlView from '../views/ControlView.vue'
import Map from '../components/Map.vue'
import homepageView from '../views/HomepageView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/C',
    name: 'ControlView',
    component: ControlView
  },
  {
    path: '/home',
    name: 'homepageView',
    component: homepageView
  },
  {
    path: '/map',
    name: 'map',
    component: Map
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
