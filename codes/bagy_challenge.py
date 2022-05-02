
# Testando o carregamento do csv

import pandas as pd

df = pd.read_csv('../bases/teste_dados_ecommerce.csv', encoding='unicode_escape',sep=';')

print(df)












