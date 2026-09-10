import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
  { path: '/trajetoria', name: 'trajetoria', component: () => import('../views/TrajetoriaView.vue') },
  { path: '/servicos', name: 'servicos', component: () => import('../views/ServicosView.vue') },
  { path: '/academico', name: 'academico', component: () => import('../views/AcademicoView.vue') },
  { path: '/projetos', name: 'projetos', component: () => import('../views/ProjetosView.vue') },
  { path: '/blog', name: 'blog', component: () => import('../views/BlogView.vue') },
]

export default createRouter({
  history: createWebHistory('/portfolio/'),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})