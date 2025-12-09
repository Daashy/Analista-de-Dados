import os
import pandas as pd
import numpy as np


# 1. Localização das pastas do objeto

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
INTERIM_DIR = os.path.join(PROJECT_ROOT, "data", "interim")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

def limpar_dados():
    """ Carrega o CSV do interim, limpa, transforma e salva no processed. """

    #2. Carregar o arquivo
    file_path = os.path.join(INTERIM_DIR, "Sample - Superstore.csv")
    df = pd.read_csv(file_path, encoding="latin-1")

    print ("Dataset carregado, Linhas: ",len(df))

    #3. Padronizando nomes de colunas
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")

    )

    print("Colunas padronizadas.")

    #4. Convertendo as datas
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    print("Datas Convertidas")

    #5. Converter númericos corretamente
    numeric_cols =["sales", "quantity", "discount", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Colunas numéricas convertidas.")

    #6. Remover linhas completamente vazias

    df = df.dropna(how="all")

    #7 Criar colunas úteis
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.to_period("M")
    df["profit_margin"] = df ["profit"] / df["sales"]

    print("Colunas derivadas criadas.")

    #8 Salvar dataset limpo na nasta proccessed

    outpath_path = os.path.join(PROCESSED_DIR, "superstore_clean.csv")
    df.to_csv(outpath_path, index=False, encoding="utf-8")

    print("Dados limpos e salvos em:", outpath_path)

if __name__ == "__main__":
    limpar_dados()