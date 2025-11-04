import { createRouter, createWebHistory } from 'vue-router'
import PacientesView from '../views/PacientesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/pacientes'
    },
    {
      path: '/pacientes',
      name: 'pacientes',
      component: PacientesView
    }
  ]
})

export default router