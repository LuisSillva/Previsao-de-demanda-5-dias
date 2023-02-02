import pandas as pd
import numpy as np

series = pd.read_excel('Dados.xlsx')

series = series[['Data', 'Vendas']]
series['Data'] = pd.to_datetime(series['Data'])
data = series['Data']
vendas = series['Vendas']

sabados = []
domingos = []
segundas = []
tercas = []
quartas = []
for i in range(len(data)):
    if data[i].day_name() == 'Saturday':
        sabados.append(vendas[i])
    elif data[i].day_name() == 'Sunday':
        domingos.append(vendas[i])
    elif data[i].day_name() == 'Monday':
        segundas.append(vendas[i])
    elif data[i].day_name() == 'Tuesday':
        tercas.append(vendas[i])
    elif data[i].day_name() == 'Wednesday':
        quartas.append(vendas[i])

media_sabados = np.mean(sabados)
media_domingos = np.mean(domingos)
media_segundas = np.mean(segundas)
media_tercas = np.mean(tercas)
media_quartas = np.mean(quartas)

print("A média de vendas do dia 21/01/2023 é: ", media_sabados)
print("A média de vendas dos 22/01/2023 é: ", media_domingos)
print("A média de vendas das 23/01/2023 é: ", media_segundas)
print("A média de vendas das 24/01/2023 é: ", media_tercas)
print("A média de vendas das 25/01/2023 é: ", media_quartas)