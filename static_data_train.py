import numpy as np
import pandas as pd

registros = 10000                   # Quantidade de registros que desejo que meu csv tenha
ids = np.arange(1, registros + 1)    # IDs de cada registro

# Parâmetros da Bateria
tensao_nominal_media = 72.8         # Tensão nominal em volts
capacidade_media = 205               # Capacidade em Ah

# Variabilidade de 5% para tensão e capacidade
variacao_tensao = 0.05 * tensao_nominal_media
variacao_capacidade = 0.05 * capacidade_media

# Gera tensões nominais aleatórias em torno de 76.8 V com uma variação de ±5%
tensoes = np.random.uniform(
    tensao_nominal_media - variacao_tensao, 
    tensao_nominal_media + variacao_tensao, 
    registros
).round(2)

# Gera capacidades aleatórias em torno de 205 Ah com uma variação de ±5%
capacidades = np.random.uniform(
    capacidade_media - variacao_capacidade, 
    capacidade_media + variacao_capacidade, 
    registros
).round(2)

# Energia Total Atual Das Baterias
energia_total_atual_baterias = (tensoes * capacidades)/1000  # 

# Parâmetros do Motor
potencia_minima = 0.0  # Potência mínima em kW
potencia_maxima = 13.0  # Potência máxima em kW

# Gerando potências flutuantes aleatórias
potencias_flutuantes = np.random.uniform(potencia_minima, potencia_maxima, registros)
motores_ativos = np.random.randint(0, 3, registros)  # Segundo o Artigo, possui até 2 motores
potencia_total_atual = potencias_flutuantes * motores_ativos

# Relação entre a Energia fornecida das baterias e o Estado do motor atual (Autonomia)
# Substituir valores de potência total que são zero por um pequeno valor
potencia_total_atual = np.where(potencia_total_atual == 0, 0.1, potencia_total_atual)
autonomia = energia_total_atual_baterias / potencia_total_atual
autonomia_horas = np.round(autonomia,2)

# Cria um DataFrame com as informações
dados = pd.DataFrame({
    "Nav State": range(1, registros + 1),
    "Tensão Nominal (V)": tensoes,
    "Capacidade (Ah)": capacidades,
    "Energia das Baterias": energia_total_atual_baterias,  # Corrigido aqui
    "Potência Flutuante (kW)": potencias_flutuantes,
    "Motores Ativos": motores_ativos,
    "Potência Total": potencia_total_atual,
    "Autonomia Barco": autonomia_horas
})

# Salvar o DataFrame em um arquivo CSV
dados.to_csv("dados.csv", index=False, encoding="utf-8")
print(dados.head())
