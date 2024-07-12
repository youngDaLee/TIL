<template>
  <div>
    <p>{{ message }}</p>
    <button @click="changeMessage">change</button>
  </div>
</template>

<script>
import { useMessage } from './hooks/useMessge';

  export default {
    setup(){
      // data
      const { message, changeMessage } = useMessage();
      return { message, changeMessage }
    }
    // data() {
    //   return {
    //     message: 'hello'
    //   }
    // },
    // methods: {
    //   changeMessage() {
    //     this.message = 'hi'
    //   }
    // }
  }
</script>

<style lang="scss" scoped>

</style>