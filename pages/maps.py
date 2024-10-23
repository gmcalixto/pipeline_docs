import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap




# Função para carregar o CSV e mostrar o trajeto do balão em um mapa
def exibir_trajeto_mapa(data):

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

exibir_trajeto_mapa(st.session_state["dataset"])
mapa_calor(st.session_state["dataset"])