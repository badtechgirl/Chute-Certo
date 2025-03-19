import pandas as pd

# Tentar carregar o arquivo CSV, tratando erros caso não exista
try:
    df = pd.read_csv('vendas_de_ingressos.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'vendas_de_ingressos.csv' não foi encontrado.")
    df = pd.DataFrame()  # Criar um DataFrame vazio para evitar erros

# 1. Exibir a quantidade de linhas e colunas do data frame.
print("\nQuantidade de linhas e colunas:")
print(df.shape)

# 2. Exibir as 7 primeiras linhas do data frame (se houver dados).
if not df.empty:
    print("\nPrimeiras 7 linhas:")
    print(df.head(7))
else:
    print("\nO DataFrame está vazio.")

# 3. Exibir as 10 últimas linhas do data frame.
if not df.empty:
    print("\nÚltimas 10 linhas:")
    print(df.tail(10))

# 4. Renomear as colunas de forma permanente:
if not df.empty:
    df = df.rename(columns={
        'Age': 'Idade',
        'Ticket_Price': 'Preco_do_Ingresso',
        'Movie_Genre': 'Genero',
        'Seat_Type': 'Tipo_de_Assento',
        'Number_of_Person': 'Numero_de_Pessoas',
        'Purchase_Again': 'Compraria_Novamente'
    })

# 5. Resumo estatístico dos dados numéricos.
if not df.empty:
    print("\nResumo estatístico:")
    print(df.describe())

# 6. Filtrar os dados por gênero (exemplo: Action).
if not df.empty:
    print("\nDados filtrados por gênero (exemplo: Action):")
    print(df[df['Genero'] == 'Action'])

# 7. Exibir os dados das linhas 12 a 20 (inclusive).
if not df.empty:
    print("\nDados das linhas 12 a 20:")
    print(df.iloc[11:21])

# 8. Exibir os dados das linhas 35, 38, 42 e 50.
if not df.empty:
    print("\nDados das linhas 35, 38, 42 e 50:")
    print(df.iloc[[34, 37, 41, 49]])

# 9. Exibir os dados em que o tipo de assento é Standard.
if not df.empty:
    print("\nDados com tipo de assento Standard:")
    print(df[df['Tipo_de_Assento'] == 'Standard'])

# 10. Exibir os dados em que as idades dos consumidores estão entre 20 e 45 anos.
if not df.empty:
    print("\nDados com idade entre 20 e 45 anos:")
    print(df[(df['Idade'] >= 20) & (df['Idade'] <= 45)])

# 11. Criar um novo DataFrame em que o gênero dos filmes assistidos é Comedy.
if not df.empty:
    df_comedy = df[df['Genero'] == 'Comedy']
    print("\nNovo DataFrame com gênero Comedy:")
    print(df_comedy)

# 12. Criar um novo DataFrame exibindo os registros de Preço do Ingresso, Gênero e Tipo de Assento nos clientes que comprariam novamente.
if not df.empty:
    df_compraria_novamente = df[df['Compraria_Novamente'] == 'Yes'][['Preco_do_Ingresso', 'Genero', 'Tipo_de_Assento']]
    print("\nDataFrame com Preço do Ingresso, Gênero e Tipo de Assento para clientes que comprariam novamente:")
    print(df_compraria_novamente)

# 13. Criar uma nova Series filtrando os dados pelo Tipo de Assento.
if not df.empty:
    series_tipo_assento = df['Tipo_de_Assento']
    print("\nNova Series com Tipo de Assento:")
    print(series_tipo_assento)

# 14. Exibir os dados antes de excluir a coluna Ticket_ID
if not df.empty:
    print("\nDataFrame antes de excluir a coluna 'Ticket_ID':")
    print(df.head())

# 15. Excluir a coluna Ticket_ID de forma permanente.
if not df.empty and 'Ticket_ID' in df.columns:
    df = df.drop('Ticket_ID', axis=1)

# 16. Verificar a quantidade de valores nulos no dataset.
if not df.empty:
    print("\nQuantidade de valores nulos:")
    print(df.isnull().sum())

# 17. Verificar a quantidade de valores NaN no dataset.
if not df.empty:
    print("\nQuantidade de valores NaN:")
    print(df.isna().sum())

# 18. Utilizar o método iloc para exibir as linhas 15 a 20 e as colunas Idade, Preço_do_Ingresso e Gênero.
if not df.empty:
    print("\nLinhas 15 a 20, colunas Idade, Preço_do_Ingresso e Gênero:")
    print(df.iloc[14:20, df.columns.get_indexer(['Idade', 'Preco_do_Ingresso', 'Genero'])])

# 19. Utilizar o método iloc para exibir as linhas 3, 8, 10 e 13 e as colunas Gênero e Número de Pessoas.
if not df.empty:
    print("\nLinhas 3, 8, 10 e 13, colunas Gênero e Número de Pessoas:")
    print(df.iloc[[2, 7, 9, 12], df.columns.get_indexer(['Genero', 'Numero_de_Pessoas'])])