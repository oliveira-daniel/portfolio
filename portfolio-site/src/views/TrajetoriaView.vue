<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import BrandIcon from '../components/BrandIcon.vue'
import {
  ArrowLeft,
  BadgeCheck,
  BookOpenText,
  CalendarDays,
  Download,
  Info,
} from '@lucide/vue'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import pubsHist from '../data/publicacoes-historicas.json'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'

const tipoLabel: Record<string, string> = {
  empresa: 'Empresa',
  ies: 'Instituição de Ensino Superior',
  pesquisa: 'Grupo de Pesquisa / Pesquisa',
  extensao: 'Extensão',
  formacao: 'Formação',
}

type TimelineItem = {
  ano: number
  nome: string
  papel: string
  tipo: string
  periodo: string
  descricao?: string
}

const trajectory: TimelineItem[] = [
  { ano: 1998, nome: 'ProFuzzy Consultoria e Sistemas Ltda', papel: 'CTO / Sócio Fundador', tipo: 'empresa', periodo: '1998–Atual', descricao: 'Consultoria em otimização combinatória e IA aplicada · Lages/SC.' },
  { ano: 2000, nome: 'Universidade do Planalto Catarinense', papel: 'Graduação', tipo: 'formacao', periodo: '2000–2006', descricao: 'Bacharelado em Informática.' },
  { ano: 2002, nome: 'Digipro Informática Ltda', papel: 'Sócio-gerente', tipo: 'empresa', periodo: '2002–2014', descricao: 'Lages/SC.' },
  { ano: 2008, nome: 'Univali (Universidade do Vale do Itajaí)', papel: 'Mestrado', tipo: 'formacao', periodo: '2008–2010', descricao: 'Mestrado em Computação Aplicada.' },
  { ano: 2011, nome: 'Logística Integrada, otimização e simulação', papel: 'Integrante', tipo: 'pesquisa', periodo: '2011–2013', descricao: 'Localização de centrais de inteligência e redes dinâmicas de transporte.' },
  { ano: 2012, nome: 'UFSC (Universidade Federal de Santa Catarina)', papel: 'Doutorado', tipo: 'formacao', periodo: '2012–2017', descricao: 'Engenharia de Produção e Sistemas.' },
  { ano: 2013, nome: 'Logística Humanitária', papel: 'Integrante', tipo: 'pesquisa', periodo: '2013–2018', descricao: 'Transporte dinâmico em situações de emergência, evitando rupturas na rede e ponderando custo x risco de ruptura.' },
  { ano: 2014, nome: 'INSA-Rouen (Institut National des Sciences Appliquées de Rouen)', papel: 'Doutorado Sanduíche', tipo: 'formacao', periodo: '2014–2015', descricao: 'Otimização em Transporte e Logística · França.' },
  { ano: 2015, nome: 'Fatenp (Faculdade de Tecnologia Nova Palhoça)', papel: 'Professor Adjunto Mestre / Coordenador de Curso', tipo: 'ies', periodo: '2015–2018', descricao: 'Coordenador do Curso de Jogos Digitais.' },
  { ano: 2018, nome: 'Universidade Unigranrio', papel: 'Professor Adjunto Doutor / Coordenador de Curso', tipo: 'ies', periodo: '2018–2024', descricao: 'Coordenação Geral de Curso, Escritório de Inovação, PPG Ensino das Ciências.' },
  { ano: 2019, nome: "Girls'n Code", papel: 'Responsável', tipo: 'extensao', periodo: '2019–2022', descricao: 'Ensino de Computação para meninas e jovens; FUNADESP.' },
  { ano: 2020, nome: 'Recursos de Acessibilidade com Arduino', papel: 'Integrante', tipo: 'pesquisa', periodo: '2020–2021', descricao: 'Soluções de baixo custo para cegos/baixa visão; FUNADESP.' },
  { ano: 2021, nome: 'Tecnologias Digitais e Recursos Didáticos no Ensino de Ciências e Matemática', papel: 'Pesquisador', tipo: 'pesquisa', periodo: '2021–Atual', descricao: 'Macroprojeto PPG Ensino de Ciências Unigranrio.' },
  { ano: 2021, nome: 'Extração de Informações Implícitas da Web', papel: 'Integrante', tipo: 'pesquisa', periodo: '2021–2022', descricao: 'QA sobre dados estruturados/não-estruturados; FUNADESP.' },
  { ano: 2021, nome: 'Faculdade Descomplica', papel: 'Professor Autor', tipo: 'ies', periodo: '2021–2022' },
  { ano: 2022, nome: 'Instituto Infnet', papel: 'Professor', tipo: 'ies', periodo: '2022–2023' },
  { ano: 2022, nome: 'GRAN Cursos', papel: 'Professor autor', tipo: 'ies', periodo: '2022–2023' },
  { ano: 2022, nome: 'Unigama', papel: 'Coordenador de Tecnologia e Inovação / Professor EAD / Coordenador de Curso', tipo: 'ies', periodo: '2022–2024' },
  { ano: 2025, nome: 'GPIAE (IA na Educação)', papel: 'Pesquisador', tipo: 'pesquisa', periodo: '2025–Atual', descricao: 'Grupo multidisciplinar DEGC/UFSC.' },
  { ano: 2026, nome: 'UFSC (Universidade Federal de Santa Catarina)', papel: 'Pós-doutorado', tipo: 'formacao', periodo: '2026–Atual', descricao: 'Engenharia e Gestão do Conhecimento.' },
]

const pubCountByYear = pubs.reduce<Record<number, number>>((acc, p: any) => {
  const ano = Number(p.ano)
  acc[ano] = (acc[ano] || 0) + 1
  return acc
}, {})

for (const [ano, count] of Object.entries(pubsHist)) {
  pubCountByYear[Number(ano)] = (pubCountByYear[Number(ano)] || 0) + count
}

const years = computed(() =>
  [...new Set([...trajectory.map((t) => t.ano), ...Object.keys(pubCountByYear).map(Number)])].sort((a, b) => a - b),
)
</script>

<template>
  <router-link to="/" class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline mb-4">
    <ArrowLeft class="w-4 h-4" /> Voltar ao início
  </router-link>

  <h1 class="text-3xl font-bold text-brand-dark mb-2">Trajetória</h1>
  <p class="text-brand-dark/60 mb-8">Carreira, formação, docência e pesquisa de 1998 até hoje.</p>

  <section class="mb-12">
    <div class="relative">
      <div v-for="y in years" :key="y" class="grid grid-cols-[48px_20px_1fr] md:grid-cols-[64px_24px_1fr] gap-4">
        <div class="text-right pt-1">
          <span class="text-sm font-bold text-brand-green">{{ y }}</span>
        </div>
        <div class="relative flex justify-center">
          <div class="absolute top-0 bottom-0 w-0.5 bg-brand-green/30"></div>
          <div class="relative z-10 mt-1.5 w-4 h-4 rounded-full ring-4 ring-brand-cream bg-brand-green"></div>
        </div>
        <div class="pb-8">
          <div v-for="(item, i) in trajectory.filter((t) => t.ano === y)" :key="i" class="pb-4">
            <GlassCard>
              <p class="text-xs font-semibold uppercase tracking-wider text-brand-green">{{ tipoLabel[item.tipo] }}</p>
              <h3 class="font-semibold text-brand-dark">{{ item.nome }}</h3>
              <div class="flex items-center gap-2 text-sm text-brand-dark/60 mt-1">
                <BadgeCheck class="w-4 h-4 text-brand-green shrink-0" />
                <span>{{ item.papel }}</span>
              </div>
              <div v-if="item.descricao" class="flex items-start gap-2 text-sm text-brand-dark/60 mt-1">
                <Info class="w-4 h-4 shrink-0 mt-0.5 text-brand-green" />
                <span>{{ item.descricao }}</span>
              </div>
              <div class="flex items-center gap-2 text-xs text-brand-dark/60 mt-1">
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

  <section>
    <GlassCard padding="p-8" class="text-center">
      <h2 class="text-2xl font-bold text-brand-dark mb-2">Quer saber mais?</h2>
      <p class="text-brand-dark/70 max-w-2xl mx-auto mb-6">
        O currículo completo está no Lattes, ou fale comigo direto pelos canais abaixo.
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
      </div>
    </GlassCard>
  </section>
</template>
