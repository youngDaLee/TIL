import { onBeforeMount, ref } from 'vue';

function useTodo() {
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

  // 라이프 사이클 API
  onBeforeMount(() => {
    todoItems.value = fetchTodos();
  });

  return { todoItems, addTodoItem }
}


export { useTodo }