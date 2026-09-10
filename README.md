# Portfólio Pessoal — Daniel de Oliveira

Site de portfólio profissional desenvolvido com Vue 3, Vite e TailwindCSS.

![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub_Pages-blue?logo=github-pages)
![Framework](https://img.shields.io/badge/Framework-Vue_3-green?logo=vue.js)
![Build](https://img.shields.io/badge/Build-Vite-orange?logo=vite)
![Styling](https://img.shields.io/badge/Styling-TailwindCSS-pink?logo=tailwind-css)

---

## 🚀 Demonstração

O site está hospedado em:

- **GitHub Pages**: [https://oliveira-daniel.github.io/portfolio/](https://oliveira-daniel.github.io/portfolio/)

---

## 📋 Visão Geral

Site de portfólio pessoal construído com tecnologias modernas de frontend. Apresenta:

- **Home** — Introdução e resumo profissional
- **Trajetória** — Histórico de formação e experiência
- **Serviços** — Áreas de atuação (IA Aplicada, Automações, Produtos Educacionais, etc.)
- **Projetos** — Portfólio de projetos acadêmicos e profissionais
- **Blog** — Artigos e publicações
- **Acadêmico** — Qualificações e certificações
- **Contato** — Formulário de contato e links redes sociais

---

## 🛠️ Stack Tecnológica

| Tecnologia        | Versão   | Uso                        |
|-------------------|----------|----------------------------|
| Vue 3             | ^3.5.42  | Framework principal        |
| Vite              | ^8.2.2   | Bundler e servidor de dev  |
| TypeScript        | ^6.0.2   | Tipagem estática           |
| Vue Router        | ^4.6.4   | Roteamento SPA             |
| TailwindCSS       | ^4.3.3   | Estilização                |
| Chart.js          | ^4.5.1   | Gráficos e visualizações   |
| @lucide/vue       | ^1.41.0  | Ícones                     |
| chartjs-plugin-datalabels | ^2.2.0 | Rótulos em gráficos  |

---

## 📁 Estrutura do Projeto

```
portfolio/
├── portfolio-site/                  # Frontend do portfólio
│   ├── public/                      # Assets estáticos (fotos, ícones, PDFs)
│   │   ├── favicon.svg
│   │   ├── og-cover.png
│   │   └── cv-daniel-oliveira.pdf
│   ├── src/
│   │   ├── components/              # Componentes reutilizáveis
│   │   │   ├── NavBar.vue
│   │   │   ├── Footer.vue
│   │   │   ├── GlassCard.vue
│   │   │   ├── TechBadge.vue
│   │   │   ├── DonutChart.vue
│   │   │   └── QualisChart.vue
│   │   ├── views/                   # Páginas do site
│   │   │   ├── HomeView.vue
│   │   │   ├── TrajetoriaView.vue
│   │   │   ├── ServicosView.vue
│   │   │   ├── ProjetosView.vue
│   │   │   ├── BlogView.vue
│   │   │   └── AcademicoView.vue
│   │   ├── data/                    # Dados do portfólio (JSON)
│   │   │   ├── portfolio.json
│   │   │   ├── projetos.json
│   │   │   ├── contato.json
│   │   │   ├── tech-icons.json
│   │   │   └── publicacoes-*.json
│   │   ├── router/
│   │   │   └── index.ts             # Configuração de rotas
│   │   ├── style.css                # Estilos globais
│   │   └── main.ts                  # Ponto de entrada
│   ├── scripts/
│   │   └── gen_cv.py                # Gera PDF do currículo
│   ├── dist/                        # Build de produção (gerado)
│   ├── index.html                   # HTML base
│   ├── vite.config.ts               # Configuração do Vite
│   ├── tsconfig.json                # Configuração do TypeScript
│   ├── package.json
│   └── public/404.html              # Fallback para SPA routing
├── conteudos-site/
├── curriculos/
├── dados/
├── modelos-design/
├── python/
├── .github/
│   └── workflows/
│       └── deploy.yml               # CI/CD para GitHub Pages
├── README.md
└── .gitignore
```

---

## 🚀 Como Rodar Localmente

### Pré-requisitos
- [Node.js](https://nodejs.org/) (versão 20+)
- [npm](https://www.npmjs.com/)
- [Python 3](https://www.python.org/) (para gerar o currículo PDF)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/oliveira-daniel/portfolio.git
cd portfolio/portfolio-site

# Instale as dependências
npm install

# Execute o servidor de desenvolvimento
npm run dev
```

O site estará disponível em `http://localhost:5173`.

### Build de Produção

```bash
npm run build
```

O build gerado ficará na pasta `dist/`.

### Gerar Currículo PDF

```bash
npm run cv
```

---

## 🌐 Deploy Automático

O projeto utiliza **GitHub Actions** para deploy automático na branch `main`. A cada push, o workflow executa:

1. **Checkout** do código
2. **Install** de dependências dentro de `portfolio-site/`
3. **Build** do projeto (`npm run build`)
4. **Deploy** para GitHub Pages

O arquivo de configuração está em `.github/workflows/deploy.yml`.

### Configuração no GitHub

1. Acesse o repositório no GitHub
2. Vá em **Settings → Pages**
3. Em **Source**, selecione **GitHub Actions**

---

## ⚙️ Configuração Importante

O projeto está configurado para funcionar no sub-diretório `/portfolio/` do GitHub Pages:

- **`vite.config.ts`** — `base: '/portfolio/'`
- **`src/router/index.ts`** — `createWebHistory('/portfolio/')`
- **`public/404.html`** — Redirecionamento para SPA routing

O workflow usa `working-directory: portfolio-site` para rodar os comandos no diretório correto.

Se for implantar na raiz do domínio, altere o `base` para `'/'` em `vite.config.ts` e `router/index.ts`.

---

## 📝 Contato

- **E-mail**: daniel.tech.edu@gmail.com
- **LinkedIn**: [Daniel Oliveira](https://www.linkedin.com/in/daniel-oliveira-dr/)
- **GitHub**: [oliveira-daniel](https://github.com/oliveira-daniel)
- **Lattes**: [Currículo Lattes](https://lattes.cnpq.br/0984344989835257)

---

## 📄 Licença

Este projeto é de uso pessoal e acadêmico. Todos os direitos reservados.
