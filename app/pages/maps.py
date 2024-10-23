import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap




# Função para carregar o CSV e mostrar o trajeto do balão em um mapa
def exibir_trajeto_mapa(data):
    """
    Exibe um mapa interativo mostrando o trajeto do balão com base nas coordenadas de latitude e longitude fornecidas.

    Parâmetros:
        data (DataFrame): Um DataFrame do pandas que deve conter as colunas 'latitude' e 'longitude'.

    Retorna:
        None: Esta função não retorna nenhum valor, mas exibe um mapa interativo no Streamlit.
    
    Erros:
        Se 'latitude' ou 'longitude' não estiverem presentes, uma mensagem de erro será exibida.
    """
    # Verificar se as colunas de latitude e longitude estão presentes
    if 'latitude' in data.columns and 'longitude' in data.columns:
 
        # Criar o mapa centrado no primeiro ponto de latitude e longitude
        mapa = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=4)

        # Adicionar o trajeto do balão como uma linha no mapa
        pontos_trajeto = list(zip(data['latitude'], data['longitude']))
        folium.PolyLine(pontos_trajeto, color="blue", weight=2.5, opacity=1).add_to(mapa)

        # Exibir o mapa no Streamlit
        st.subheader("Mapa do Trajeto do Balão")
        st_folium(mapa, width=700, height=500)
    else:
        st.error("As colunas 'latitude' e 'longitude' não foram encontradas no arquivo CSV.")


def mapa_calor(data):
    """
    Exibe um mapa de calor interativo baseado nas coordenadas de latitude e longitude fornecidas.

    Parâmetros:
        data (DataFrame): Um DataFrame do pandas que deve conter pelo menos as colunas 'latitude' e 'longitude'.

    Retorna:
        None: Esta função não retorna nenhum valor, mas exibe um mapa de calor no Streamlit.

    Descrição:
        O mapa de calor é gerado usando a biblioteca Folium e é exibido no Streamlit. A intensidade das cores no mapa de calor representa a concentração de pontos.
    """
    st.subheader("Mapa de Calor")

    # Converter o DataFrame em uma lista de pares de coordenadas
    locations = data[['latitude', 'longitude']].values.tolist()

    # Criar o mapa centrado nas coordenadas médias dos dados
    mapa = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=2)

    # Adicionar o HeatMap ao mapa
    HeatMap(locations).add_to(mapa)

    # Exibir o mapa interativo no Streamlit
    st_folium(mapa, width=700, height=500)




# Título do aplicativo
st.title("Mapas")

if 'dataset' in st.session_state:

    exibir_trajeto_mapa(st.session_state["dataset"])
    mapa_calor(st.session_state["dataset"])

else:
    st.info("Por favor, faça o upload de um arquivo CSV para visualizar o mapa.")