import pandas as pd

df = pd.read_csv('abalone.csv')

df['Sex'] = df['Sex'].replace('f','F')

df = df[df['Height'] < 0.3]
df = df[df['Height'] > 0]
df = df[df['Whole weight'] < 2.216]
df = df[df['Shucked weight'] < 0.97075]
df = df[df['Viscera weight'] < 0.48075]
df = df[df['Shell weight'] < 0.6065]
df.fillna(0.42,inplace=True)

df.to_csv('abalone_clear.csv')