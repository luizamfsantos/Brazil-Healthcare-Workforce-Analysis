# %% [markdown]
# # import libraries

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# # equipes de saude totais data

# %%
df = pd.read_csv('../../../Dados/Raw/Equipes_Saude/totais/2008-2022.csv', delimiter=';', encoding='utf-8')


# %%
df.head()

# %% [markdown]
# ### replace column names

# %%
df.columns

# %%
months = {"/Jan":"-01-01", "/Fev":"-02-01", "/Mar":"-03-01", "/Abr":"-04-01", "/Mai":"-05-01", "/Jun":"-06-01", "/Jul":"-07-01", "/Ago":"-08-01", "/Set":"-09-01", "/Out":"-10-01", "/Nov":"-11-01", "/Dez":"-12-01"}
for key, value in months.items():
    df.columns = df.columns.str.replace(key, value)

# %%
df.columns

# %%
df.set_index("Unidade da Federacao", inplace=True)

# %%
df.columns

# %%
df.head()

# %%
df.columns = pd.to_datetime(df.columns)
df.columns

# %% [markdown]
# ### check for NAs

# %%
df.isna().sum().sum()

# %% [markdown]
# ### save data

# %%
# save data in a new csv file
df.to_csv('../../../Dados/Processado/Equipes_Saude/totais/2008-2022.csv', index=True)

# %% [markdown]
# # population data

# %% [markdown]
# #### load data

# %%
pop = pd.read_csv('../../../Dados/Raw/Populacao/pop_2000_2021.csv', delimiter=';')

# %%
pop.head()

# %% [markdown]
# ### linear smoothing to create monthly data

# %%
pop.set_index("Unidade da Federacao", inplace=True)

# %%
pop.head()

# %%
# create a copy of pop
pop1 = pop.copy()

# %% [markdown]
# ### change column type

# %%
columns = np.arange(2000, 2022, 1)

# %%
pop1.columns = columns

# %%
pop1.columns

# %%
# create monthly data
for year in range(2000, 2021):
    for month in range(1, 13):
        monthly_increment = ((pop1[year+1] - pop1[year]) / 12).round(0)
        pop1[f'{year}-{month}-01'] = pop1[year] + (monthly_increment * month)

pop1.head()
        

# %%
# drop original columns
pop1.drop(columns=columns, inplace=True)
pop1.head()

# %% [markdown]
# ### save data

# %%
# pop1.to_csv('../../../Dados/Processado/Populacao/pop_2000_2020_mensal.csv', index=True)

# %% [markdown]
# # density of health professionals

# %% [markdown]
# #### load data

# %%
pop = pd.read_csv('../../../Dados/Processado/Populacao/pop_2000_2020_mensal.csv', delimiter=',')
equipe = pd.read_csv('../../../Dados/Processado/Equipes_Saude/totais/2008-2022.csv', delimiter=',')

# %%
pop.head()

# %%
equipe.head()

# %% [markdown]
# #### set column index

# %%
pop.set_index("Unidade da Federacao", inplace=True)
equipe.set_index("Unidade da Federacao", inplace=True)

# %% [markdown]
# #### change column name dtype

# %%
equipe.columns = pd.to_datetime(equipe.columns)

# %%
pop.columns = pd.to_datetime(pop.columns)

# %% [markdown]
# #### new df with intersection

# %%
# create a new dataframe with the time frame that both dataframes intersect that contains both dataframes
equipe_subset = equipe.loc[:, equipe.columns.isin(pop.columns)]
pop_subset = pop.loc[:, pop.columns.isin(equipe.columns)]

# %% [markdown]
# ##### check sizes match

# %%
equipe_subset.shape

# %%
pop_subset.shape

# %% [markdown]
# ##### divide number of equipes per population

# %%
pop_subset /= 10000
pop_subset.head()

# %%
density = equipe_subset.div(pop_subset)
density.head()

# %% [markdown]
# ### save data

# %%
# density.to_csv('../../../Dados/Processado/Equipes_Saude/densidade/densidade10000habitantes.csv', index=True)

# %% [markdown]
# # tipos de equipe

# %% [markdown]
# #### load data

# %%
# file paths of type  ../../../Dados/Raw/Equipes_Saude/separados_por_tipo_equipe/2008-12.csv
# delimeter ';'
# encoding 'utf-8'
# loop through all files and concatenate them into a single dataframe

# %%
# add path
import os, sys
currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# %%
path_2008_01 = '../../../Dados/Raw/Equipes_Saude/separados_por_tipo_equipe/2008/2008-01.csv'
df_2008_01 = pd.read_csv(path_2008_01, delimiter=';', encoding='utf-8')

# %%
path_tipos_totais = '../../../Dados/Raw/Equipes_Saude/totais/2007-2023_tipos_equipe.csv'
df_tipos_totais = pd.read_csv(path_tipos_totais, delimiter=';', encoding='utf-8')

# %%
tipos_equipe = df_tipos_totais.iloc[:,0].copy()

# %%
tipos_equipe.values

# %% [markdown]
# #### NAs

# %%
# fillna 0
df_tipos_totais.fillna(0, inplace=True)

# %%
# replace - with 0
df_tipos_totais.replace('-', 0, inplace=True)

# %% [markdown]
# #### change column types

# %%
# plot df_tipos_totais
df_tipos_totais.set_index('Tipo da Equipe', inplace=True)
df_tipos_totais.columns

# %%
months = {"/Jan":"-01-01", "/Fev":"-02-01", "/Mar":"-03-01", "/Abr":"-04-01", "/Mai":"-05-01", "/Jun":"-06-01", "/Jul":"-07-01", "/Ago":"-08-01", "/Set":"-09-01", "/Out":"-10-01", "/Nov":"-11-01", "/Dez":"-12-01"}
for key, value in months.items():
    df_tipos_totais.columns = df_tipos_totais.columns.str.replace(key, value)

# %%
df_tipos_totais.columns = pd.to_datetime(df_tipos_totais.columns)

# %% [markdown]
# #### save data

# %%
df_tipos_totais.to_csv('../../../Dados/Processado/Equipes_Saude/totais/2007-2023_tipos_equipe.csv', index=True)

# %%



