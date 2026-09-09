# -*- coding: utf-8 -*-
"""Gera public/cv-daniel-oliveira.pdf a partir dos dados do site.

Uso:  npm run cv   (ou: python3 scripts/gen_cv.py, a partir de portfolio-site/)

Regras ATS aplicadas: sem tabelas, sem colunas, sem graficos, sem imagens,
fontes padrao (Helvetica, latin-1), cabecalhos de secao simples, ordem
anticronologica, metadados do documento preenchidos e URLs em texto.
Publicacoes selecionadas lidas de src/data/publicacoes-ultimos-5-anos.json.

Dependencia: pip install fpdf2 pypdf  (pypdf so para verificacao manual)
"""
import json
from pathlib import Path
from fpdf import FPDF
from fpdf.enums import XPos, YPos

NX = XPos.LMARGIN
NY = YPos.NEXT

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "public" / "cv-daniel-oliveira.pdf"

DARK = (32, 55, 47)
GREEN = (81, 142, 69)
GRAY = (90, 90, 90)
BLACK = (30, 30, 30)


def clean(s):
    s = str(s)
    for a, b in [
        ("–", "-"), ("—", "-"), ("‘", "'"), ("’", "'"),
        ("“", '"'), ("”", '"'), ("…", "..."), ("�", ""),
    ]:
        s = s.replace(a, b)
    return s.encode("latin-1", errors="ignore").decode("latin-1")


with open(BASE / "src" / "data" / "publicacoes-ultimos-5-anos.json",
          encoding="utf-8", errors="replace") as f:
    pubs = json.load(f)

rank = {"A2": 0, "A3": 1, "A4": 2}
selected = sorted(
    [p for p in pubs if p.get("tipo") == "artigo" and p.get("qualis") in rank],
    key=lambda p: (rank[p["qualis"]], p["ano"]),
)


class CV(FPDF):
    def section(self, title):
        self.ln(4)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*GREEN)
        self.cell(0, 7, clean(title).upper(), new_x=NX, new_y=NY)
        self.set_draw_color(*GREEN)
        self.set_line_width(0.4)
        self.line(self.l_margin, self.get_y(), 210 - self.r_margin, self.get_y())
        self.ln(2)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.2, clean(text), new_x=NX, new_y=NY)
        self.ln(1)

    def job(self, title, org_period, bullets):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*BLACK)
        self.cell(0, 5.5, clean(title), new_x=NX, new_y=NY)
        if org_period:
            self.set_font("Helvetica", "I", 10)
            self.set_text_color(*GRAY)
            self.cell(0, 5.2, clean(org_period), new_x=NX, new_y=NY)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*BLACK)
        for b in bullets:
            self.multi_cell(0, 5.2, "- " + clean(b), new_x=NX, new_y=NY)
        self.ln(2)


pdf = CV()
pdf.set_margins(20, 18, 20)
pdf.set_auto_page_break(True, margin=20)
pdf.set_title("Daniel de Oliveira - CV")
pdf.set_author("Daniel de Oliveira")
pdf.set_subject("CTO, pesquisador e professor - IA aplicada, automação e otimização")
pdf.set_keywords("IA, automação, otimização, ensino, pesquisa, CTO, currículo")
pdf.add_page()

# Cabeçalho
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(*DARK)
pdf.cell(0, 10, "Daniel de Oliveira", new_x=NX, new_y=NY)
pdf.set_font("Helvetica", "", 11.5)
pdf.set_text_color(*GREEN)
pdf.cell(0, 6.5, "CTO, pesquisador e professor - IA aplicada, automação e otimização",
         new_x=NX, new_y=NY)
pdf.ln(2)
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 5.2, "E-mail: daniel.tech.edu@gmail.com  |  WhatsApp: +55 21 98330-1312",
         new_x=NX, new_y=NY)
pdf.cell(0, 5.2, "LinkedIn: linkedin.com/in/daniel-oliveira-dr",
         new_x=NX, new_y=NY, link="https://www.linkedin.com/in/daniel-oliveira-dr/")
pdf.cell(0, 5.2, "GitHub: github.com/oliveira-daniel  |  Lattes: lattes.cnpq.br/0984344989835257",
         new_x=NX, new_y=NY)

# Resumo
pdf.section("Resumo")
pdf.body(
    "CTO e sócio-fundador da ProFuzzy (desde 1998), pesquisador e professor com "
    "doutorado em Engenharia de Produção (UFSC, com doutorado-sanduíche no INSA-Rouen, "
    "França) e pós-doutorado em Engenharia e Gestão do Conhecimento (UFSC). Atua na "
    "interseção entre Inteligência Artificial, otimização combinatória e ensino: "
    "sistemas neuro-fuzzy, multiagentes, LLMs e pipelines RAG aplicados a plataformas "
    "de saúde e transporte, concessões públicas e projetos educacionais. Disponível "
    "para atuação PJ ou CLT, como liderança técnica, especialista ou consultor."
)

# Experiência
pdf.section("Experiência profissional")
pdf.job(
    "CTO / Sócio-fundador",
    "ProFuzzy Consultoria e Sistemas Ltda - 1998 - atual",
    [
        "Consultoria em otimização combinatória e IA aplicada.",
        "Produtos e plataformas com agentes inteligentes, RAG, dashboards e automações.",
    ],
)
pdf.job(
    "Pesquisador - GPIAE (IA na Educação)",
    "DEGC/UFSC - 2025 - atual",
    ["Grupo multidisciplinar de pesquisa em Inteligência Artificial na Educação."],
)
pdf.job(
    "Coordenador de Tecnologia e Inovação / Professor EAD / Coordenador de Curso",
    "Unigama - 2022 - 2024",
    ["Coordenação de tecnologia e inovação e de cursos, com atuação em EAD."],
)
pdf.job(
    "Professor Adjunto Doutor / Coordenador de Curso",
    "Universidade Unigranrio - 2018 - 2024",
    [
        "Coordenação geral de curso, Escritório de Inovação e PPG em Ensino das Ciências.",
        "Pesquisador do macroprojeto de Tecnologias Digitais e Recursos Didáticos no Ensino de Ciências e Matemática.",
    ],
)
pdf.job(
    "Professor autor / Professor",
    "Faculdade Descomplica, Instituto Infnet, GRAN Cursos - 2021 - 2023",
    ["Autoria e docência de conteúdos de computação para ensino superior e concursos."],
)
pdf.job(
    "Professor Adjunto Mestre / Coordenador de Curso",
    "Fatenp - Faculdade de Tecnologia Nova Palhoça - 2015 - 2018",
    ["Coordenação do Curso de Jogos Digitais."],
)
pdf.job(
    "Sócio-gerente",
    "Digipro Informática Ltda, Lages/SC - 2002 - 2014",
    ["Gestão e desenvolvimento de sistemas."],
)

# Formação
pdf.section("Formação acadêmica")
pdf.job("Pós-doutorado em Engenharia e Gestão do Conhecimento",
        "UFSC - 2026 - atual", [])
pdf.job("Doutorado em Engenharia de Produção e Sistemas",
        "UFSC - 2012 - 2017 (doutorado-sanduíche no INSA-Rouen, França, 2014 - 2015)",
        ["Tese em otimização e simulação de redes dinâmicas de transporte."])
pdf.job("Mestrado em Computação Aplicada", "Univali - 2008 - 2010", [])
pdf.job("Bacharelado em Informática",
        "Universidade do Planalto Catarinense - 2000 - 2006", [])

# Pesquisa
pdf.section("Pesquisa e produção")
pdf.body(
    "34 itens publicados nos últimos 5 anos (8 artigos em periódicos, 9 capítulos de "
    "livro e 17 trabalhos em anais de eventos), com classificação Qualis até A2. "
    "Orientações de mestrado concluídas e em andamento no PPG em Ensino das Ciências. "
    "Participação em grupos de pesquisa em logística, acessibilidade com Arduino, "
    "extração de informações da web e IA na educação. Currículo completo no Lattes."
)

# Publicações selecionadas
pdf.section("Publicações selecionadas")
for p in selected:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*BLACK)
    pdf.multi_cell(0, 5.2, clean(p["titulo"]), new_x=NX, new_y=NY)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5.2, clean(p["autores"]), new_x=NX, new_y=NY)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(
        0, 5.2,
        "%s, %s. Qualis %s." % (clean(p["veiculo"]), p["ano"], p["qualis"]),
        new_x=NX, new_y=NY,
    )
    pdf.set_text_color(*BLACK)
    pdf.ln(2)

# Habilidades
pdf.section("Habilidades técnicas")
pdf.body("IA e automação: Python, Agno, LangChain, n8n, PyTorch, sistemas multiagentes, "
         "RAG, LLMs, sistemas neuro-fuzzy (ANFIS).")
pdf.body("Frontend web: Vue, React, Tailwind CSS. Backend e APIs: FastAPI, Node.js.")
pdf.body("Otimização: algoritmos genéticos, fluxo em redes, programação matemática, "
         "roteirização e dimensionamento de frotas.")
pdf.body("Ensino: microlearning, gamificação, storytelling, trilhas adaptativas, "
         "laboratórios virtuais, EAD.")

# Idiomas
pdf.section("Idiomas")
pdf.body("Português (nativo), Inglês, Francês.")

pdf.output(OUT)
print("OK", OUT, "- pubs:", len(selected))
