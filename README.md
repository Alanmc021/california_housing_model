# **🏡 Projeto: Previsão de Valores de Casas na Califórnia**

Este repositório contém um projeto de **Machine Learning** focado na previsão de valores de casas na Califórnia usando o **California Housing Dataset**. O objetivo é desenvolver um modelo preditivo para estimar o valor mediano das casas com base em características socioeconômicas e geográficas.

## 🚀 **Objetivos do Projeto**

### 📊 **1. Análise Exploratória de Dados (EDA)**
- Compreender a estrutura e características do dataset.
- Identificar padrões, correlações e outliers.

### 🤖 **2. Modelagem Preditiva**
- Criar um pipeline de Machine Learning.
- Treinar e avaliar modelos de regressão para prever preços.

### 🌍 **3. Deploy do Modelo**
- Criar uma API com **FastAPI** para disponibilizar previsões.
- Salvar e versionar o modelo treinado.

### 📄 **4. Documentação e Reproducibilidade**
- Garantir que o projeto seja bem documentado e de fácil replicabilidade.

---

## 📂 **Dataset: California Housing Dataset**

O dataset utilizado é o **California Housing Dataset**, disponível no `scikit-learn`. Ele contém informações de distritos da Califórnia, incluindo:

### 📌 **Features**
- `MedInc`: Renda média dos residentes.
- `HouseAge`: Idade média das casas.
- `AveRooms`: Número médio de cômodos por residência.
- `AveBedrms`: Número médio de quartos por residência.
- `Population`: População do distrito.
- `AveOccup`: Número médio de ocupantes por residência.
- `Latitude`: Latitude do distrito.
- `Longitude`: Longitude do distrito.

### 🎯 **Target (variável de saída)**
- `MedHouseVal`: Valor mediano das casas (em centenas de milhares de dólares).

O dataset possui **20.640 amostras** e **8 features**. Ele foi derivado do censo dos EUA de 1990 e é amplamente utilizado para tarefas de regressão.

---

## 📌 **Etapas do Projeto**

### 🕵️‍♂️ **1. Análise Exploratória de Dados (EDA)**

**Visualização de Dados:**
- Histogramas para distribuição das variáveis.
- Scatter plots para análise de localização geográfica x valor das casas.
- Pair plots para identificar correlações entre features.

**Tratamento de Dados:**
- Identificação e remoção de outliers.
- Normalização e padronização dos dados.

### ⚡ **2. Modelagem Preditiva**

**Pipeline de Machine Learning:**
- Pré-processamento com `StandardScaler`.
- Treinamento de modelo **Ridge Regression** (`RidgeCV`).
- Validação cruzada para evitar overfitting.

**Desempenho do Modelo:**
- **Score R² médio:** `0.553 ± 0.062` (modelo explica 55.3% da variância do target).

### 🌐 **3. Deploy do Modelo**

**Criação de uma API com FastAPI**
- Endpoint `/predict` que recebe os dados e retorna o valor previsto da casa.
- **Exemplo de requisição:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
  ```

**Salvamento do Modelo:**
- O modelo treinado foi salvo como `california_housing_model.pkl`.

---

## 🛠 **Tecnologias Utilizadas**

| Tecnologia | Uso |
|------------|-----|
| **Python** | Linguagem principal do projeto |
| **Scikit-learn** | Treinamento do modelo |
| **Pandas / NumPy** | Manipulação e análise de dados |
| **Matplotlib / Seaborn** | Visualização de dados |
| **FastAPI** | Criação da API |
| **Joblib** | Salvamento e carregamento do modelo |

---

## 📁 **Estrutura do Repositório**

```plaintext
📂 projeto-previsao-casas/
│── 📜 README.md                # Documentação do projeto
│── 📜 requirements.txt         # Dependências do projeto
│── 📝 Untitled5.ipynb # Notebook com análise e modelagem
│── 🚀 main.py                   # Código da API FastAPI
│── 🎯 california_housing_model.pkl  # Modelo treinado
└── 📂 data/                     # Diretório de armazenamento dos dados
```

---

## 💻 **Como Executar o Projeto**

### 1️⃣ **Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/projeto-previsao-casas.git
cd projeto-previsao-casas
```

### 2️⃣ **Instale as Dependências**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Execute o Jupyter Notebook (opcional)**
```bash
jupyter notebook
```
Abra `california_housing_analysis.ipynb` para visualizar a análise exploratória e treinamento do modelo.

### 4️⃣ **Inicie a API**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Acesse `http://127.0.0.1:8000/docs` para testar a API via Swagger UI.

---

## 📌 **Autor**

👤 [Alan Martins](https://github.com/seu-usuario)
 

