## CONVERSION DEL ARCHIVO
import pandas as pd 

def formatAge(x):
	return x[2:3]

def getRaza(x):
    if x == 'NOR': return 0
    elif x == 'HOL': return 1
    elif x == 'AYR': return 2
    elif x == 'JER': return 3

df = pd.read_excel('Neospora.xlsx')

df["EDAD"] = df["EDAD"].apply(formatAge)
df["RAZA"] = df["RAZA"].apply(getRaza)

for i in ['NEOSPORA','TORO','INSEMINACION','ABORTO','REPETICION','NO_CARGA','DISTOCIAS','TERNEROS_DEBILES','MUERTE_EMBRIONARIA']:
    df[i] = df[i].apply(lambda x: int (x))

df.to_csv('Neospora.csv', encoding='utf-8', index=False)
