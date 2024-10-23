import streamlit as st
import pandas as pd
import altair as alt

# Função para carregar o CSV e gerar o gráfico de dispersão usando Altair
def exibir_grafico_dispersao(data):
    """
    Exibe um gráfico de dispersão das coordenadas geográficas (latitude e longitude) 
    dos dados fornecidos usando Altair.

    Parâmetros:
        data (DataFrame): Um DataFrame do pandas que deve conter as colunas 'latitude' e 'longitude'.

    Retorna:
        None: Esta função não retorna nenhum valor, mas exibe um gráfico de dispersão no Streamlit.
    """

    # Verificar se as colunas de latitude e longitude estão presentes
    if 'latitude' in data.columns and 'longitude' in data.columns:

        # Gerar o gráfico de dispersão usando Altair
        st.subheader("Gráfico de Dispersão das Posições do Balão")
        
        scatter_plot = alt.Chart(data).mark_circle(size=60).encode(
            x=alt.X('longitude', title='Longitude'),
            y=alt.Y('latitude', title='Latitude'),
            tooltip=['latitude', 'longitude'],  # Tooltip com informações dos pontos
            color=alt.value('blue')  # Cor dos pontos
        ).properties(
            title='Dispersão das Posições do Balão',
            width=700,
            height=400
        ).interactive()  # Permitir zoom e pan no gráfico
        
        # Exibir o gráfico no Streamlit
        st.altair_chart(scatter_plot, use_container_width=True)
    else:
        st.error("As colunas 'latitude' e 'longitude' não foram encontradas no arquivo CSV.")

# Função para carregar o CSV e gerar o gráfico de altitude
def exibir_grafico_altitude(data):
    """
    Exibe um gráfico de linha mostrando a altitude ao longo do tempo, utilizando dados fornecidos.

    Parâmetros:
        data (DataFrame): Um DataFrame do pandas que deve conter as colunas 'timestamp' e 'altitude'.

    Retorna:
        None: Esta função não retorna nenhum valor, mas exibe um gráfico de linha no Streamlit.
    """

    # Converter a coluna 'timestamp' para o tipo datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Verificar se a coluna altitude está presente
    if 'altitude' in data.columns:
        # Gerar o gráfico de altitude ao longo do tempo
        st.subheader("Gráfico de Altura do Balão em Relação ao Tempo")
        st.line_chart(data[['timestamp', 'altitude']].set_index('timestamp'))
    else:
        st.error("A coluna 'altitude' não foi encontrada no arquivo CSV.")

# Função para carregar o CSV e gerar as métricas de altitude
def exibir_metricas_altitude(data):
    """
    Calcula e exibe métricas de altitude, incluindo a maior e a menor altitude registradas.

    Parâmetros:
        data (DataFrame): Um DataFrame do pandas que deve conter a coluna 'altitude'.

    Retorna:
        None: Esta função não retorna nenhum valor, mas exibe métricas de altitude no Streamlit.
    """
    # Converter a coluna 'timestamp' para o tipo datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Verificar se a coluna altitude está presente
    if 'altitude' in data.columns:
        # Calcular a maior e a menor altitude
        maior_altitude = data['altitude'].max()
        menor_altitude = data['altitude'].min()

        # Exibir métricas com st.metric
        st.subheader("Métricas de Altura do Balão")
        
        # Usando o layout de colunas para exibir as duas métricas lado a lado
        col1, col2 = st.columns(2)
        
        # Métrica da maior altitude
        col1.metric("Maior Altitude (m)", f"{maior_altitude:.2f}")

        # Métrica da menor altitude
        col2.metric("Menor Altitude (m)", f"{menor_altitude:.2f}")
    else:
        st.error("A coluna 'altitude' não foi encontrada no arquivo CSV.")


# Título do aplicativo
st.title("Gráficos")

if 'dataset' in st.session_state:

    exibir_grafico_dispersao(st.session_state['dataset'])
    exibir_grafico_altitude(st.session_state['dataset'])
    exibir_metricas_altitude(st.session_state['dataset'])

else:
    st.info("Por favor, faça o upload de um arquivo CSV para visualizar o mapa.")
