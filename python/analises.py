"""Análises do portfólio a partir dos CSVs (pandas)."""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
DADOS = BASE / "dados"

pubs = pd.read_csv(DADOS / "publicacoes-ultimos-5-anos.csv")
repos = pd.read_csv(DADOS / "github-repos.csv")
projs = pd.read_csv(DADOS / "projetos.csv")
ori = pd.read_csv(DADOS / "orientacoes.csv")


def ranking_ano_publicacoes():
    print("== Ranking de publicações por ano ==")
    print(pubs.groupby("ano").size().sort_values(ascending=False))
    print("\n== Por ano e tipo ==")
    print(pubs.groupby(["ano", "tipo"]).size().unstack(fill_value=0))


def filtrar_publicacoes(tipo=None, ano=None, qualis=None):
    df = pubs
    if tipo:
        df = df[df["tipo"] == tipo]
    if ano:
        df = df[df["ano"] == ano]
    if qualis:
        df = df[df["qualis"] == qualis]
    return df


def repos_por_categoria():
    print("== Repos por categoria ==")
    print(repos.groupby("category").size().sort_values(ascending=False))


if __name__ == "__main__":
    ranking_ano_publicacoes()
    print()
    repos_por_categoria()
    print("\n== Artigos A3 ==")
    print(filtrar_publicacoes(tipo="artigo", qualis="A3")[["ano", "titulo"]].to_string(index=False))
