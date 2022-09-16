import pandas as pd
import os

dfCara2020 = pd.read_csv('data/DataSource/caracteristiques-2020.csv', sep = ';')[['long','lat']].applymap(lambda x: str(x.replace(',','.'))).astype(float)
dfCara2019 = pd.read_csv('data/DataSource/caracteristiques-2019.csv', sep = ';')[['long','lat']].applymap(lambda x: str(x.replace(',','.'))).astype(float)
dfCara2018 = pd.read_csv('data/DataSource/caracteristiques-2018.csv', sep = ',', encoding="ISO-8859-1")[['long','lat']].astype(float)/100000
dfCara2017 = pd.read_csv('data/DataSource/caracteristiques-2017.csv', sep = ',', encoding="ISO-8859-1")[['long','lat']].astype(float)/100000
dfCara2016 = pd.read_csv('data/DataSource/caracteristiques-2016.csv', sep = ',', encoding="ISO-8859-1")[['long','lat']].astype(float)/100000

df = pd.concat([dfCara2020, dfCara2019, dfCara2018, dfCara2017, dfCara2016], axis = 0).dropna()
df = df[df['lat']!=0]

os.chdir("C:/Users/girar/Projet/Projet_Accident/data/map")
df.to_csv("Map.csv", index = False)

