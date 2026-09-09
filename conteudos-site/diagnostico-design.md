# Diagnóstico de Design — Site CV / Portfólio

**Data:** 09/09/2026
**Escopo:** Análise de design, conteúdo, UX e profissionalismo do site em `portfolio-site/`
**Objetivo:** Avaliar o que está bom, o que falta e o que melhorar para deixá-lo profissional

## Resumo executivo

O site já transmite senioridade e consistência visual, mas está mais próximo de um perfil rico / currículo navegável do que de um portfólio profissional com boa conversão para clientes ou recrutadores.

- Forte em credibilidade
- Bom em conteúdo
- Razoável em visual
- Fraco em conversão profissional

Sensação atual: "pessoa muito qualificada"
Sensação ideal: "profissional altamente qualificado, com proposta clara, prova concreta e fácil de contratar"

## 1. Estrutura atual

Rotas principais:

- `Início` — `src/views/HomeView.vue`
- `Serviços` — `src/views/ServicosView.vue`
- `Acadêmico` — `src/views/AcademicoView.vue`
- `Portfólio` — `src/views/ProjetosView.vue`
- `Blog` — `src/views/BlogView.vue`

Componentes base:

- `src/components/NavBar.vue`
- `src/components/Footer.vue`
- `src/components/GlassCard.vue`
- `src/components/TechBadge.vue`
- `src/components/DonutChart.vue` / `QualisChart.vue`

Sistema visual:

- Paleta: verde `#518E45`, amarelo `#F1CA30`, dark `#20372F`, cream `#F9F6EB`
- Fonte: Inter
- Estilo: glassmorphism + badges + cards
- Dark mode com persistência em `localStorage`
- Refs: `src/style.css`, `src/App.vue`, `index.html`

## 2. Pontos fortes

- Identidade visual coerente: paleta sóbria, bom uso de `glass`, badges e cartões.
- Conteúdo forte de autoridade: trajetória longa, atuação em IA, docência, pesquisa, doutorado e pós-doc.
- Estrutura organizada em áreas relevantes.
- Página Acadêmica é o trecho com mais força de prova: gráficos, publicações, orientações, grupos de pesquisa.
- Hierarquia básica clara na Home: hero/bio → tecnologias → capacidades → timeline.

## 3. O que está faltando

### 3.1 Contato visível

Maior lacuna atual. Não há área clara com:

- e-mail: daniel.tech.edu@gmail.com
- LinkedIn: www.linkedin.com/in/daniel-oliveira-dr/
- GitHub: github.com/oliveira-daniel
- Lattes / ORCID: lattes.cnpq.br/0984344989835257
- botão de contato / agendar conversa > enviar para whatsapp +55 21 98330 1312
- botão para baixar CV

Refs:

- `src/components/Footer.vue:1-4`
- `src/components/NavBar.vue:10-16`
- `src/router/index.ts:3-9`

### 3.2 Proposta de valor clara

Hero atual é rico, mas longo e biográfico (`src/views/HomeView.vue:130-133`).
Falta responder em 5 segundos:

- quem você ajuda
- com o quê
- com qual resultado

CTAs atuais são só internos: “Ver Serviços” e “Produção Acadêmica” (`src/views/HomeView.vue:134-140`).
Faltam CTAs como:

- Falar comigo / Agendar conversa
- Baixar CV
- Ver trabalhos selecionados
- LinkedIn / GitHub / Lattes

### 3.3 Provas de resultado

Portfólio mostra áreas e projetos, mas os cards são majoritariamente texto: nome + descrição.
Faltam:

- resultados mensuráveis
- contexto / cliente / instituição
- papel específico
- stack relevante por projeto
- links para demo, artigo, repo ou estudo de caso
- screenshots / visual > Isso eu consigo
- estrutura problema → abordagem → resultado

Ref: `src/views/ProjetosView.vue:39-45`

### 3.4 Fechamento comercial em Serviços

`src/views/ServicosView.vue` lista bem as competências, mas falta camada comercial:

- para quem é
- quais problemas resolve
- formato de atuação
- entregáveis
- como contratar
- CTA final

### 3.5 Sinais de confiança rápidos

Autoridade real existe, mas poderia ser escaneável com blocos como:

- +25 anos de experiência
- CTO e fundador desde 1998
- Doutor UFSC / INSA-Rouen
- Professor / pesquisador
- X publicações / orientações
- Instituições: UFSC, Unigranrio/Afya, ProFuzzy, etc.
- depoimentos, logos, prêmios, menções

## 4. Melhorias de design

### 4.1 Home mais escaneável

Ordem ideal para conversão:

1. headline forte + subtítulo curto + CTAs
2. provas rápidas / métricas
3. projetos em destaque
4. capacidades
5. trajetória resumida

Hoje a timeline completa ocupa espaço demais para landing principal.
Ref: `src/views/HomeView.vue:177-215`

### 4.2 Avatar genérico

Círculo com letra “D” passa sensação de placeholder (`src/views/HomeView.vue:126-128`).
Melhorar com:

- foto profissional, ou
- monograma / marca pessoal mais refinada

### 4.3 Nuvem de tecnologias pouco estratégica

Grupos existem no código, mas a UI achata tudo em ordem alfabética (`src/views/HomeView.vue:147-159`).
Melhor:

- destacar 6–10 tecnologias-chave, ou
- manter agrupamento visual por categoria, ou
- priorizar capacidades e casos reais sobre lista de ferramentas

### 4.4 Navbar com risco no mobile

Nav horizontal com 5 links + toggle, sem menu mobile (`src/components/NavBar.vue:20-43`).
Melhorar com:

- menu mobile / drawer
- CTA de contato no header
- estado ativo mais forte
- `scrollBehavior` no router

### 4.5 Blog vazio

Rota com “Nenhum post publicado ainda” reduz percepção de acabamento (`src/views/BlogView.vue:5-13`).
Melhor:

- ocultar até ter 2–3 posts, ou
- renomear para Notas / Insights / Publicações, ou
- publicar textos-semente curtos

### 4.6 Footer fraco

Só copyright (`src/components/Footer.vue:1-4`).
Footer profissional deveria ter:

- e-mail
- sociais / acadêmicos
- mini CTA
- localização opcional
- link CV / Lattes

## 5. UX, acessibilidade e polish

- Contraste: uso intenso de `text-brand-dark/40` e `/60` sobre fundos translúcidos pode prejudicar legibilidade, sobretudo no dark mode.
- Texto de apoio muito em `text-sm`; priorizar `text-base` para conteúdo principal.
- Falta `focus-visible` claro; interações dependem muito de `hover`.
- Toggle de tema é só ícone com `title`; adicionar `aria-label` (`src/components/NavBar.vue:35-42`).
- Tabs/acordeões do Acadêmico precisam de semântica ARIA: `aria-selected`, `aria-expanded`, `aria-controls` (`src/views/AcademicoView.vue:131-175`).
- Adicionar skip link em `src/App.vue`.
- Timeline com colunas fixas `64px / 24px / 1fr` pode apertar no mobile (`src/views/HomeView.vue:180-186`).
- Charts são visuais; adicionar resumos textuais equivalentes.
- Alguns nomes de projetos parecem slugs de repo (`gerador_historias`, `cosmic-ppt-gen`, `deep_research`); normalizar títulos para apresentação.
- Mistura de `@lucide/vue` e `lucide-vue-next`; padronizar em um pacote.
- `index.html` só tem `title`; faltam meta description e Open Graph / social preview.

## 6. Priorização sugerida

### Prioridade alta

- [ ] Reescrever hero com headline, subtítulo e CTA.
- [ ] Adicionar contato visível no header, hero e footer.
- [ ] Destacar projetos selecionados com prova de resultado.
- [ ] Ocultar/retrabalhar blog vazio.
- [ ] Trocar avatar placeholder por foto/identidade real.

### Prioridade média

- [ ] Resumir timeline da home; mover cronologia completa para CV.
- [ ] Tornar Serviços mais comercial.
- [ ] Adicionar métricas e instituições.
- [ ] Melhorar navegação mobile.
- [ ] Aumentar contraste de textos secundários.

### Prioridade baixa

- [ ] Ajustes finos de acessibilidade.
- [ ] Meta description + Open Graph.
- [ ] Padronização de nomes/descrições de projetos.
- [ ] Unificação de ícones e variantes de card/CTA.

## 7. Direção por objetivo

Se foco for clientes:

- destacar problemas resolvidos, casos e impacto
- linguagem orientada a resultado
- CTA de conversa / consultoria

Se foco for recrutadores:

- destacar cargo-alvo, stack principal, impacto
- facilitar CV, LinkedIn, GitHub, Lattes

Se foco for híbrido:

- separar trilhas: Para empresas / Portfólio / Acadêmico
- resumir academia na Home e manter detalhe como material de apoio

## 8. Próximos passos possíveis

1. checklist priorizado de melhorias
2. avaliação com nota por critério
3. proposta de reorganização completa da home
4. texto novo para hero e seções principais
