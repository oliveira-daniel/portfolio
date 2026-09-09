<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
import BrandIcon from '../components/BrandIcon.vue'
import {
  ArrowRight,
  BarChart3,
  Bot,
  ClipboardList,
  FlaskConical,
  GraduationCap,
  Handshake,
  Network,
  Rocket,
  Route,
} from '@lucide/vue'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'

const servicos = [
  {
    icon: Network,
    titulo: 'Modelagem de conhecimento com ontologias',
    texto: 'Estruturação do conhecimento do domínio para integrar dados e dar base semântica a sistemas de decisão, buscadores e agentes inteligentes.',
    entregas: ['Ontologia do domínio', 'Vocabulário padronizado'],
  },
  {
    icon: BarChart3,
    titulo: 'Análise de dados e machine learning',
    texto: 'Segmentação, detecção de padrões e insights que orientam decisões em saúde, educação, transporte e mercado, de dashboards a modelos neuro-fuzzy.',
    entregas: ['Dashboard', 'Relatórios e insights', 'Modelo treinado'],
  },
  {
    icon: Route,
    titulo: 'Otimização e pesquisa operacional',
    texto: 'Solução de problemas como roteirização, dimensionamento de frotas e alocação de recursos, com algoritmos genéticos, fluxo em redes e programação matemática.',
    entregas: ['Modelo de otimização', 'Rotas e alocação', 'Recomendações'],
  },
  {
    icon: Bot,
    titulo: 'Agentes de IA, RAG e automação',
    texto: 'Sistemas multiagentes e RAG sobre bases próprias, com agentes conversacionais e automação de fluxos, do protótipo à operação, incluindo inteligência de mercado para concessões públicas.',
    entregas: ['Agente inteligente', 'Pipeline RAG', 'Automações e integrações'],
  },
  {
    icon: GraduationCap,
    titulo: 'Produtos de ensino e gamificação',
    texto: 'Ambientes de aprendizagem com storytelling, gamificação e sala de aula invertida, laboratórios virtuais, microlearning e trilhas adaptativas, do conteúdo ao sistema.',
    entregas: ['Conteúdo e trilhas', 'Ambiente gamificado', 'Laboratório virtual'],
  },
  {
    icon: Handshake,
    titulo: 'Consultoria e mentoria técnica',
    texto: 'Apoio especializado para equipes e projetos no desenho de arquiteturas de IA, avaliação de soluções, transferência de tecnologia e mentoria em machine learning, otimização e automação.',
    entregas: ['Diagnóstico técnico', 'Arquitetura proposta', 'Mentoria'],
  },
]

const frentes = ['Ensino', 'Transporte e logística', 'Concessões públicas', 'Saúde e bem-estar']

const passos = [
  {
    icon: ClipboardList,
    titulo: '1. Diagnóstico',
    texto: 'Entendimento do problema, dos dados disponíveis e do resultado esperado, com escopo e critérios claros.',
  },
  {
    icon: FlaskConical,
    titulo: '2. Proposta e protótipo',
    texto: 'Desenho da solução e validação rápida em protótipo, antes de investir na implementação completa.',
  },
  {
    icon: Rocket,
    titulo: '3. Entrega e operação',
    texto: 'Implementação, transferência de tecnologia e acompanhamento para a solução operar de verdade.',
  },
]
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Serviços</h1>
  <p class="text-brand-dark/60 mb-8">Soluções sob medida de IA, otimização e produto, do diagnóstico à operação, para empresas, equipes e instituições.</p>

  <section class="grid md:grid-cols-2 gap-4 mb-12">
    <GlassCard v-for="s in servicos" :key="s.titulo" class="relative flex flex-col">
      <span class="absolute top-4 right-4 w-7 h-7 rounded-full bg-brand-green/15 flex items-center justify-center" aria-hidden="true">
        <component :is="s.icon" class="w-4 h-4 text-brand-green" />
      </span>
      <h2 class="text-lg font-bold text-brand-dark mb-2 pr-10">{{ s.titulo }}</h2>
      <p class="text-sm text-brand-dark/60">{{ s.texto }}</p>
      <div class="flex flex-wrap gap-1.5 mt-auto pt-4">
        <span v-for="e in s.entregas" :key="e" class="badge badge-green">{{ e }}</span>
      </div>
    </GlassCard>
  </section>

  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Frentes de atuação</h2>
    <p class="text-brand-dark/60 mb-4">Setores onde essas soluções já foram aplicadas.</p>
    <div class="grid gap-4 md:grid-cols-[1.6fr_1fr] md:items-center">
      <div class="flex flex-wrap gap-2">
        <span v-for="f in frentes" :key="f" class="badge badge-yellow">{{ f }}</span>
      </div>
      <div class="flex md:justify-end">
        <router-link to="/projetos" class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline">
          Ver casos no portfólio <ArrowRight class="w-4 h-4" />
        </router-link>
      </div>
    </div>
  </section>

  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Como funciona</h2>
    <p class="text-brand-dark/60 mb-4">Um caminho simples do problema à solução em operação.</p>
    <div class="grid md:grid-cols-3 gap-4">
      <GlassCard v-for="p in passos" :key="p.titulo" class="relative">
        <span class="absolute top-4 right-4 w-7 h-7 rounded-full bg-brand-green/15 flex items-center justify-center" aria-hidden="true">
          <component :is="p.icon" class="w-4 h-4 text-brand-green" />
        </span>
        <h3 class="font-bold text-brand-dark mb-1.5 pr-10">{{ p.titulo }}</h3>
        <p class="text-sm text-brand-dark/60">{{ p.texto }}</p>
      </GlassCard>
    </div>
  </section>

  <section>
    <GlassCard padding="p-8" class="text-center">
      <h2 class="text-2xl font-bold text-brand-dark mb-2">Vamos conversar sobre seu projeto</h2>
      <p class="text-brand-dark/70 max-w-2xl mx-auto mb-6">
        Conte o problema que você quer resolver e receba uma avaliação inicial sem compromisso.
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
          :href="`mailto:${contato.email}`"
          class="glass inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform"
        >
          <BrandIcon :path="brandIcons.gmail.path" :hex="brandIcons.gmail.hex" label="Gmail" /> {{ contato.email }}
        </a>
      </div>
    </GlassCard>
  </section>
</template>
