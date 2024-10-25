import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("./dados.csv")
# Definindo as variáveis independentes (X) e a variável dependente (y)
X = df.drop(columns=["Nav State", "Autonomia Barco"])
y = df["Autonomia Barco"]

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)
# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Exemplo de novos dados para previsão
novos_dados = pd.DataFrame({
    "Tensão Nominal (V)": [71.79],
    "Capacidade (Ah)": [207.48],
    "Energia das Baterias": [14.8949892],
    "Potência Flutuante (kW)": [1.5124240080842877],
    "Motores Ativos": [2],
    "Potência Total": [3.0248480161685753]
})

# Prevendo a autonomia
previsao_autonomia = model.predict(novos_dados)
print(f"Autonomia Prevista: {previsao_autonomia[0]:.2f} horas")
