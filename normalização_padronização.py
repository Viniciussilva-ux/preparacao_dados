import pandas as pd
from sklearn.preprocessing import RobustScaler , MinMaxScaler , StandardScaler


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização = RobustScaler
scaler = RobustScaler
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler (de 0 a 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['idadeMinMaxScaler'].maen(), df['salarioMinMaxScaler'].std()))

print('\n MinMaxScaler (de -1 a 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\n StandardScaler (Ajuste a média de 0 a desvio padrão de 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].mean(), df['idadeStandardScaler'].std()))
print('Salario - Min: {:.4f} Max: {:.4f} Mean: {:.18} Std: {:.4f}'.format(df['salarioStandardScaler'].min(), df['salarioStandardScaler'].max(), df['salarioStandardScaler'].mean(), df['idadeStandardScaler'].std()))

print('\n RobustScaler (Ajuste a mediana e IQR):')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df["idadeRobustScaler"].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))
print('Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].mean(), df['salarioRobustScaler'].std()))




