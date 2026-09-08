<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
import TechBadge from '../components/TechBadge.vue'
import { BadgeCheck, Info, CalendarDays, BookOpenText } from '@lucide/vue'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import pubsHist from '../data/publicacoes-historicas.json'
import techIcons from '../data/tech-icons.json'

const techGroups = [
  {
    group: 'Linguagens',
    items: [
      { label: 'C#', icon: null },
      { label: 'CSS', icon: 'css' },
      { label: 'HTML', icon: 'html5' },
      { label: 'Java', icon: 'openjdk' },
      { label: 'JavaScript', icon: 'javascript' },
      { label: 'PHP', icon: 'php' },
      { label: 'Python', icon: 'python' },
      { label: 'TypeScript', icon: 'typescript' },
    ],
  },
  {
    group: 'Frameworks',
    items: [
      { label: 'FastAPI', icon: 'fastapi' },
      { label: 'Flask', icon: 'flask' },
      { label: 'React', icon: 'react' },
      { label: 'Tailwind', icon: 'tailwindcss' },
      { label: 'Vue', icon: 'vuedotjs' },
    ],
  },
  {
    group: 'IA & Automação',
    items: [
      { label: 'Agno', icon: null },
      { label: 'Anaconda', icon: 'anaconda' },
      { label: 'LangChain', icon: 'langchain' },
      { label: 'n8n', icon: 'n8n' },
      { label: 'PyTorch', icon: 'pytorch' },
    ],
  },
  {
    group: 'Infra & Outros',
    items: [
      { label: 'Arduino', icon: 'arduino' },
      { label: 'Docker', icon: 'docker' },
      { label: 'Linux', icon: 'linux' },
      { label: 'Moodle', icon: 'moodle' },
      { label: 'Node.js', icon: 'nodedotjs' },
      { label: 'Unity', icon: 'unity' },
    ],
  },
]

const tech = techGroups
  .flatMap((g) => g.items)
  .sort((a, b) => a.label.localeCompare(b.label))

type TechIcon = { label: string; path: string; hex: string }
const icons = techIcons as Record<string, TechIcon>

function iconFor(name: string | null) {
  if (!name || !icons[name]) return undefined
  return { path: (icons[name] as TechIcon).path, hex: (icons[name] as TechIcon).hex }
}

const tipoLabel: Record<string, string> = {
  empresa: 'Empresa',
  ies: 'Instituição de Ensino Superior',
  pesquisa: 'Grupo de Pesquisa / Pesquisa',
  extensao: 'Extensão',
  formacao: 'Formação',
  software: 'Software',
}

type TimelineItem = {
  ano: number
  nome: string
  papel: string
  tipo: string
  periodo: string
  descricao?: string
}

const timeline: TimelineItem[] = [
  { ano: 1998, nome: 'ProFuzzy Consultoria e Sistemas Ltda', papel: 'CTO / Sócio Fundador', tipo: 'empresa', periodo: '1998–Atual', descricao: 'Consultoria em otimização combinatória e IA aplicada · Lages/SC.' },
  { ano: 2002, nome: 'Digipro Informática Ltda', papel: 'Sócio-gerente', tipo: 'empresa', periodo: '2002–2014', descricao: 'Lages/SC.' },
  { ano: 2000, nome: 'Universidade do Planalto Catarinense', papel: 'Graduação', tipo: 'formacao', periodo: '2000–2006', descricao: 'Bacharelado em Informática.' },
  { ano: 2008, nome: 'Univali — Universidade do Vale do Itajaí', papel: 'Mestrado', tipo: 'formacao', periodo: '2008–2010', descricao: 'Mestrado em Computação Aplicada.' },
  { ano: 2011, nome: 'Logística Integrada — otimização e simulação', papel: 'Integrante', tipo: 'pesquisa', periodo: '2011–2013', descricao: 'Localização de centrais de inteligência e redes dinâmicas de transporte.' },
  { ano: 2012, nome: 'UFSC — Universidade Federal de Santa Catarina', papel: 'Doutorado', tipo: 'formacao', periodo: '2012–2017', descricao: 'Engenharia de Produção e Sistemas.' },
  { ano: 2014, nome: 'INSA-Rouen — Institut National des Sciences Appliquées de Rouen', papel: 'Doutorado Sanduíche', tipo: 'formacao', periodo: '2014–2015', descricao: 'Otimização em Transporte e Logística · França.' },
  { ano: 2013, nome: 'LOGÍSTICA HUMANITÁRIA', papel: 'Integrante', tipo: 'pesquisa', periodo: '2013–2018', descricao: 'Transporte dinâmico em situações de emergência, evitando rupturas na rede e ponderando custo x risco de ruptura.' },
  { ano: 2015, nome: 'Fatenp — Faculdade de Tecnologia Nova Palhoça', papel: 'Professor Adjunto Mestre / Coordenador de Curso', tipo: 'ies', periodo: '2015–2018', descricao: 'Coordenador do Curso de Jogos Digitais.' },
  { ano: 2018, nome: 'Universidade Unigranrio', papel: 'Professor Adjunto Doutor / Coordenador de Curso', tipo: 'ies', periodo: '2018–2024', descricao: 'Coordenação Geral de Curso, Escritório de Inovação, PPG Ensino das Ciências.' },
  { ano: 2019, nome: "Girls'n Code", papel: 'Responsável', tipo: 'extensao', periodo: '2019–2022', descricao: 'Ensino de Computação para meninas e jovens.' },
  { ano: 2020, nome: 'Recursos de Acessibilidade com Arduino', papel: 'Integrante', tipo: 'pesquisa', periodo: '2020–2021', descricao: 'Soluções de baixo custo para cegos/baixa visão; FUNADESP.' },
  { ano: 2021, nome: 'Tecnologias Digitais e Recursos Didáticos no Ensino de Ciências e Matemática', papel: 'Pesquisador', tipo: 'pesquisa', periodo: '2021–Atual', descricao: 'Macroprojeto PPG Ensino de Ciências Unigranrio.' },
  { ano: 2021, nome: 'Extração de Informações Implícitas da Web', papel: 'Integrante', tipo: 'pesquisa', periodo: '2021–2022', descricao: 'QA sobre dados estruturados/não-estruturados; FUNADESP.' },
  { ano: 2021, nome: 'Faculdade Descomplica', papel: 'Professor Autor', tipo: 'ies', periodo: '2021–2022' },
  { ano: 2022, nome: 'Instituto Infnet', papel: 'Professor', tipo: 'ies', periodo: '2022–2023' },
  { ano: 2022, nome: 'GRAN Cursos', papel: 'Professor autor', tipo: 'ies', periodo: '2022–2023' },
  { ano: 2022, nome: 'Unigama', papel: 'Coordenador de Tecnologia e Inovação / Professor EAD / Coordenador de Curso', tipo: 'ies', periodo: '2022–2024' },
  { ano: 2025, nome: 'GPIAE — IA na Educação', papel: 'Pesquisador', tipo: 'pesquisa', periodo: '2025–Atual', descricao: 'Grupo multidisciplinar DEGC/UFSC.' },
  { ano: 2026, nome: 'UFSC — Universidade Federal de Santa Catarina', papel: 'Pós-doutorado', tipo: 'formacao', periodo: '2026–Atual', descricao: 'Engenharia e Gestão do Conhecimento.' },
]

const pubCountByYear = pubs.reduce<Record<number, number>>((acc, p: any) => {
  const ano = Number(p.ano)
  acc[ano] = (acc[ano] || 0) + 1
  return acc
}, {})

for (const [ano, count] of Object.entries(pubsHist)) {
  pubCountByYear[Number(ano)] = (pubCountByYear[Number(ano)] || 0) + count
}

const years = [...new Set([...timeline.map((t) => t.ano), ...Object.keys(pubCountByYear).map(Number)])].sort((a, b) => a - b)
</script>

<template>
  <section class="mb-12">
    <GlassCard>
      <div class="flex flex-col md:flex-row gap-8 items-center">
        <div class="w-32 h-32 rounded-full bg-brand-green/20 flex items-center justify-center text-4xl font-bold text-brand-green shrink-0">
          D
        </div>
        <div>
          <h1 class="text-4xl font-bold text-brand-green mb-2">Daniel de Oliveira</h1>
          <p class="text-brand-dark/80 leading-relaxed">
            CTO e sócio-fundador da <strong>ProFuzzy</strong> (1998–atual), Professor colaborador no PPG Ensino de Ciências e Saúde da Unigranrio/Afya e pesquisador no <strong>GPIAE/DEGC/UFSC</strong>. Doutor em Engenharia de Produção (UFSC/INSA-Rouen) e mestre em Computação (Univali). Atua na interseção entre Inteligência Artificial, Otimização Combinatória e Educação. Experiência em sistemas neuro-fuzzy, arquitetura multiagentes, LLMs e pipelines RAG, aplicados a plataformas de saúde e transporte, concessões públicas e projetos de transporte. No campo do ensino, destaca-se a vivência em computação, EAD, desenvolvimento de games, gamificação e governança de inovação.
          </p>
          <div class="flex gap-3 mt-4">
            <router-link to="/servicos" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-105 transition-transform">
              Ver Serviços
            </router-link>
            <router-link to="/academico" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-105 transition-transform">
              Produção Acadêmica
            </router-link>
          </div>
        </div>
      </div>
    </GlassCard>
  </section>

  <section class="mb-12">
    <GlassCard>
      <h2 class="text-xl font-bold text-brand-dark mb-4">Tecnologias & Ferramentas</h2>
      <div class="flex flex-wrap gap-2">
        <TechBadge
          v-for="t in tech"
          :key="t.label"
          :label="t.label"
          :path="iconFor(t.icon)?.path"
          :hex="iconFor(t.icon)?.hex"
        />
      </div>
    </GlassCard>
  </section>

  <section class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-12">
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Soluções em IA & Otimização</h3>
      <p class="text-sm text-brand-dark/60">LLMs, agentes, RAG, sistemas neuro-fuzzy, algoritmos genéticos, GRASP, redes de fluxo.</p>
    </GlassCard>
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Plataformas & Automação</h3>
      <p class="text-sm text-brand-dark/60">Desenvolvimento de plataformas web, pipelines n8n, dashboards, crawlers, storyboards com IA.</p>
    </GlassCard>
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Frentes de Atuação</h3>
      <p class="text-sm text-brand-dark/60">Saúde & Bem-estar, Transporte & Logística, Concessões Públicas, Educação.</p>
    </GlassCard>
  </section>

  <section>
    <h2 class="text-2xl font-bold text-brand-dark mb-4">Trajetória</h2>
    <div class="relative">
      <div v-for="y in years" :key="y" class="grid grid-cols-[64px_24px_1fr] gap-4">
        <div class="text-right pt-1">
          <span class="text-sm font-bold text-brand-green">{{ y }}</span>
        </div>
        <div class="relative flex justify-center">
          <div class="absolute top-0 bottom-0 w-0.5 bg-brand-green/30"></div>
          <div class="relative z-10 mt-1.5 w-4 h-4 rounded-full ring-4 ring-brand-cream bg-brand-green"></div>
        </div>
        <div class="pb-8">
          <div v-for="(item, i) in timeline.filter((t) => t.ano === y)" :key="i" class="pb-4">
            <GlassCard>
              <p class="text-xs font-semibold uppercase tracking-wider text-brand-green">{{ tipoLabel[item.tipo] }}</p>
              <h3 class="font-semibold text-brand-dark">{{ item.nome }}</h3>
              <div class="flex items-center gap-2 text-sm text-brand-dark/60 mt-1">
                <BadgeCheck class="w-4 h-4 text-brand-green shrink-0" />
                <span>{{ item.papel }}</span>
              </div>
              <div v-if="item.descricao" class="flex items-start gap-2 text-sm text-brand-dark/40 mt-1">
                <Info class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
                <span>{{ item.descricao }}</span>
              </div>
              <div class="flex items-center gap-2 text-xs text-brand-dark/40 mt-1">
                <CalendarDays class="w-4 h-4 text-brand-yellow shrink-0" />
                <span>{{ item.periodo }}</span>
              </div>
            </GlassCard>
          </div>
          <div v-if="pubCountByYear[y]" class="mt-2">
            <div class="flex items-center gap-2 text-sm font-semibold text-brand-yellow">
              <BookOpenText class="w-4 h-4 shrink-0" />
              <span>{{ pubCountByYear[y] }} publicação{{ pubCountByYear[y] > 1 ? 'ões' : 'ão' }} no ano.</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>