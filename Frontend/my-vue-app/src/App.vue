<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* Estilos globales */
html, body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f8f8f8; /*si cambio este cambia el color del fondo*/
}

/* Estilos específicos */
.blank-window {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f0f0;
}

.blank-window h1 {
  color: #333;
  font-size: 2rem;
  margin-bottom: 1rem;
}

.blank-window a {
  color: #42b983;
  text-decoration: none;
  font-size: 1.2rem;
}

.blank-window a:hover {
  text-decoration: underline;
}
</style>