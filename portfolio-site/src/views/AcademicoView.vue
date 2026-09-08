<script setup lang="ts">
import { computed, ref } from 'vue'
import { BookOpenText, Building2, CalendarDays, ChevronDown, Info, Users } from 'lucide-vue-next'
import GlassCard from '../components/GlassCard.vue'
import QualisChart from '../components/QualisChart.vue'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import ori from '../data/orientacoes.json'

const tab = ref<'geral' | 'publicacoes' | 'orientacoes' | 'grupos'>('geral')

const tabs = [
  { id: 'geral', label: 'Visão Geral' },
  { id: 'publicacoes', label: 'Publicações' },
  { id: 'orientacoes', label: 'Orientações' },
  { id: 'grupos', label: 'Grupos de Pesquisa' },
]

const artigos = computed(() => pubs.filter((p: any) => p.tipo === 'artigo'))
const artigosSemC = computed(() => artigos.value.filter((p: any) => p.qualis !== 'C'))
const capitulos = computed(() => pubs.filter((p: any) => p.tipo === 'capitulo'))
const anais = computed(() => pubs.filter((p: any) => ['anais', 'resumo', 'resumo_expandido'].includes(p.tipo)))

const qualisCount = computed(() => {
  const c: Record<string, number> = {}
  for (const a of artigosSemC.value) {
    c[a.qualis] = (c[a.qualis] || 0) + 1
  }
  return c
})

const tipos = ['artigo', 'capitulo', 'anais', 'resumo', 'resumo_expandido']
const label: Record<string, string> = {
  artigo: 'Artigos em periódicos',
  capitulo: 'Capítulos de livro',
  anais: 'Anais completos',
  resumo: 'Resumos',
  resumo_expandido: 'Resumos expandidos',
}

const openSections = ref<string[]>(['artigo'])

function toggleSection(t: string) {
  openSections.value = openSections.value.includes(t)
    ? openSections.value.filter((s) => s !== t)
    : [...openSections.value, t]
}

const grouped = computed(() => {
  const map: Record<string, any[]> = {}
  for (const t of tipos) map[t] = []
  for (const p of pubs) if (map[p.tipo]) map[p.tipo].push(p)
  return map
})

const concluidas = computed(() => ori.filter((o: any) => o.situacao === 'Concluída'))
const aIniciar = computed(() => ori.filter((o: any) => o.situacao === 'A iniciar'))

const grupos = [
  { nome: 'GPIAE — IA na Educação', instituicao: 'DEGC/UFSC', periodo: '2025–Atual', descricao: 'Grupo multidisciplinar em Inteligência Artificial na Educação.' },
  { nome: 'Logística Integrada — otimização e simulação', instituicao: 'UFSC', periodo: '2011–2013', descricao: 'Localização de centrais de inteligência e redes dinâmicas de transporte.' },
  { nome: 'Logística Humanitária', instituicao: 'UFSC', periodo: '2013–2018', descricao: 'Transporte dinâmico em situações de emergência, evitando rupturas na rede e ponderando custo x risco de ruptura.' },
  { nome: 'Tecnologias Digitais e Recursos Didáticos no Ensino de Ciências e Matemática', instituicao: 'Unigranrio', periodo: '2021–Atual', descricao: 'Macroprojeto PPG Ensino de Ciências Unigranrio.' },
  { nome: 'Extração de Informações Implícitas da Web', instituicao: 'Unigranrio', periodo: '2021–2022', descricao: 'QA sobre dados estruturados/não-estruturados; FUNADESP.' },
  { nome: 'Recursos de Acessibilidade com Arduino', instituicao: 'Unigranrio', periodo: '2020–2021', descricao: 'Soluções de baixo custo para cegos/baixa visão; FUNADESP.' },
]

type Grupo = (typeof grupos)[number]
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Acadêmico</h1>
  <p class="text-brand-dark/60 mb-6">Últimos 5 anos</p>

  <div class="flex gap-2 mb-8 flex-wrap">
    <button
      v-for="t in tabs"
      :key="t.id"
      @click="tab = t.id"
      class="px-4 py-2 rounded-full text-sm font-semibold transition-colors"
      :class="tab === t.id
        ? 'bg-brand-green text-white'
        : 'glass text-brand-dark/70 hover:bg-brand-green/20'"
    >
      {{ t.label }}
    </button>
  </div>

  <div v-if="tab === 'geral'">
    <section class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
      <GlassCard>
        <p class="text-3xl font-bold text-brand-green">{{ artigos.length }}</p>
        <p class="text-sm text-brand-dark/60">Artigos</p>
      </GlassCard>
      <GlassCard>
        <p class="text-3xl font-bold text-brand-green">{{ capitulos.length }}</p>
        <p class="text-sm text-brand-dark/60">Capítulos</p>
      </GlassCard>
      <GlassCard>
        <p class="text-3xl font-bold text-brand-green">{{ anais.length }}</p>
        <p class="text-sm text-brand-dark/60">Em anais</p>
      </GlassCard>
      <GlassCard>
        <p class="text-3xl font-bold text-brand-green">{{ concluidas.length }}</p>
        <p class="text-sm text-brand-dark/60">Orientações</p>
      </GlassCard>
    </section>

    <section>
      <h2 class="text-xl font-bold text-brand-dark mb-4">Qualis (artigos, exceto C)</h2>
      <QualisChart :counts="qualisCount" />
      <div class="flex gap-4 flex-wrap mt-4">
        <GlassCard v-for="(q, label) in qualisCount" :key="label">
          <p class="text-2xl font-bold text-brand-green">{{ q }}</p>
          <p class="text-sm text-brand-dark/60">Qualis {{ label }}</p>
        </GlassCard>
      </div>
    </section>
  </div>

  <div v-else-if="tab === 'publicacoes'">
    <div class="space-y-3">
      <GlassCard v-for="t in tipos" :key="t">
        <button
          @click="toggleSection(t)"
          class="w-full flex items-center justify-between gap-2 text-left"
        >
          <span class="flex items-center gap-2">
            <h2 class="text-xl font-bold text-brand-dark">{{ label[t] }}</h2>
            <span class="badge badge-yellow">{{ grouped[t].length }}</span>
          </span>
          <ChevronDown
            class="w-5 h-5 text-brand-green shrink-0 transition-transform"
            :class="openSections.includes(t) ? 'rotate-180' : ''"
          />
        </button>
        <div v-if="openSections.includes(t)" class="space-y-3 mt-3">
          <GlassCard v-for="p in grouped[t]" :key="p.titulo">
            <div class="flex flex-wrap gap-1.5 mb-1">
              <span class="badge badge-green">{{ p.ano }}</span>
              <span v-if="p.qualis.startsWith('A')" class="badge badge-green">Qualis {{ p.qualis }}</span>
              <span v-else-if="p.qualis.startsWith('B')" class="badge badge-yellow">Qualis {{ p.qualis }}</span>
            </div>
            <h3 class="font-semibold text-brand-dark">{{ p.titulo }}</h3>
            <div class="flex items-start gap-2 text-sm text-brand-dark/60 mt-1">
              <Users class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
              <span>{{ p.autores }}</span>
            </div>
            <div class="flex items-start gap-2 text-xs text-brand-dark/40 mt-1">
              <BookOpenText class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
              <span>{{ p.veiculo }}.</span>
            </div>
          </GlassCard>
        </div>
      </GlassCard>
    </div>
  </div>

  <div v-else-if="tab === 'grupos'">
    <section>
      <h2 class="text-xl font-bold text-brand-dark mb-4">Grupos de Pesquisa</h2>
      <div class="space-y-3">
        <GlassCard v-for="g in grupos" :key="g.nome">
          <div class="flex flex-wrap gap-1.5 mb-1">
            <span class="badge badge-green">{{ g.instituicao }}</span>
          </div>
          <h3 class="font-semibold text-brand-dark">{{ g.nome }}</h3>
          <div class="flex items-start gap-2 text-sm text-brand-dark/60 mt-1">
            <Info class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
            <span>{{ g.descricao }}</span>
          </div>
          <div class="flex items-start gap-2 text-xs text-brand-dark/40 mt-1">
            <CalendarDays class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
            <span>{{ g.periodo }}</span>
          </div>
        </GlassCard>
      </div>
    </section>
  </div>

  <div v-else>
    <section>
      <h2 class="text-xl font-bold text-brand-dark mb-4">Orientações de Mestrado</h2>
      <div class="space-y-3">
        <GlassCard v-for="o in [...concluidas, ...aIniciar]" :key="o.aluno">
          <div class="flex flex-wrap gap-1.5 mb-1">
            <span class="badge badge-green">{{ o.ano }}</span>
            <span class="badge badge-yellow">Mestrado</span>
            <span v-if="o.situacao === 'A iniciar'" class="badge badge-yellow">Em andamento</span>
          </div>
          <h3 class="font-semibold text-brand-dark">{{ o.aluno }}</h3>
          <div class="flex items-start gap-2 text-sm text-brand-dark/60 mt-1">
            <Info class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
            <span>{{ o.titulo }}</span>
          </div>
          <div class="flex items-start gap-2 text-xs text-brand-dark/40 mt-1">
            <Building2 class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
            <span>{{ o.programa }}</span>
          </div>
        </GlassCard>
      </div>
    </section>
  </div>
</template>