import { ref } from "vue";

function useMessage() {
  // data
  const message = ref('hello');

  // methods
  function changeMessage() {
    message.value = 'hi';
  }

  return { message, changeMessage }
}

export { useMessage }