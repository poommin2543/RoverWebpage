import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import vuetify from './plugins/vuetify'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import vuetify from './plugins/vuetify'
import * as VueGoogleMaps from "vue2-google-maps"
import VueGamepad from 'vue-gamepad';
import 'material-design-icons-iconfont'
Vue.use(VueGamepad);
Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyD553x-on9CsDmxWaD3rfKg2l3MX48kov8",
    // libraries: "places"
    libraries: "places,drawing,visualization"
  }
});
Vue.use(Vuetify)
Vue.config.productionTip = false
// Vue.use(Vuetify)
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
