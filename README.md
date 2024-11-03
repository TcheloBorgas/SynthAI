# Projeto de Previsão de Churn, Risco de Crédito e Fraude Financeira
Este projeto visa desenvolver e implementar modelos de machine learning para previsão de churn (cancelamento de clientes), risco de crédito e fraude financeira, com uma API modular para gerenciamento dos modelos e uma interface simplificada em Streamlit para visualização e interação.

## Índice
* Visão Geral do Projeto
* Funcionalidades
* Estrutura do Projeto
* Instalação
* Uso
* Contribuição
* Licença


## Visão Geral do Projeto
O objetivo deste projeto é fornecer uma solução de machine learning para empresas que desejam monitorar e gerenciar três áreas críticas:

1. Churn: Identificação de clientes com maior probabilidade de cancelamento.
2. Risco de Crédito: Avaliação do risco de inadimplência de novos clientes ou concessão de crédito.
2. Fraude Financeira: Detecção de atividades suspeitas e potencialmente fraudulentas.

Combinamos a criação desses modelos com uma API modular que permite a fácil gestão e implementação dos modelos individualmente e um frontend em Streamlit para interação simplificada.

## Funcionalidades
* Modelo de Previsão de Churn: Analisa dados históricos de clientes para prever a probabilidade de churn.
* Modelo de Previsão de Risco de Crédito: Avalia o risco de crédito baseado em dados financeiros e de histórico de pagamentos.
* Modelo de Previsão de Fraude Financeira: Detecta padrões que podem indicar fraude com base em transações e comportamentos financeiros.
* API Modular: Interface de API para integração e gestão dos modelos individualmente, com endpoints dedicados.
* Frontend em Streamlit: Interface amigável para exibição e teste dos resultados dos modelos, acessível via navegador.


## Estrutura do Projeto
```
│   .gitignore
│   LICENSE
│   Organização Sprint 1 Chall.docx
│   QA_SPRINT1.pdf
│   README.md
│   requirements.txt
│   SPRINT 3 IA.mp4
│
├───IA
│   ├───app
│   │   │   logs.log
│   │   │   main.py
│   │   │
│   │   ├───api
│   │   │   ├───churn_model
│   │   │   │   │   churn_api.py
│   │   │   │   │   churn_pipeline.joblib
│   │   │   │   │   model
│   │   │   │   │   __init__.py
│   │   │   │   │
│   │   │   │   └───__pycache__
│   │   │   │           churn_api.cpython-311.pyc
│   │   │   │           churn_pipeline.joblib
│   │   │   │           __init__.cpython-311.pyc
│   │   │   │
│   │   │   ├───credit_risk_model
│   │   │   │   │   credit_risk_api.py
│   │   │   │   │   credit_risk_pipeline.pkl
│   │   │   │   │   expected_columns.joblib
│   │   │   │   │   __init__.py
│   │   │   │   │
│   │   │   │   └───__pycache__
│   │   │   │           credit_risk_api.cpython-311.pyc
│   │   │   │           __init__.cpython-311.pyc
│   │   │   │
│   │   │   └───fraud_detection_model
│   │   │       │   fraud_api.py
│   │   │       │   fraud_detection_pipeline.joblib
│   │   │       │   __init__.py
│   │   │       │
│   │   │       └───__pycache__
│   │   │               fraud_api.cpython-311.pyc
│   │   │               __init__.cpython-311.pyc
│   │   │
│   │   ├───template
│   │   │       streamlit.py
│   │   │
│   │   └───__pycache__
│   │           main.cpython-311.pyc
│   │
│   └───Data
│           fraud_dataset_example.csv
│           WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├───Models
│   ├───Churn
│   │       graph Churn-churn.png
│   │       graph churn-dep .png
│   │       graph churn-MC.png
│   │       matrix cnf.png
│   │       model
│   │       Ragnar_v5.ipynb
│   │
│   ├───Fraude Financeira
│   │       Detec_Fraude  - Aula 5.4.ipynb
│   │
│   └───Risco de Credito
│           logs.log
│           map_cartopy.png
│           Modelo RC.ipynb
│           num.png
│
└───Prototipagem
        Fluxograma da API.vsdx
        Fluxograma de Funcionamento Geral.vsdx
        Fluxograma dos Modelos de ML.vsdx
        Fluxograma Geral.vsdx
        Fluxograma Tratamento e Analise de Dados.vsdx
        Links sprint 2.txt
        Pitch_sprint1.mp4
```

# Descrição das Pastas

* models/: Contém os scripts de cada modelo (churn, risco de crédito e fraude).
* api/: API modular, com um arquivo app.py para iniciar a API e um endpoint específico para cada modelo.
* streamlit_app/: Aplicação em Streamlit para frontend simplificado.
* data/: Contém os datasets para treinamento e teste dos modelos.


## Instalação
1. Clone o repositório:
```
git clone https://github.com/TcheloBorgas/SynthAI
```

2. Execute a API:
```
cd app/api
python main.py
```

3. Inicie a aplicação em Streamlit:
```
cd frontend
streamlit run streamlit.py
```

# Uso

Após configurar o ambiente e rodar a API e o frontend, você pode acessar a interface do Streamlit no navegador para:

* Realizar previsões de churn, risco de crédito e fraude, com visualização dos resultados.
* Gerenciar os modelos de forma modular pela API.


Cada modelo possui endpoints específicos, por exemplo:

* POST /churn/predict - Realiza uma previsão de churn.
* POST /credit-risk/predict - Realiza uma previsão de risco de crédito.
* POST /fraud/predict - Realiza uma previsão de fraude.



## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a Licença MIT.