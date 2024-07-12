<template>
  <ul>
    <li v-for="(item, index) in todoItems" :key="index">
      <span>{{ item }}</span>
      <button @click="removeTodo(item, index)">삭제</button>
    </li>
  </ul>
</template>

<script>
import { watch } from 'vue';


export default {
  props: ['todoItems'],
  setup(props, context) {
    function removeTodo(item, index) {
      context.emit('remove', item, index);
    }

    watch(props.todoItems, (newValue) => {
      // watch 지양 -> 데이터 추적이 어려워짐(어디에서 뭘 하는지...)
      // watch보다는 emit, props등을 이용해서 선언형으로 코딩하자! -> 코드 동작 추적
      console.log(newValue);
    });

    return { removeTodo }
  }
}
</script>

<style lang="scss" scoped>

</style>