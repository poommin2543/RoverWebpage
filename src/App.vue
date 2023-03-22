<template>
  <v-app>
    <v-main>
      <router-view>
      </router-view>
    </v-main>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  watch: {
    $route(to) {
      document.title = `APPLICATION_NAME - ${to.meta.title}`;
      const link = document.querySelector("[rel='icon']")
      link.setAttribute('href', to.meta.icon)
    }
  }
}

</script>
