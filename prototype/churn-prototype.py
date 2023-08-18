# %%
import streamlit as st
import pandas as pd
from frequent_topics import CommentsAnalyzer
from recommendation import Recommender

# %%
df = pd.read_csv("../data/churn_com_texto.csv",delimiter=",", quotechar='"', on_bad_lines="skip")

# %%
df['Número de Reclamações'] = pd.to_numeric(df['Número de Reclamações'], errors='coerce')
df = df.fillna(0)
df = df.replace('-','0')
df['Comentários'] = df['Comentários'].astype(str, errors='ignore')

# %%
recommender = Recommender(df)

# Filtre os dados usando a função de recomendação da classe acima
df = recommender.filter_complaints()

# %%
# Tela inicial
st.title("Análise de Propensão ao Churn")

# Seleção de Tipo de Serviço
service_type = st.selectbox("Escolha um Tipo de Serviço:", ["Todos", "Telefonia Móvel", "Telefonia Fixa", "Internet", "TV a Cabo"])
if service_type != "Todos":
    df = df[df['Tipo de Serviço'] == service_type]
    df = df[['Nome','Idade','Localização','Data de Início do Contrato','Valor Mensal do Contrato','Número de Reclamações','Comentários']]

# %%
# Visualização de Usuários Propensos ao Churn
st.subheader("Usuários Propensos ao Churn")
st.write(df)

# %%
# Analise os feedbacks usando a classe FeedbackAnalyzer
analyzer = CommentsAnalyzer(df['Comentários'])

# Visualização de Tópicos de Problemas
st.subheader("Tópicos de Problemas")
if service_type == "Todos":
    st.bar_chart(df['Tipo de Serviço'].value_counts())
else:
    keyword_frequencies = analyzer.get_keyword_frequencies(num_topics=5)
    st.bar_chart(pd.Series(keyword_frequencies))

# %%
# Recomendações de Ação
st.subheader("Recomendações de Ação")
text = recommender.generate_text(service_type)
st.write("Aqui podem ser listadas recomendações baseadas nos feedbacks dos usuários.")


