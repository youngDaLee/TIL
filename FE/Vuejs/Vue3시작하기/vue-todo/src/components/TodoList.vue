<template>
  <ul>
    <li v-for="(item, index) in items" :key="index">{{ item }}</li>
  </ul>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const items = ref(['apple', 'samsung', 'inflearn']);

    return { items }
  }
}
</script>

<style lang="scss" scoped>

</style>