import csv
import random
from faker import Faker
from datetime import datetime, timedelta

pais = "Índia"

# Inicializar o Faker e definir a semente para reprodutibilidade
fake = Faker()
Faker.seed(0)

# Função para gerar coordenadas aleatórias dentro dos limites de um país
def gerar_lat_long_pais(pais):
    """
        Gera coordenadas de latitude e longitude aleatórias dentro dos limites geográficos de um país específico.
        Adicionando mais uma linha sobre a documentação desta função

        Parâmetros:
            pais (str): Nome do país para o qual gerar as coordenadas.

        Retorna:
            tuple: Um par (latitude, longitude) com valores flutuantes representando as coordenadas geográficas.
    """
    if pais == 'Brasil':
        latitude = random.uniform(-33.0, 5.3)  # Limites de latitude do Brasil
        longitude = random.uniform(-74.0, -34.0)  # Limites de longitude do Brasil
    elif pais == 'EUA':
        latitude = random.uniform(24.396308, 49.384358)  # Limites de latitude dos EUA
        longitude = random.uniform(-125.0, -66.93457)  # Limites de longitude dos EUA
    elif pais == 'Índia':
        latitude = random.uniform(6.5, 35.5)  # Limites de latitude da Índia
        longitude = random.uniform(68.0, 97.0)  # Limites de longitude da Índia
    elif pais == 'Rússia':
        latitude = random.uniform(41.2, 81.86)  # Limites de latitude da Rússia
        longitude = random.uniform(19.6, 179.4)  # Limites de longitude da Rússia
    elif pais == 'Canadá':
        latitude = random.uniform(41.67, 83.11)  # Limites de latitude do Canadá
        longitude = random.uniform(-141.0, -52.6)  # Limites de longitude do Canadá
    return latitude, longitude

# Função para gerar altitude aleatória em metros (0 a 40.000 metros)
def gerar_altitude():
    """
    Gera um valor aleatório de altitude em metros, variando de 0 a 40.000 metros.

    Retorna:
        float: Um valor flutuante representando a altitude em metros.
    """
    return random.uniform(0, 40000)

# Nome do arquivo CSV de saída
nome_arquivo = 'dados_balao.csv'

# Tempo inicial: assume que o balão começa em um determinado momento
tempo_inicial = datetime.now()

# Definir a quantidade de dias e o intervalo entre os registros (1 minuto)
quantidade_dias = 30
intervalo_minutos = timedelta(minutes=1)

# Abrir o arquivo CSV e preparar para escrita
with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escrever o cabeçalho do CSV
    writer.writerow(['timestamp', 'latitude', 'longitude', 'altitude'])

    # Gerar os dados para cada minuto em 30 dias
    for i in range(quantidade_dias):  # 30 dias
        timestamp = tempo_inicial + i * intervalo_minutos
        latitude, longitude = gerar_lat_long_pais(pais)
        altitude = gerar_altitude()
        # Escrever os dados no arquivo CSV
        writer.writerow([timestamp.strftime('%Y-%m-%d %H:%M:%S'), latitude, longitude, altitude])

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
