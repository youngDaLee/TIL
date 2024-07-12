<template>
  <div>
    <input type="text" v-model="todoInput">
    <button @click="addTodo">추가</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
    setup() {
      // data
      const todoInput = ref('');

      // method
      function addTodo() {
        const todo = todoInput.value;
        localStorage.setItem(todo, todo);
      }

      return { todoInput, addTodo }
    }
  }
</script>

<style lang="scss" scoped>

</style>