#热爱学习的CXQ

import pandas as pd

df = pd.DataFrame(pd.read_csv('1.csv',header=0))

print(df)

df=df.drop('1',axis=1)

df['6']=df['2']+df['3']

print('newdf\n',df)