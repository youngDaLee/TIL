<template>
  <AppHeader 
  v-bind:appTitle="message"
  v-on:change="changeMessage"
  >
  </AppHeader>

</template>

<script>
import AppHeader from './components/AppHeader.vue'

export default {
  components: {
    // 'AppHeader': AppHeader,
    AppHeader
  },
  data() {
    return {
      message: '앱헤더 컴포넌트',
    }
  },
  methods: {
    changeMessage() {
      this.message='변경됨'
    }
  }
}
</script>

<style scoped>

</style>