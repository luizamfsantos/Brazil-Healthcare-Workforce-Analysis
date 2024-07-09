# %% [markdown]
# # import libraries

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# # load data

# %%
density = pd.read_csv('../../../Dados/Processado/Equipes_Saude/densidade/densidade10000habitantes.csv')

# %%
density.head()

# %%
density.set_index("Unidade da Federacao", inplace=True)
density.columns = pd.to_datetime(density.columns)

# %% [markdown]
# # visualizations

# %%
# Transpose the DataFrame to have states as columns and dates as rows
density_transposed = density.transpose()

# Plot settings
plt.figure(figsize=(18, 6))  # Set the figure size

# Loop through each state and plot its time series data
for state in density_transposed.columns:
    dates = density_transposed.index
    values = density_transposed[state]
    
    # Plot the time series data
    plt.plot(dates, values, label=state)

# Add labels and title
plt.xlabel('Ano')
plt.ylabel('Equipes de Saude por 10.000 habitantes')
plt.title('Numero de Equipes de Saude por 10.000 habitantes')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend to distinguish between states
plt.legend(loc='upper left', ncol=3)  # Adjust the position and columns as needed

# Show the plot
plt.tight_layout()
plt.show()


# %%
density.index

# %%
def plot_regiao(regiao_transposed,regiao):
    plt.figure(figsize=(18, 6))  # Set the figure size

    # Loop through each state and plot its time series data
    for state in regiao_transposed.columns:
        dates = regiao_transposed.index
        values = regiao_transposed[state]
        
        # Plot the time series data
        plt.plot(dates, values, label=state)

    # Add labels and title
    plt.xlabel('Ano')
    plt.ylabel('Equipes de Saude por 10.000 habitantes')
    plt.title(f'Numero de Equipes de Saude por 10.000 habitantes \n {regiao}')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add legend to distinguish between states
    plt.legend(loc='upper left')  # Adjust the position and columns as needed

    # Show the plot
    plt.tight_layout()
    plt.show()


# %%
# regiao norte
regiao_norte_estados = ['11 Rondonia', '12 Acre', '13 Amazonas', '14 Roraima', '15 Para',
       '16 Amapa', '17 Tocantins']
regiao_norte_density = density.loc[regiao_norte_estados]
regiao_norte_density_transposed = regiao_norte_density.transpose()
plot_regiao(regiao_norte_density_transposed,"Norte")

# %%
# regiao nordeste
regiao_nordeste_estados = ['21 Maranhao', '22 Piaui', '23 Ceara', '24 Rio Grande do Norte',
       '25 Paraiba', '26 Pernambuco', '27 Alagoas', '28 Sergipe', '29 Bahia']
regiao_nordeste_density = density.loc[regiao_nordeste_estados]
regiao_nordeste_density_transposed = regiao_nordeste_density.transpose()
plot_regiao(regiao_nordeste_density_transposed,"Nordeste")

# %%
# regiao sudeste
regiao_sudeste_estados = ['31 Minas Gerais', '32 Espirito Santo', '33 Rio de Janeiro',
       '35 Sao Paulo']
regiao_sudeste_density = density.loc[regiao_sudeste_estados]
regiao_sudeste_density_transposed = regiao_sudeste_density.transpose()
plot_regiao(regiao_sudeste_density_transposed,"Sudeste")

# %%
# regiao sul
regiao_sul_estados = ['41 Parana', '42 Santa Catarina', '43 Rio Grande do Sul']
regiao_sul_density = density.loc[regiao_sul_estados]
regiao_sul_density_transposed = regiao_sul_density.transpose()
plot_regiao(regiao_sul_density_transposed,"Sul")

# %%
# regiao centro-oeste
regiao_centro_oeste_estados = ['50 Mato Grosso do Sul', '51 Mato Grosso', '52 Goias','53 Distrito Federal']
regiao_centro_oeste_density = density.loc[regiao_centro_oeste_estados]
regiao_centro_oeste_density_transposed = regiao_centro_oeste_density.transpose()
plot_regiao(regiao_centro_oeste_density_transposed,"Centro-Oeste")


