<template>
  <TodoHeader :appTitle="title"/>
  <TodoInput @add="addTodoItem"/>
  <TodoList :todoItems="todoItems" @remove="removeTodoItem"/>
</template>

<script>
import TodoHeader from '@/components/TodoHeader.vue';
import TodoInput from '@/components/TodoInput.vue';
import TodoList from '@/components/TodoList.vue';
import { onBeforeMount, ref } from 'vue';

export default {
  components: {
    TodoHeader,
    TodoInput,
    TodoList,
  },
  data() {
    return {
      title: '할일 앱',
    }
  },
  setup() {
    // data
    const todoItems = ref([]);

    // methods
    function fetchTodos() {
      const result = [];
      for (let i = 0; i < localStorage.length; i++) {
        const todoItem = localStorage.key(i);
        // items.value.push(todoItem);
        result.push(todoItem);
      }
      return result;
    }

    function addTodoItem(todo) {
      todoItems.value.push(todo);
      localStorage.setItem(todo, todo);
    }

    console.log('setup called')
    // 라이프 사이클 API
    onBeforeMount(() => {
    console.log('mount called')
    todoItems.value = fetchTodos();
    });

    return { todoItems, addTodoItem }
  },
  methods: {
    removeTodoItem(item, index){
      this.todoItems.splice(index, 1);
      localStorage.removeItem(item, item);
    },
  }
}
</script>

<style lang="scss" scoped>

</style>