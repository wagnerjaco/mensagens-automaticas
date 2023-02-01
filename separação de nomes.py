import pandas as pd

#contatos =pd.read_csv('contacts outlook.csv')
#print(contatos.head())
#contatos_coluna1 = contatos[["First Name"]]

#print(contatos_coluna1.head())
filepath = 'contacts google.csv'
df = pd.read_csv(filepath, sep=',')
print(df)
contatos_coluna1 = df[["Name"]]

print(contatos_coluna1)
contatos_coluna1cc = contatos_coluna1.dropna()
print(contatos_coluna1cc)