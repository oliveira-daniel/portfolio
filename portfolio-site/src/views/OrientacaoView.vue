<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import ori from '../data/orientacoes.json'

const concluidas = computed(() => ori.filter((o: any) => o.situacao === 'Concluída'))
const aIniciar = computed(() => ori.filter((o: any) => o.situacao === 'A iniciar'))
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Orientações</h1>
  <p class="text-brand-dark/60 mb-8">Últimos 5 anos — PPG Ensino de Ciências (Unigranrio)</p>

  <section class="mb-8">
    <h2 class="text-xl font-bold text-brand-dark mb-4">Concluídas ({{ concluidas.length }})</h2>
    <div class="space-y-3">
      <GlassCard v-for="o in concluidas" :key="o.aluno">
        <p class="text-xs text-brand-green font-semibold mb-1">{{ o.ano }} · {{ o.tipo }}</p>
        <h3 class="font-semibold text-brand-dark">{{ o.aluno }}</h3>
        <p class="text-sm text-brand-dark/60">{{ o.titulo }}</p>
        <p class="text-xs text-brand-dark/40 mt-1">{{ o.programa }}</p>
      </GlassCard>
    </div>
  </section>

  <section v-if="aIniciar.length">
    <h2 class="text-xl font-bold text-brand-dark mb-4">Em andamento</h2>
    <GlassCard v-for="o in aIniciar" :key="o.aluno">
      <p class="text-xs text-brand-yellow font-semibold mb-1">{{ o.ano }} · {{ o.tipo }}</p>
      <h3 class="font-semibold text-brand-dark">{{ o.aluno }}</h3>
      <p class="text-sm text-brand-dark/60">{{ o.titulo }}</p>
    </GlassCard>
  </section>
</template>