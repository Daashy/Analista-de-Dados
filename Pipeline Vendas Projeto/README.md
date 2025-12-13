## ✍️ Autoria
Projeto desenvolvido por **Gustavo Fernandes** como parte de estudos em Análise de Dados.
Este repositório tem fins educacionais e demonstrativos.

-----------------

# 📊 Pipeline de Análise de Vendas — Superstore

## 🎯 Objetivo do Projeto
Este projeto tem como objetivo simular um **pipeline completo de dados**, semelhante ao encontrado em ambientes corporativos, passando pelas etapas de **ingestão, tratamento (ETL), análise exploratória (EDA)** e geração de **insights estratégicos** para apoio à tomada de decisão.

O foco principal é **avaliar o impacto da política de descontos no lucro**, identificar riscos de rentabilidade e propor **recomendações acionáveis de negócio**.

---

## 🧱 Estrutura Geral do Projeto

O projeto foi organizado seguindo boas práticas de engenharia e análise de dados:

Pipeline Vendas Projeto/
│
├── README.md ← Visão geral do projeto
├── LICENSE ← Licença MIT
│
├── data/
│ ├── raw/ ← Dados brutos (originais)
│ ├── interim/ ← Dados intermediários
│ └── processed/ ← Dados tratados e prontos para análise
│
├── src/
│ └── etl/
│ ├── etl_ingestao.py ← Ingestão e extração dos dados
│ └── etl_cleaning.py ← Limpeza, padronização e transformação
│
├── notebooks/
│ └── eda/
│ ├── EDA_superstore.ipynb ← Análise exploratória completa
│ └── README.md ← Documentação específica do EDA
│
└── dashboards/
└── (em desenvolvimento)

---

## 🔄 Etapas do Projeto

### 1️⃣ Ingestão de Dados
- Extração do dataset Superstore a partir de fonte pública
- Organização dos dados brutos na camada `raw`
- Preparação para processamento posterior

📂 Scripts: `src/etl/etl_ingestao.py`

---

### 2️⃣ ETL — Limpeza e Transformação
Nesta etapa foram realizadas:
- Padronização de nomes de colunas
- Conversão correta de tipos de dados (datas e numéricos)
- Remoção de registros inválidos
- Criação de colunas derivadas (ano, mês, margem de lucro)
- Salvamento do dataset final na camada `processed`

📂 Scripts: `src/etl/etl_cleaning.py`

---

### 3️⃣ Análise Exploratória de Dados (EDA)
A etapa de EDA teve como foco **entender o comportamento do negócio** e identificar padrões, riscos e oportunidades.

Principais análises realizadas:
- Visão geral de vendas e lucro
- Evolução temporal das vendas
- Análise por categoria, região e segmento
- Avaliação de eficiência (vendas × lucro)
- Estudo aprofundado da política de descontos

📂 Notebook: `notebooks/eda/EDA_superstore.ipynb`  
📄 Documentação detalhada: `notebooks/eda/README.md`

---

## 🔍 Principais Insights

- **Technology** lidera o faturamento total.
- **Office Supplies** apresenta maior eficiência operacional, com melhor relação entre vendas e lucro.
- Aproximadamente **70% das vendas com desconto concentram-se na faixa de 20%**.
- Descontos acima de **20%** apresentam impacto negativo consistente no lucro médio.
- A categoria **Furniture concentra mais de 250 mil em vendas com prejuízo**, superando a soma das demais categorias.
- A região **Central** apresenta alto volume de vendas, porém baixa eficiência em lucro.

---

## ⚠️ Riscos Identificados
- Política de descontos excessivamente agressiva.
- Alta concentração de prejuízo na categoria Furniture.
- Redução significativa da margem em níveis elevados de desconto.

---

## ✅ Recomendações de Negócio
- Definir **limite padrão de até 10% de desconto** para preservar margem.
- Permitir **até 20% apenas em compras recorrentes ou de alto volume**.
- Revisar política comercial da categoria Furniture.
- Realizar análises regionais específicas para ajuste de estratégia.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Pandas, NumPy)
- **Matplotlib & Seaborn** (visualização)
- **Git & GitHub**
- **Jupyter Notebook**

---

## 🚀 Status do Projeto
🟡 Em desenvolvimento  
Próximas etapas incluem:
- Construção de dashboards (Power BI)
- Storytelling visual para stakeholders
- Consolidação final para portfólio profissional

---

## ✍️ Autoria
Projeto desenvolvido por **Gustavo Fernandes**  
GitHub: https://github.com/Daashy

Este repositório tem fins educacionais e demonstrativos, com foco em aprendizado prático e portfólio profissional.

## 📜 Licença
Este projeto está licenciado sob a licença MIT — consulte o arquivo `LICENSE` para mais detalhes.
