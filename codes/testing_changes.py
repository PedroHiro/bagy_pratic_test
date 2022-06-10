
from operator import index
import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': [1,2,3,4,5], 
                    'Col2': [6,7,8,9,10],
                    'Col3': [11,-12,13,14,-15]})

print(df)

#df['Col3'] = df['Col3'].abs()

#indexes = df.loc[df[df['Col3']<0].index]
neg_values = df['Col3'] > 0 
df['Col3'].where(neg_values,-df['Col3'],inplace=True)

print(df)



















