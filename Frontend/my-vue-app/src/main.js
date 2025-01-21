import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/HomePage.vue'
import BlankWindow from './components/BlankWindow.vue'
import ItemsForSale from './components/ItemsForSale.vue'

// Definir rutas
const routes = [
  { path: '/', component: HomePage },
  { path: '/blank', component: BlankWindow },
  { path: '/items-for-sale', component: ItemsForSale }
]

// Crear instancia de router
const router = createRouter({
  history: createWebHistory(),
  routes
});

// Crear instancia de la aplicación y usar router
const app = createApp(App)
app.use(router)
app.mount('#app')