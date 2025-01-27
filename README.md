# Inventário de Produtos
Esse projeto realiza a importação de dados de uma planilha do Excel para uma tabela de dados criada dentro de uma database.

# Funcionamento do Código
Main:
- Cria uma conexão com a base de dados inventario;
- Cria um cursor para navegar pela base de dados criada;
- Cria uma tabela dentro da base de dados, inserindo as colunas dos dados a serem importados;
- Utiliza a função excel_data_extraction do arquivo interacao_excel para extrair os dados da planilha Excel;
- Insere os valores extraídos na planilha dentro da base de dados;
- Visualiza os dados inseridos utilizando o método get_all do service.

Interação_Excel:
- Utiliza a biblioteca pandas para realizar a leitura dos dados de um arquivo .xlsx do Excel;
- Os dados lidos são disponibilizados na forma de um dicionário
- Os dados do dicionário são iterados e o seu formato é ajustado para uma lista contendo várias tuplas correspondentes à cada produto cadastrado no inventário com as suas características;
- Esses dados tratados e no formato correto são retornados.

Inventory_Service:
- Uma classe é instanciada. O nome da classe é InventoryService;
- Um dos métodos dessa classe é o getall(self). Esse método seleciona e mostra todos os dados de uma tabela de dados utilizando comandos SQLite;
- Os dados inseridos na tabela da base de dados criada para o projeto são mostrados no terminal através desse método.
