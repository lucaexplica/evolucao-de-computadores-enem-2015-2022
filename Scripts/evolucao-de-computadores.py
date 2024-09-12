#Vou instalar a biblioteca Python chamada openpyxl.
#Essa biblioteca é amplamente utilizada para trabalhar com arquivos do Excel no formato **".xlsx".

import openpyxl

#Vou instalar também a biblioteca Python chamada XlsxWriter. E essa biblioteca permite criar e manipular planilhas do Excel no formato ".xlsx".

#import XlsxWriter

#Vou intalar o Pandoc, ele é uma ferramenta de linha de comando que converte entre diferentes formatos de documentos, como Markdown, HTML, LaTeX e muitos outros.

#import Pandoc

#Vou importar a biblioteca Pandas e atribuir um apelido (alias) a ela, neste caso, vou usar "pd".

import pandas as pd

#Vou importar a biblioteca NumPy e atribuir a ela um apelido, neste caso, "np".

import numpy as np

#Vou importar a biblioteca Seaborn e atribuir a ela um apelido, que é "sns".

import seaborn as sns

#Vou importar a biblioteca Matplotlib e atribuir a ela um apelido, que é "plt".

import matplotlib.pyplot as plt

#Carregar os dados dos Nomes do Municipios por Região

regiao = pd.read_csv("RegiãoPorCodigoMunicipio.csv")

#Carregar os dados da Amazonia Legal
amazonia = pd.read_csv("CSV_Municipios_da_Amazonia_Legal_2022.csv")

#A seguir, vamos carregar os microdados do ENEM (arquivo grande, processamento leva tempo) - eventualmente pode ser necessário executar localmente. Você irá mudar o caminho conforme tiver salvo na sua maquina os arquivos

#2022
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2022 = pd.read_csv("2022_MICRODADOS_ENEM.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2022.head()

enem2022 = enem2022.dropna()

enem2022['Ano'] = 2022

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2022['Q024'] = enem2022['Q024'].replace(mapeamento)

enem2022.head()

tem_computador_2022 = enem2022['Q024'].sum()
tem_computador_2022

enem2022['CO_MUNICIPIO_ESC'] = enem2022['CO_MUNICIPIO_ESC'].astype(int)

enem2022_brasil = enem2022.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2022_brasil.head()

enem2022amazonia = enem2022.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2022amazonia = enem2022amazonia.dropna()

soma_computadores_regiao_brasil2022 = enem2022_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2022

soma_computadores_regiao_amazonia2022 = enem2022amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2022

#2021
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2021 = pd.read_csv("MICRODADOS_ENEM_2021.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2021.head()

enem2021 = enem2021.dropna()

enem2021['Ano'] = 2021

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2021['Q024'] = enem2022['Q024'].replace(mapeamento)

enem2021.head()

tem_computador_2021 = enem2021['Q024'].sum()
tem_computador_2021

enem2021['CO_MUNICIPIO_ESC'] = enem2021['CO_MUNICIPIO_ESC'].astype(int)

enem2021_brasil = enem2021.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2021_brasil.head()

enem2021amazonia = enem2021.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2021amazonia = enem2021amazonia.dropna()

soma_computadores_regiao_brasil2022 = enem2021_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2022

soma_computadores_regiao_amazonia2021 = enem2021amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2021

#2020
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2020 = pd.read_csv("MICRODADOS_ENEM_2020.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2020.head()

enem2020 = enem2020.dropna()

enem2020['Ano'] = 2020

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2020['Q024'] = enem2020['Q024'].replace(mapeamento)

enem2020.head()

tem_computador_2020 = enem2020['Q024'].sum()
tem_computador_2020

enem2020['CO_MUNICIPIO_ESC'] = enem2020['CO_MUNICIPIO_ESC'].astype(int)

enem2020_brasil = enem2020.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2020_brasil.head()

enem2020amazonia = enem2020.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2020amazonia = enem2020amazonia.dropna()

soma_computadores_regiao_brasil2020 = enem2020_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2020

soma_computadores_regiao_amazonia2020 = enem2020amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2020

#2019
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2019 = pd.read_csv("MICRODADOS_ENEM_2019.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2019.head()

enem2019 = enem2019.dropna()

enem2019['Ano'] = 2019

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2019['Q024'] = enem2019['Q024'].replace(mapeamento)

enem2019.head()

tem_computador_2019 = enem2019['Q024'].sum()
tem_computador_2019

enem2019['CO_MUNICIPIO_ESC'] = enem2019['CO_MUNICIPIO_ESC'].astype(int)

enem2019_brasil = enem2019.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2019_brasil.head()

enem2019amazonia = enem2019.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2019amazonia = enem2019amazonia.dropna()

soma_computadores_regiao_brasil2019 = enem2019_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2019

soma_computadores_regiao_amazonia2019 = enem2019amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2019

#2018
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2018 = pd.read_csv("MICRODADOS_ENEM_2018.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2018.head()

enem2018 = enem2018.dropna()

enem2018['Ano'] = 2018

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2018['Q024'] = enem2018['Q024'].replace(mapeamento)

enem2018.head()

tem_computador_2018 = enem2018['Q024'].sum()
tem_computador_2018

enem2018['CO_MUNICIPIO_ESC'] = enem2018['CO_MUNICIPIO_ESC'].astype(int)

enem2018_brasil = enem2018.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2018_brasil.head()

enem2018amazonia = enem2018.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2018amazonia = enem2018amazonia.dropna()

soma_computadores_regiao_brasil2018 = enem2018_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2018

soma_computadores_regiao_amazonia2018 = enem2018amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2018

#2017
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2017 = pd.read_csv("MICRODADOS_ENEM_2017.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2017.head()

enem2017 = enem2017.dropna()

enem2017['Ano'] = 2017

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2017['Q024'] = enem2017['Q024'].replace(mapeamento)

enem2017.head()

tem_computador_2017 = enem2017['Q024'].sum()
tem_computador_2017

enem2017['CO_MUNICIPIO_ESC'] = enem2017['CO_MUNICIPIO_ESC'].astype(int)

enem2017_brasil = enem2017.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2017_brasil.head()

enem2017amazonia = enem2017.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2017amazonia = enem2017amazonia.dropna()

soma_computadores_regiao_brasil2017 = enem2017_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2017

soma_computadores_regiao_amazonia2017 = enem2017amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2017

#2016
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2016 = pd.read_csv("MICRODADOS_ENEM_2016.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2016.head()

enem2016 = enem2016.dropna()

enem2016['Ano'] = 2016

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2016['Q024'] = enem2016['Q024'].replace(mapeamento)

enem2016.head()

tem_computador_2016 = enem2016['Q024'].sum()
tem_computador_2016

enem2016['CO_MUNICIPIO_ESC'] = enem2016['CO_MUNICIPIO_ESC'].astype(int)

enem2016_brasil = enem2016.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2016_brasil.head()

enem2016amazonia = enem2016.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2016amazonia = enem2016amazonia.dropna()

soma_computadores_regiao_brasil2016 = enem2016_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2016

soma_computadores_regiao_amazonia2016 = enem2016amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2016

#2015
#Q024 - Você tem Computador?
#A-não tem
#B-1
#C-2
#D-3
#E-4 ou mais

enem2015 = pd.read_csv("MICRODADOS_ENEM_2015.csv",sep=";",encoding="ISO-8859-1",usecols=['Q024','CO_MUNICIPIO_ESC'])
enem2015.head()

enem2015 = enem2015.dropna()

enem2015['Ano'] = 2015

mapeamento = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1}

enem2015['Q024'] = enem2015['Q024'].replace(mapeamento)

enem2015.head()

tem_computador_2015 = enem2015['Q024'].sum()
tem_computador_2015

enem2015['CO_MUNICIPIO_ESC'] = enem2015['CO_MUNICIPIO_ESC'].astype(int)

enem2015_brasil = enem2015.merge(regiao[['CO_MUNICIPIO_ESC','NM_REGIÃO']], on='CO_MUNICIPIO_ESC', how='left')

enem2015_brasil.head()

enem2015amazonia = enem2015.merge(amazonia[['CO_MUNICIPIO_ESC','NM_REGIAO']], on='CO_MUNICIPIO_ESC', how='left')

enem2015amazonia = enem2015amazonia.dropna()

soma_computadores_regiao_brasil2015 = enem2015_brasil.groupby('NM_REGIÃO')['Q024'].sum()
soma_computadores_regiao_brasil2015

soma_computadores_regiao_amazonia2015 = enem2015amazonia.groupby('NM_REGIAO')['Q024'].sum()
soma_computadores_regiao_amazonia2015

#Graficos de linha com base se tem acesso a internet e a computador no Brasil

enem_combinado_brasil = pd.concat([enem2022_brasil,enem2020_brasil,enem2019_brasil,enem2018_brasil,enem2017_brasil,enem2016_brasil,enem2015_brasil], ignore_index=True)

enem_combinado_brasil.dropna(inplace=True)

enem_combinado_brasil['Q024'] = enem_combinado_brasil['Q024'].astype(int)

enem_combinado_brasil.rename(columns={'NM_REGIÃO': 'REGIAO'}, inplace=True)

soma_computadores_por_regiao_brasil = enem_combinado_brasil.groupby(['Ano', 'REGIAO'])['Q024'].sum().reset_index()

for regiao in soma_computadores_por_regiao_brasil['REGIAO'].unique():
    dados_regiao = soma_computadores_por_regiao_brasil[soma_computadores_por_regiao_brasil['REGIAO'] == regiao]
    plt.plot(dados_regiao['Ano'], dados_regiao['Q024'], marker='o', label=regiao)

#Adicionando detalhes ao gráfico
plt.title('Evolução da Quantidade de Computadores por Região no Brasil')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Computadores')
plt.legend()
plt.grid(True)

#Mostrar o gráfico
plt.show()

#Graficos de linha com base se tem acesso a internet e a computador na Amazonia Legal
enem_combinado_amazonia = pd.concat([enem2022amazonia,enem2020amazonia,enem2019amazonia,enem2018amazonia,enem2017amazonia,enem2016amazonia,enem2015amazonia], ignore_index=True)
enem_combinado_amazonia

enem_combinado_amazonia.dropna(inplace=True)

enem_combinado_amazonia['Q024'] = enem_combinado_amazonia['Q024'].astype(int)

enem_combinado_amazonia

enem_combinado_amazonia = enem_combinado_amazonia.pivot(index='Ano', columns='NM_REGIAO', values='Q024')

soma_computadores_por_regiao_amazonia = enem_combinado_amazonia.groupby(['Ano', 'NM_REGIAO'])['Q024'].sum().reset_index()

for regiao in soma_computadores_por_regiao_amazonia['NM_REGIAO'].unique():
    dados_regiao = soma_computadores_por_regiao_amazonia[soma_computadores_por_regiao_amazonia['NM_REGIAO'] == regiao]
    plt.plot(dados_regiao['Ano'], dados_regiao['Q024'], marker='o', label=regiao)

#Adicionando detalhes ao gráfico
plt.title('Evolução da Quantidade de Computadores por Região na Amazônia')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Computadores')
plt.legend()
plt.grid(True)

#Mostrar o gráfico
plt.show()
