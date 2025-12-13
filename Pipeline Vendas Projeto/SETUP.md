# 🛠️ Setup do Ambiente — Pipeline de Análise de Vendas

Este documento descreve **passo a passo** como configurar o ambiente necessário para executar este projeto localmente, mesmo para quem **está começando do zero** em Python e Análise de Dados.

---

## 1️⃣ Instalação do Python

### 🎯 Objetivo
Instalar o Python, linguagem utilizada em todo o projeto (ETL, EDA e análises).

### 📌 Passos
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão **Python 3.11 ou superior**
3. Durante a instalação, marque a opção **Add Python to PATH**
4. Clique em **Install**

### ✅ Verificação
Abra o terminal e execute:
python --version

Se retornar algo como *Python 3.11.x*, a instalação foi concluída.

---

## 2️⃣ Instalação do VS Code

### 🎯 Objetivo
Utilizar um editor moderno para escrever código e executar notebooks.

### 📌 Passos
1. Acesse: https://code.visualstudio.com/
2. Baixe e instale normalmente

### 🔌 Extensões necessárias
- Python (Microsoft)
- Jupyter (Microsoft)

---

## 3️⃣ Obter o projeto

### 🔹 Clonar com Git
git clone https://github.com/Daashy/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

### 🔹 Ou baixar manualmente
- Code → Download ZIP
- Extraia a pasta
- Abra no VS Code com **File → Open Folder**

---

## 4️⃣ Criar ambiente virtual (.venv)

### 🎯 Objetivo
Isolar as dependências do projeto.

### 📌 Comando
python -m venv .venv

---

## 5️⃣ Ativar o ambiente virtual

### ▶ Windows
.venv\Scripts\activate

Caso dê erro:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### ▶ Linux / macOS
source .venv/bin/activate

---

## 6️⃣ Selecionar interpretador no VS Code

- Ctrl + Shift + P
- Python: Select Interpreter
- Escolha o Python dentro da pasta .venv

---

## 7️⃣ Instalar bibliotecas

pip install pandas numpy matplotlib seaborn jupyter

---

## 8️⃣ requirements.txt

Conteúdo:
pandas
numpy
matplotlib
seaborn
jupyter

Instalar:
pip install -r requirements.txt

---

## 9️⃣ Executar ETL

python src/etl/etl_ingestao.py
python src/etl/etl_cleaning.py

---

## 🔟 Executar EDA

Abra:
notebooks/eda/EDA_superstore.ipynb

Selecione o kernel do .venv e execute todas as células.

---

## 🧠 Dicas
- Sempre ative o .venv
- Reinicie o kernel ao instalar libs
- Use caminhos relativos

---

## ✍️ Autoria
Gustavo Fernandes  
GitHub: https://github.com/Daashy
