# **Projeto: Previsão de Valores de Casas na Califórnia**

Este repositório contém um projeto de machine learning focado na previsão de valores de casas na Califórnia usando o **California Housing Dataset**. O objetivo é criar um modelo preditivo que estime o valor mediano das casas com base em características como renda média, idade das casas, localização geográfica e outras variáveis.

---

## **Objetivos do Projeto**

1. **Análise Exploratória de Dados (EDA)**:
   - Entender a estrutura e as características do dataset.
   - Identificar padrões, correlações e outliers.

2. **Modelagem Preditiva**:
   - Treinar um modelo de regressão para prever o valor mediano das casas.
   - Avaliar o desempenho do modelo usando validação cruzada.

3. **Colocar o Modelo em Produção**:
   - Criar uma API para servir o modelo treinado.
   - Disponibilizar o modelo para uso em um ambiente de produção.

4. **Documentação e Reproducibilidade**:
   - Garantir que o projeto seja bem documentado e reproduzível.

---

## **Dataset: California Housing Dataset**

O dataset utilizado é o **California Housing Dataset**, disponível na biblioteca `scikit-learn`. Ele contém informações sobre distritos na Califórnia, incluindo:

- **Features**:
  - `MedInc`: Renda média dos residentes.
  - `HouseAge`: Idade média das casas.
  - `AveRooms`: Número médio de cômodos por residência.
  - `AveBedrms`: Número médio de quartos por residência.
  - `Population`: População do distrito.
  - `AveOccup`: Número médio de ocupantes por residência.
  - `Latitude`: Latitude do distrito.
  - `Longitude`: Longitude do distrito.

- **Target**:
  - `MedHouseVal`: Valor mediano das casas (em centenas de milhares de dólares).

O dataset possui **20.640 amostras** e **8 features**. Ele foi derivado do censo dos EUA de 1990 e é amplamente utilizado para tarefas de regressão.

---

## **Trabalho Realizado**

### **1. Análise Exploratória de Dados (EDA)**

- **Visualização de Dados**:
  - Histogramas para entender a distribuição das features.
  - Scatter plots para analisar a relação entre localização geográfica e valor das casas.
  - Pair plots para identificar correlações entre as features.

- **Identificação de Outliers**:
  - Análise de estatísticas descritivas para detectar valores extremos.

### **2. Modelagem Preditiva**

- **Pipeline de Machine Learning**:
  - Criação de um pipeline com normalização (`StandardScaler`) e regressão Ridge (`RidgeCV`).
  - Treinamento do modelo com validação cruzada para garantir robustez.

- **Desempenho do Modelo**:
  - Score R² médio de **0.553 ± 0.062**, indicando que o modelo explica 55.3% da variância do target.

### **3. Colocação do Modelo em Produção**

- **API com FastAPI**:
  - Criação de um endpoint `/predict` que recebe dados de entrada e retorna o valor previsto da casa.
  - Exemplo de requisição:
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

- **Salvamento do Modelo**:
  - O modelo treinado foi salvo no Google Drive como `california_housing_model.pkl` para uso em produção.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação principal.
- **Scikit-learn**: Para criação e treinamento do modelo de regressão Ridge.
- **Pandas e NumPy**: Para manipulação e análise de dados.
- **Matplotlib e Seaborn**: Para visualização de dados.
- **FastAPI**: Para criar a API que serve o modelo treinado.
- **Joblib**: Para salvar e carregar o modelo.

---

## **Estrutura do Repositório**


---

### **Explicação das Formatações**

1. **Estrutura do Repositório**:
├── app.py # Código da API FastAPI
├── california_housing_analysis.ipynb # Notebook com análise e modelagem
├── california_housing_model.pkl # Modelo treinado
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

2. **Como Usar**:
   - Usei listas numeradas para os passos.
   - Blocos de código (```bash) para comandos de terminal.

3. **Autor**:
   - Usei quebras de linha (`  `) para separar nome e links.
   - Links podem ser adicionados usando Markdown, por exemplo:
     ```markdown
     [Meu Perfil no GitHub](https://github.com/seu-usuario)
     ```

---

### **Como Usar**
1. Copie o conteúdo acima.
2. Cole no seu arquivo `README.md`.
3. Substitua `[Nome do Autor]`, `[Link para o seu perfil no GitHub]` e `[Link para o seu LinkedIn]` pelas suas informações.

Se precisar de mais ajustes, é só avisar! 😊
