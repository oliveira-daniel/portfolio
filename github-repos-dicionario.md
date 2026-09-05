# Dicionário de Dados - Repositórios GitHub

## Visão Geral

Este documento descreve a estrutura e metadados dos repositórios GitHub do usuário `oliveira-daniel`.

**Total de Repositórios:** 46
**Públicos:** 14
**Privados:** 31
**Forks:** 1

---

## Estrutura do CSV

### Colunas

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `name` | string | Nome do repositório no GitHub | `portfolio` |
| `description` | string | Descrição breve do repositório | `Gestão de projetos e desenho de processos PERT.` |
| `visibility` | enum | Visibilidade do repositório | `public`, `private`, `public;fork` |
| `updated_at` | datetime | Data e hora da última atualização (ISO 8601) | `2026-09-05T06:12:00Z` |
| `category` | string | Categoria temática do repositório | `Machine Learning & AI` |

---

## Detalhamento dos Campos

### `name`
- **Descrição:** Identificador único do repositório na conta do usuário
- **Formato:** String em kebab-case (lowercase com hífens)
- **Restrições:** Deve ser único dentro da conta do usuário
- **Observações:** Pode conter letras minúsculas, números e hífens

### `description`
- **Descrição:** Resumo opcional que explica o propósito do repositório
- **Formato:** String de texto livre
- **Restrições:** Limite de 500 caracteres no GitHub
- **Observações:** Campo pode estar vazio (`null`)

### `visibility`
- **Descrição:** Indica se o repositório é acessível publicamente
- **Valores possíveis:**
  - `public` - Repositório visível para todos
  - `private` - Repositório visível apenas para o dono e colaboradores autorizados
  - `public;fork` - Repositório forkado de outro usuário (visível publicamente)

### `updated_at`
- **Descrição:** Data e hora da última modificação feita no repositório
- **Formato:** ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
- **Fuso horário:** UTC
- **Observações:** Atualizado automaticamente pelo GitHub a cada push

### `category`
- **Descrição:** Categoria temática do repositório baseada em análise de conteúdo e propósito
- **Formato:** String classificatória
- **Valores possíveis:**
  - `Machine Learning & AI` - Projetos de IA, ML, redes neurais, fuzzy logic
  - `Automação & Workflows` - Automações, n8n, PPT generation com IA
  - `Transporte & Logística` - Análise de viagens, busca de empresas, concessões
  - `Educação & Laboratórios` - Cursos, laboratórios virtuais, materiais de aula
  - `Saúde` - Prontuários, clínicas, sistemas médicos
  - `Jogos & GameDev` - Jogos, tutoriais, física, visualização, storyboards
  - `Outros Projetos` - Portfólios, frameworks, projetos diversos
- **Observações:** Classificação subjetiva baseada em descrição e nome do repositório

---

## Categorias Temáticas

### Machine Learning & AI — *Inteligência que aprende*
- `deep_research`
- `neuro-fuzzy`
- `Fuzzy-Logic-Blueprint`
- `Experimentos-RN`
- `gerador_historias`
- `design-gest-o-projetos`
- `MAGMA-Framework`

### Automação & Workflows — *Eficiência em escala*
- `n8n-workflow`
- `cosmic-ppt-gen`
- `Visual-Shorts-Storyboarder`

### Transporte & Logística — *Mobilidade inteligente*
- `Analise-viagens`
- `Busca-Empresas-Transporte`
- `Radar-Concessoes`

### Educação & Laboratórios — *Conhecimento que transforma*
- `Laboratorio-Virtual`
- `curador-digital-unigranrio`
- `AulasProjCustom`
- `revisao-javascript`
- `ava-blackboard-test`
- `Fabrica-Prod-Educ`
- `MoodleUnigama`

### Saúde & Bem-estar
- `prontuario`
- `OncoCore`
- `clinica-terapeutica`
- `home-routine-tracker`

### Jogos & GameDev — *Mundos interativos*
- `livro-jogos-javascript-vol1`
- `Intro-jogos-javascript-videos`
- `sec-game`
- `TopDownGame`
- `Physics2DTest`
- `ARVisualization`
- `Board-Experiment`
- `JanelaDialogo`
- `Estruturas-de-dados-Jogos`
- `WorkshopViaCatarina`
- `Jam01_2017_1`
- `games-xp`

### Outros Projetos — *Explorações diversas*
- `portfolio`
- `Arqueometrico`
- `flask-hello-world`
- `flask-first`
- `javascript`
- `dom_css_javascript`
- `jekyll-now`
- `uni-logo`
- `NTesteAulas`
- `cloudsteam`

---

## Metadados do Arquivo

| Propriedade | Valor |
|-------------|-------|
| Codificação | UTF-8 |
| Separador | vírgula (`,`) |
| Delimitador de texto | aspas duplas (`"`) |
| Linha de cabeçalho | Sim |
| Encerramento de linha | LF (Unix) ou CRLF (Windows) |
