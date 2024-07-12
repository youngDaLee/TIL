<template>
  <TodoHeader :appTitle="title"/>
  <TodoInput @add="addTodoItem"/>
  <TodoList :todoItems="todoItems" @remove="removeTodoItem"/>
</template>

<script>
import TodoHeader from '@/components/TodoHeader.vue';
import TodoInput from '@/components/TodoInput.vue';
import TodoList from '@/components/TodoList.vue';
import { useTodo } from './hooks/useTodo';

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
    const { 
      todoItems, 
      addTodoItem
      // fetchTodos, 
    } = useTodo();

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