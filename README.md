# Análise de Churn e Estratégia de Redução

Este repositório apresenta uma abordagem para avaliar o cenário de "churn" (taxa de cancelamento) elevado de clientes em uma empresa de telecomunicações. A empresa deseja entender melhor por que seus clientes estão cancelando os serviços, especialmente considerando o alto custo de instalação envolvido.

## Contexto

A empresa de telecomunicações está enfrentando um desafio com a alta taxa de cancelamento entre seus clientes. Isso é particularmente problemático devido ao custo elevado associado à instalação dos serviços. Para abordar esse problema, a empresa busca uma estratégia eficaz para reduzir o churn e reter os clientes.

## Objetivos

- Analisar as principais razões por trás do cancelamento dos serviços.
- Identificar padrões nos comentários dos clientes para entender suas preocupações.
- Desenvolver um protótipo de produto para análise de clientes propensos a churn.

## Conjunto de Dados

O conjunto de dados inclui comentários dos clientes que cancelaram os serviços, juntamente com o tipo de serviço associado, além de informações pessoais e de contrato.

## Preparando o ambiente

Para criar o ambiente de execução, execute o comando `pip install -r requirements.txt` no diretório raiz do projeto.

## Executando a Análise

1. Clone este repositório para o seu ambiente local.
2. Abra o arquivo `analise-churn.ipynb` no seu editor de código.
3. Adapte os dados de exemplo no código para corresponder ao seu conjunto de dados real.
4. Execute o código para realizar a análise e obter insights sobre as razões do churn.

## Executando o Protótipo

1. Entre no diretório `/prototype`.
3. Execute o comando `python3 -m streamlit run churn-prototype.py --server.port 8502`.
4. O navegador padrão deverá abrir em seguida com o painel Streamlit executando no servidor local.

## Apresentação do projeto

Para entender melhor o projeto, leia a apresentação dos slides no diretório principal.

