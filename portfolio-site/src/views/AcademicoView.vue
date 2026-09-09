<script setup lang="ts">
import { computed, ref } from 'vue'
import { BookOpenText, Building2, CalendarDays, ChevronDown, Download, Info, Users } from 'lucide-vue-next'
import GlassCard from '../components/GlassCard.vue'
import BrandIcon from '../components/BrandIcon.vue'
import DonutChart from '../components/DonutChart.vue'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'
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
const displayTipos = ['artigo', 'capitulo', 'anais_eventos'] as const
const displayLabel: Record<string, string> = {
  artigo: 'Periódicos',
  capitulo: 'Capítulos',
  anais_eventos: 'Anais',
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
  { nome: 'GPIAE (IA na Educação)', instituicao: 'DEGC/UFSC', periodo: '2025–Atual', descricao: 'Grupo multidisciplinar em Inteligência Artificial na Educação.' },
  { nome: 'Logística Integrada, otimização e simulação', instituicao: 'UFSC', periodo: '2011–2013', descricao: 'Localização de centrais de inteligência e redes dinâmicas de transporte.' },
  { nome: 'Logística Humanitária', instituicao: 'UFSC', periodo: '2013–2018', descricao: 'Transporte dinâmico em situações de emergência, evitando rupturas na rede e ponderando custo x risco de ruptura.' },
  { nome: 'Tecnologias Digitais e Recursos Didáticos no Ensino de Ciências e Matemática', instituicao: 'Unigranrio', periodo: '2021–Atual', descricao: 'Macroprojeto PPG Ensino de Ciências Unigranrio.' },
  { nome: 'Extração de Informações Implícitas da Web', instituicao: 'Unigranrio', periodo: '2021–2022', descricao: 'QA sobre dados estruturados/não-estruturados; FUNADESP.' },
  { nome: 'Recursos de Acessibilidade com Arduino', instituicao: 'Unigranrio', periodo: '2020–2021', descricao: 'Soluções de baixo custo para cegos/baixa visão; FUNADESP.' },
]

type Grupo = (typeof grupos)[number]

const gruposOrdenados = computed(() =>
  [...grupos].sort((a, b) => {
    const start = (p: string) => Number(p.split('–')[0])
    const end = (p: string) => (p.includes('Atual') ? 9999 : Number(p.split('–')[1]))
    if (start(b.periodo) !== start(a.periodo)) return start(b.periodo) - start(a.periodo)
    return end(b.periodo) - end(a.periodo)
  }),
)

const gruposAtivos = computed(() => grupos.filter((g) => g.periodo.includes('Atual')))
const totalPubs = computed(() => pubs.length)
const resumoCount = computed(() => pubs.filter((p: any) => ['resumo', 'resumo_expandido'].includes(p.tipo)).length)
const gruposPorInstituicao = computed(() => {
  const m: Record<string, number> = {}
  for (const g of grupos) m[g.instituicao] = (m[g.instituicao] || 0) + 1
  return m
})

const anaisEventos = computed(() => [...grouped.value['anais'], ...grouped.value['resumo'], ...grouped.value['resumo_expandido']])
const displayGrouped = computed<Record<string, any[]>>(() => ({
  artigo: grouped.value['artigo'],
  capitulo: grouped.value['capitulo'],
  anais_eventos: anaisEventos.value,
}))

const pubDonut = computed(() => {
  const labels = displayTipos.map((t) => displayLabel[t])
  const values = displayTipos.map((t) => (displayGrouped.value as any)[t].length)
  return { labels, values }
})
const pubColors = ['#518E45', '#F1CA30', '#20372F']

const oriDonut = computed(() => ({
  labels: ['Concluídas', 'Em andamento'],
  values: [concluidas.value.length, aIniciar.value.length],
}))
const oriColors = ['#518E45', '#F1CA30']

const gruposDonut = computed(() => ({
  labels: ['Ativos', 'Encerrados'],
  values: [gruposAtivos.value.length, grupos.length - gruposAtivos.value.length],
}))
const gruposColors = ['#518E45', '#cbd5e1']

const qualisDonut = computed(() => {
  const labels = Object.keys(qualisCount.value).sort()
  const values = labels.map((l) => qualisCount.value[l])
  return { labels, values }
})
const qualisPalette: Record<string, string> = { A2: '#20372F', A3: '#518E45', A4: '#F1CA30', B2: '#94a3b8' }
const qualisColors = computed(() => qualisDonut.value.labels.map((l) => qualisPalette[l] ?? '#94a3b8'))


</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Acadêmico</h1>

  <div class="flex gap-2 mb-8 mt-6 flex-wrap">
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
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <DonutChart title="Publicações*" :labels="pubDonut.labels" :values="pubDonut.values" :colors="pubColors" />
      <DonutChart title="Publicações no Extrato Qualis*" :labels="qualisDonut.labels" :values="qualisDonut.values" :colors="qualisColors" />
      <DonutChart title="Orientações de mestrado" :labels="oriDonut.labels" :values="oriDonut.values" :colors="oriColors" />
      <DonutChart title="Grupos de pesquisa" :labels="gruposDonut.labels" :values="gruposDonut.values" :colors="gruposColors" />
    </section>
    <p class="text-xs text-brand-dark/40 mt-3">* Publicações dos últimos 5 anos</p>
  </div>

  <div v-else-if="tab === 'publicacoes'">
    <p class="text-sm text-brand-dark/60 mb-4">Publicações dos últimos 5 anos</p>
    <div class="space-y-3">
      <div
        v-for="t in displayTipos"
        :key="t"
        class="rounded-2xl border border-brand-green/15 overflow-hidden bg-white/40 backdrop-blur-sm dark:bg-white/[0.04] dark:border-white/10"
      >
        <button
          @click="toggleSection(t)"
          class="w-full flex items-center justify-between gap-2 text-left px-6 py-4"
        >
          <span class="flex items-center gap-2">
            <h2 class="text-lg font-bold text-brand-dark">{{ displayLabel[t] }}</h2>
            <span class="badge badge-yellow">{{ (displayGrouped as any)[t].length }}</span>
          </span>
          <ChevronDown
            class="w-5 h-5 text-brand-green shrink-0 transition-transform"
            :class="openSections.includes(t) ? 'rotate-180' : ''"
          />
        </button>
        <div v-if="openSections.includes(t)" class="px-3 pb-3 space-y-3 border-t border-brand-green/10 dark:border-white/10 pt-3 bg-brand-green/[0.02] dark:bg-white/[0.02]">
          <GlassCard v-for="p in (displayGrouped as any)[t]" :key="p.titulo">
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
      </div>
    </div>
  </div>

  <div v-else-if="tab === 'grupos'">
    <section>
      <h2 class="text-xl font-bold text-brand-dark mb-4">Grupos de Pesquisa</h2>
      <div class="space-y-3">
        <GlassCard v-for="g in gruposOrdenados" :key="g.nome">
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

  <section class="mt-12">
    <GlassCard class="!p-8 text-center">
      <h2 class="text-2xl font-bold text-brand-dark mb-2">Vamos colaborar em pesquisa</h2>
      <p class="text-brand-dark/70 max-w-2xl mx-auto mb-6">
        Para orientações, parcerias de pesquisa ou projetos com base científica, estes são os melhores canais.
      </p>
      <div class="flex flex-wrap justify-center gap-3">
        <a
          :href="contato.whatsappLink"
          target="_blank"
          rel="noopener"
          class="inline-flex items-center gap-2 bg-brand-green text-white px-5 py-2.5 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform"
        >
          <BrandIcon :path="brandIcons.whatsapp.path" hex="FFFFFF" label="WhatsApp" /> Chamar no WhatsApp
        </a>
        <a
          :href="contato.cvUrl"
          class="glass inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform"
        >
          <Download class="w-4 h-4" /> Baixar CV
        </a>
        <a
          :href="contato.lattesUrl"
          target="_blank"
          rel="noopener"
          class="glass inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform"
        >
          <BrandIcon :path="brandIcons.lattes.path" :viewBox="brandIcons.lattes.viewBox" label="Lattes" class="brand-lattes" /> Lattes
        </a>
      </div>
    </GlassCard>
  </section>
</template>