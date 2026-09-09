<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import TechBadge from '../components/TechBadge.vue'
import BrandIcon from '../components/BrandIcon.vue'
import {
  ArrowRight,
  Download,
  Briefcase,
  Users,
  GraduationCap,
  Sparkles,
  FlaskConical,
  PenLine,
} from '@lucide/vue'
import portfolioItems from '../data/portfolio.json'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import ori from '../data/orientacoes.json'
import techIcons from '../data/tech-icons.json'

type TechIcon = { label: string; path: string; hex: string }
const icons = techIcons as Record<string, TechIcon>

function iconFor(name: string | null) {
  if (!name || !icons[name]) return undefined
  return { path: icons[name].path, hex: icons[name].hex }
}

const stackPrincipal = [
  {
    group: 'IA e automação',
    items: [
      { label: 'Python', icon: 'python' },
      { label: 'LangChain', icon: 'langchain' },
      { label: 'n8n', icon: 'n8n' },
      { label: 'PyTorch', icon: 'pytorch' },
    ],
  },
  {
    group: 'Web e produto',
    items: [
      { label: 'TypeScript', icon: 'typescript' },
      { label: 'Vue', icon: 'vuedotjs' },
      { label: 'React', icon: 'react' },
      { label: 'Tailwind', icon: 'tailwindcss' },
    ],
  },
  {
    group: 'Infra e dados',
    items: [
      { label: 'Docker', icon: 'docker' },
      { label: 'Linux', icon: 'linux' },
      { label: 'Node.js', icon: 'nodedotjs' },
    ],
  },
]

const destaques = computed(() =>
  (portfolioItems as any[]).filter((p) => p.destaque && !p.experimental).slice(0, 4),
)

const provas = [
  { valor: '+25 anos', rotulo: 'em tecnologia' },
  { valor: 'CTO desde 1998', rotulo: 'sócio-fundador ProFuzzy' },
  { valor: 'Doutor UFSC', rotulo: 'com passagem INSA-Rouen' },
  { valor: `${pubs.length} publicações`, rotulo: 'últimos 5 anos' },
  { valor: `${ori.length} orientações`, rotulo: 'mestrado' },
]

const capacidades = [
  {
    titulo: 'IA aplicada e agentes inteligentes',
    texto: 'LLMs, RAG, multiagentes e sistemas neuro-fuzzy para resolver problemas reais com autonomia e contexto.',
  },
  {
    titulo: 'Automação de processos e plataformas',
    texto: 'Plataformas web, pipelines, dashboards, crawlers e workflows com n8n — do protótipo à operação.',
  },
  {
    titulo: 'Otimização e apoio à decisão',
    texto: 'Roteirização, dimensionamento de frotas, alocação de recursos e modelos para decisões complexas.',
  },
  {
    titulo: 'Produtos educacionais e aprendizagem',
    texto: 'Microlearning, gamificação, storytelling, laboratórios virtuais e trilhas adaptativas com base sólida.',
  },
]

const marcos = [
  { ano: '1998–Atual', titulo: 'ProFuzzy — CTO / Sócio-fundador', texto: 'Consultoria em IA aplicada e otimização combinatória.' },
  { ano: '2008–2017', titulo: 'Mestrado e Doutorado', texto: 'Univali em Computação Aplicada; UFSC em Engenharia de Produção com doutorado-sanduíche no INSA-Rouen.' },
  { ano: '2015–2024', titulo: 'Docência e coordenação', texto: 'Coordenação de cursos, inovação e PPG em Fatenp, Unigranrio/Afya e parceiras EAD.' },
  { ano: '2013–Atual', titulo: 'Pesquisa aplicada', texto: 'Transporte e logística, IA na educação, acessibilidade e extração de informações da web.' },
  { ano: '2025–Atual', titulo: 'GPIAE / DEGC / UFSC', texto: 'Pesquisa multidisciplinar em IA na Educação.' },
  { ano: '2026–Atual', titulo: 'Pós-doutorado UFSC', texto: 'Engenharia e Gestão do Conhecimento.' },
]
</script>

<template>
  <!-- 1. HERO -->
  <section class="mb-10">
    <GlassCard>
      <div class="grid gap-8 md:grid-cols-[1.6fr_1fr] md:items-start">
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-brand-green mb-3">
            CTO, pesquisador e professor | IA aplicada, automação e otimização
          </p>
          <h1 class="text-3xl md:text-4xl font-bold leading-tight text-brand-dark mb-4">
            Ajudo empresas e instituições a transformar conhecimento e processos complexos em
            soluções de IA, automação e produtos digitais com impacto real.
          </h1>
          <p class="text-base text-brand-dark/80 leading-relaxed mb-6">
            Com experiência executiva, técnica e acadêmica, atuo no desenho e desenvolvimento de
            sistemas inteligentes, automações, plataformas e produtos de ensino para contextos
            que exigem profundidade técnica e visão estratégica.
          </p>
          <div class="flex flex-wrap gap-3 mb-5">
            <router-link
              to="/projetos"
              class="inline-flex items-center gap-2 bg-brand-green text-white px-5 py-2.5 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-green"
            >
              Ver projetos em destaque
              <ArrowRight class="w-4 h-4" />
            </router-link>
            <a
              :href="contato.whatsappLink"
              target="_blank"
              rel="noopener"
              aria-label="Falar comigo no WhatsApp"
              class="glass inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-green"
            >
              <BrandIcon :path="brandIcons.whatsapp.path" :hex="brandIcons.whatsapp.hex" label="WhatsApp" />
              Falar comigo no WhatsApp
            </a>
          </div>
          <div class="flex flex-wrap gap-2 text-sm">
            <a :href="contato.linkedinUrl" target="_blank" rel="noopener" aria-label="Perfil no LinkedIn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full glass text-brand-dark/70 hover:text-brand-dark font-medium">
              <BrandIcon :path="brandIcons.linkedin.path" :hex="brandIcons.linkedin.hex" label="LinkedIn" /> LinkedIn
            </a>
            <a :href="contato.githubUrl" target="_blank" rel="noopener" aria-label="Perfil no GitHub" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full glass text-brand-dark/70 hover:text-brand-dark font-medium">
              <BrandIcon :path="brandIcons.github.path" label="GitHub" class="brand-github" /> GitHub
            </a>
            <a :href="contato.lattesUrl" target="_blank" rel="noopener" aria-label="Currículo Lattes" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full glass text-brand-dark/70 hover:text-brand-dark font-medium">
              <BrandIcon :path="brandIcons.lattes.path" :hex="brandIcons.lattes.hex" :viewBox="brandIcons.lattes.viewBox" label="Lattes" /> Lattes
            </a>
            <a :href="`mailto:${contato.email}`" aria-label="Enviar e-mail" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full glass text-brand-dark/70 hover:text-brand-dark font-medium">
              <BrandIcon :path="brandIcons.gmail.path" :hex="brandIcons.gmail.hex" label="Gmail" /> E-mail
            </a>
            <a :href="contato.cvUrl" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full glass text-brand-dark/70 hover:text-brand-dark font-medium">
              <Download class="w-4 h-4 text-brand-green" /> Baixar CV
            </a>
          </div>
        </div>
        <div class="shrink-0">
          <div class="rounded-2xl border-2 border-dashed border-brand-green/30 bg-brand-green/[0.04] dark:bg-white/[0.03] aspect-[3/4] flex flex-col items-center justify-center text-center p-6">
            <!-- Substitua por: <img src="/foto-daniel.jpg" alt="Foto profissional de Daniel de Oliveira" class="w-full h-full object-cover rounded-2xl" /> -->
            <div class="w-20 h-20 rounded-full bg-brand-green/15 flex items-center justify-center text-3xl font-bold text-brand-green mb-3">
              D
            </div>
            <p class="font-semibold text-brand-dark text-sm">Espaço reservado para foto profissional</p>
            <p class="text-xs text-brand-dark/50 mt-1">Substituir por <code>/public/foto-daniel.jpg</code> quando disponível.</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-4">
            <span class="badge badge-green">+25 anos em tecnologia</span>
            <span class="badge badge-green">CTO e fundador desde 1998</span>
            <span class="badge badge-yellow">Doutor pela UFSC</span>
            <span class="badge badge-yellow">IA · ensino · saúde · transporte</span>
          </div>
        </div>
      </div>
    </GlassCard>
  </section>

  <!-- 2. FAIXA DE PROVAS -->
  <section class="mb-10" aria-label="Provas rápidas">
    <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
      <GlassCard v-for="p in provas" :key="p.valor" class="!p-4 text-center">
        <p class="font-bold text-brand-dark text-sm md:text-base">{{ p.valor }}</p>
        <p class="text-xs text-brand-dark/60 mt-1">{{ p.rotulo }}</p>
      </GlassCard>
    </div>
  </section>

  <!-- 3. TRILHAS -->
  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Escolha o caminho mais próximo do seu objetivo</h2>
    <p class="text-brand-dark/60 mb-4">Atendo tanto empresas e clientes quanto recrutadores e parceiros — sem misturar as conversas.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard class="flex flex-col">
        <div class="flex items-center gap-2 mb-2">
          <Briefcase class="w-5 h-5 text-brand-green" />
          <h3 class="font-bold text-brand-dark">Para empresas e clientes</h3>
        </div>
        <p class="text-sm text-brand-dark/60 mb-4">Soluções em IA aplicada, automação, otimização e produtos digitais para transformar processos, produtos e operações.</p>
        <div class="flex flex-wrap gap-2 mt-auto">
          <router-link to="/servicos" class="inline-flex items-center gap-2 bg-brand-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform">
            Ver serviços e casos <ArrowRight class="w-4 h-4" />
          </router-link>
          <router-link to="/projetos" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform">
            Ver portfólio
          </router-link>
        </div>
      </GlassCard>
      <GlassCard class="flex flex-col">
        <div class="flex items-center gap-2 mb-2">
          <Users class="w-5 h-5 text-brand-green" />
          <h3 class="font-bold text-brand-dark">Para recrutadores e parcerias</h3>
        </div>
        <p class="text-sm text-brand-dark/60 mb-4">Trajetória executiva, técnica e acadêmica em liderança, pesquisa aplicada, ensino e inovação — disponível para PJ ou CLT.</p>
        <div class="flex flex-wrap gap-2 mt-auto">
          <router-link to="/academico" class="inline-flex items-center gap-2 bg-brand-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform">
            Ver trajetória e currículo <ArrowRight class="w-4 h-4" />
          </router-link>
          <a :href="contato.cvUrl" class="glass inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform">
            <Download class="w-4 h-4" /> Baixar CV
          </a>
        </div>
      </GlassCard>
    </div>
  </section>

  <!-- 4. PROJETOS EM DESTAQUE -->
  <section class="mb-12">
    <div class="flex items-end justify-between gap-4 mb-4">
      <div>
        <h2 class="text-2xl font-bold text-brand-dark">Projetos selecionados</h2>
        <p class="text-brand-dark/60 mt-1">Casos que combinam tecnologia, estratégia e execução para resolver problemas reais.</p>
      </div>
      <router-link to="/projetos" class="hidden md:inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline shrink-0">
        Ver portfólio completo <ArrowRight class="w-4 h-4" />
      </router-link>
    </div>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in destaques" :key="r.name" class="flex flex-col">
        <div class="rounded-xl overflow-hidden bg-brand-green/[0.06] border border-brand-green/15 aspect-video flex items-center justify-center mb-4">
          <img
            v-if="(r as any).imagem"
            :src="(r as any).imagem"
            :alt="`Print do projeto ${(r as any).name}`"
            class="w-full h-full object-cover"
            loading="lazy"
          />
          <span v-else class="text-xs font-medium text-brand-dark/40 px-4 text-center">Espaço para print — adicione <code>imagem</code> em portfolio.json</span>
        </div>
        <p class="text-xs font-semibold uppercase tracking-wider text-brand-green">{{ (r as any).bloco }}</p>
        <h3 class="font-semibold text-brand-dark mt-1">{{ (r as any).name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ (r as any).description }}</p>
        <div v-if="(r as any).contexto || (r as any).papel || (r as any).resultado" class="text-sm mt-3 space-y-1">
          <p v-if="(r as any).contexto" class="text-brand-dark/70"><strong>Contexto:</strong> {{ (r as any).contexto }}</p>
          <p v-if="(r as any).papel" class="text-brand-dark/70"><strong>Papel:</strong> {{ (r as any).papel }}</p>
          <p v-if="(r as any).resultado" class="text-brand-dark/70"><strong>Resultado:</strong> {{ (r as any).resultado }}</p>
        </div>
        <div v-if="((r as any).stack?.length || (r as any).badges?.length)" class="flex flex-wrap gap-1.5 mt-3">
          <span v-for="s in ((r as any).stack ?? (r as any).badges ?? [])" :key="s" class="badge badge-green">{{ s }}</span>
        </div>
        <div class="flex flex-wrap items-center gap-2 mt-auto pt-4">
          <router-link to="/projetos" class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline">
            Ver detalhes <ArrowRight class="w-4 h-4" />
          </router-link>
          <span v-if="(r as any).periodo" class="text-xs text-brand-dark/40 ml-auto">{{ (r as any).periodo }}</span>
        </div>
      </GlassCard>
    </div>
    <router-link to="/projetos" class="md:hidden inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline mt-4">
      Ver portfólio completo <ArrowRight class="w-4 h-4" />
    </router-link>
  </section>

  <!-- 5. CAPACIDADES -->
  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Como posso contribuir</h2>
    <p class="text-brand-dark/60 mb-4">Da concepção à entrega, atuo na modelagem, arquitetura e desenvolvimento de soluções para contextos complexos.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="c in capacidades" :key="c.titulo">
        <h3 class="font-bold text-brand-dark mb-1.5">{{ c.titulo }}</h3>
        <p class="text-sm text-brand-dark/60">{{ c.texto }}</p>
      </GlassCard>
    </div>
    <router-link to="/servicos" class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline mt-4">
      Ver todos os serviços <ArrowRight class="w-4 h-4" />
    </router-link>
  </section>

  <!-- 6. STACK PRINCIPAL -->
  <section class="mb-12">
    <GlassCard>
      <div class="flex items-center gap-2 mb-1">
        <Sparkles class="w-5 h-5 text-brand-green" />
        <h2 class="text-xl font-bold text-brand-dark">Stack principal</h2>
      </div>
      <p class="text-sm text-brand-dark/60 mb-4">Recorte enxuto das tecnologias que mais uso — o restante aparece no contexto de cada projeto.</p>
      <div class="space-y-4">
        <div v-for="g in stackPrincipal" :key="g.group">
          <p class="text-xs font-bold uppercase tracking-wider text-brand-green mb-2">{{ g.group }}</p>
          <div class="flex flex-wrap gap-2">
            <TechBadge
              v-for="t in g.items"
              :key="t.label"
              :label="t.label"
              :path="iconFor(t.icon)?.path"
              :hex="iconFor(t.icon)?.hex"
            />
          </div>
        </div>
      </div>
    </GlassCard>
  </section>

  <!-- 7. AUTORIDADE ACADÊMICA -->
  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Base acadêmica que sustenta a prática</h2>
    <p class="text-brand-dark/60 mb-4">Experiência de mercado combinada com pesquisa aplicada, publicações, docência e orientação.</p>
    <div class="grid md:grid-cols-3 gap-4">
      <GlassCard>
        <FlaskConical class="w-5 h-5 text-brand-green mb-2" />
        <h3 class="font-bold text-brand-dark mb-1.5">Pesquisa aplicada</h3>
        <p class="text-sm text-brand-dark/60">IA na educação, transporte e logística, acessibilidade e extração de informações da web.</p>
      </GlassCard>
      <GlassCard>
        <GraduationCap class="w-5 h-5 text-brand-green mb-2" />
        <h3 class="font-bold text-brand-dark mb-1.5">Publicações e orientação</h3>
        <p class="text-sm text-brand-dark/60">{{ pubs.length }} publicações nos últimos 5 anos e {{ ori.length }} orientações de mestrado.</p>
      </GlassCard>
      <GlassCard>
        <Users class="w-5 h-5 text-brand-green mb-2" />
        <h3 class="font-bold text-brand-dark mb-1.5">Instituições e grupos</h3>
        <p class="text-sm text-brand-dark/60">UFSC, Unigranrio/Afya, ProFuzzy, GPIAE e grupos de pesquisa em IA e ensino.</p>
      </GlassCard>
    </div>
    <div class="flex flex-wrap gap-2 mt-4">
      <router-link to="/academico" class="inline-flex items-center gap-2 bg-brand-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform">
        Ver produção acadêmica <ArrowRight class="w-4 h-4" />
      </router-link>
      <router-link to="/academico" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform">
        Grupos e orientações
      </router-link>
    </div>
  </section>

  <!-- 8. TRAJETÓRIA RESUMIDA -->
  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-2">Trajetória selecionada</h2>
    <p class="text-brand-dark/60 mb-4">Uma carreira construída na interseção entre tecnologia, inovação, ensino e pesquisa.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="m in marcos" :key="m.titulo" class="!p-5">
        <p class="text-xs font-bold uppercase tracking-wider text-brand-green">{{ m.ano }}</p>
        <h3 class="font-semibold text-brand-dark mt-1">{{ m.titulo }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ m.texto }}</p>
      </GlassCard>
    </div>
    <router-link to="/academico" class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-green hover:underline mt-4">
      Ver trajetória completa <ArrowRight class="w-4 h-4" />
    </router-link>
  </section>

  <!-- 9. BLOG / INSIGHTS -->
  <section class="mb-12">
    <GlassCard>
      <div class="flex items-center gap-2 mb-2">
        <PenLine class="w-5 h-5 text-brand-green" />
        <h2 class="text-xl font-bold text-brand-dark">Artigos e insights</h2>
        <span class="badge badge-yellow ml-1">Em breve</span>
      </div>
      <p class="text-sm text-brand-dark/60 mb-4">
        Publicações sobre IA aplicada, automação, educação e produtos digitais — com versões também no LinkedIn.
        A seção de blog será ativada com os primeiros 2–3 textos.
      </p>
      <div class="flex flex-wrap gap-2">
        <router-link to="/blog" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-[1.03] transition-transform">
          Visitar blog
        </router-link>
        <a :href="contato.linkedinUrl" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-brand-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:scale-[1.03] transition-transform">
          <BrandIcon :path="brandIcons.linkedin.path" hex="FFFFFF" label="LinkedIn" /> Acompanhar no LinkedIn <ArrowRight class="w-4 h-4" />
        </a>
      </div>
    </GlassCard>
  </section>

  <!-- 10. CTA FINAL -->
  <section>
    <GlassCard class="!p-8 text-center">
      <h2 class="text-2xl font-bold text-brand-dark mb-2">Vamos conversar</h2>
      <p class="text-brand-dark/70 max-w-2xl mx-auto mb-6">
        Se você procura apoio em IA aplicada, automação, produto ou pesquisa com foco em entrega
        concreta, estou disponível para conversar — como consultor, parceiro ou contratado.
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
