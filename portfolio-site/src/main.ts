import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

const routes = [
  { path: '/', name: 'home', component: () => import('./views/HomeView.vue') },
  { path: '/publicacoes', name: 'publicacoes', component: () => import('./views/PublicacoesView.vue') },
  { path: '/projetos', name: 'projetos', component: () => import('./views/ProjetosView.vue') },
  { path: '/consultoria', name: 'consultoria', component: () => import('./views/ConsultoriaView.vue') },
  { path: '/orientacao', name: 'orientacao', component: () => import('./views/OrientacaoView.vue') },
  { path: '/blog', name: 'blog', component: () => import('./views/BlogView.vue') },
]

const router = createRouter({ history: createWebHistory(), routes })

createApp(App).use(router).mount('#app')