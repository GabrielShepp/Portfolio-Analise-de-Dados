import pandas as pd
import numpy as np

data = {
    'ID_Cliente': [1, 2, 3, 4, 5, 6],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Salvador', 'Rio de Janeiro', np.nan],
    'Valor_Compra': [125.50, 40.00, 210.90, 85.00, np.nan, 150.00],
    'Status_Assinatura': ['Ativo', 'Inativo', 'Ativo', 'Ativo', 'Inativo', 'Ativo']
}

df = pd.DataFrame(data)

print("DataFrame Original:")
print(df)
print("-" * 30)
#
#
# df['Cidade'].fillna('Cidade desconhecida', inplace=True)
# df['Valor_Compra'].fillna(0.0, inplace=True)
# print(df)
# Condtion_value = (df['Valor_Compra'] > 100)
# Condition_local = (df['Cidade'] == 'São Paulo')
# table_cont = df[Condtion_value & Condition_local]
# print(table_cont)
#
# df.insert(loc=len(df.columns), column='Lucro', value=(df['Valor_Compra']*1.25))
#
# lucro_medio = df.groupby('Cidade')['Lucro'].mean()
# print(lucro_medio)
# print(df)

vendas_data = {
    'ID_Cliente': [1, 2, 3, 7, 8],
    'Total_Gasto': [500, 30, 900, 100, 45],
    'Mes': ['Jan', 'Fev', 'Jan', 'Mar', 'Fev']
}
df_vendas = pd.DataFrame(vendas_data)

print("\nDataFrame de Vendas:")
print(df_vendas)

df_merge = df.merge(df_vendas, on='ID_Cliente', how='inner')
print(df_merge)