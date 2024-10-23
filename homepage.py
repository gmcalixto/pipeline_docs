import streamlit as st
import pandas as pd


# Título do aplicativo
st.title("Visualização de Dados do Balão")

# Instrução para upload do arquivo CSV
uploaded_file = st.file_uploader("Faça o upload do arquivo CSV contendo os dados de latitude e longitude", type=["csv"])

if uploaded_file is not None:
    # Carregar os dados CSV
    st.session_state['dataset'] = pd.read_csv(uploaded_file)
    
    data = st.session_state['dataset']

else:
    st.info("Por favor, faça o upload de um arquivo CSV para visualizar o mapa.")
