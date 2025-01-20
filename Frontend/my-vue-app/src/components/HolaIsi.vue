<!-- src/components/HelloWorld.vue -->
<template>
    <div class="hello">
      <h1>{{ message }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      message: String
    }
  }
  </script>
  
  <style scoped>
  .hello {
    font-family: Arial, sans-serif;
    color: #42b983;
  }
  </style>