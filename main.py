from service.inventory_service import InventoryService
import sqlite3
import interacao_excel
# Criando a conexão com a base de dados (na primeira interação a base de dados é criada através desse comando)
conn = sqlite3.connect('inventario.db')

# Criando o cursor que permitirá navegar e realizar operações com a base de dados
c = conn.cursor()

# Criando uma tabela na base de dados com as seguintes colunas:
"""
product_name -> text
brand -> text
category -> text
qtd -> integer
"""
c.execute("""CREATE TABLE inventory (   
            product__name text, 
            brand text, 
            category text, 
            qtd integer
        )
 """)

# Extraindo dados de uma planilha excel e organizando eles na forma dados = [(dado1), (dado2), ..., (dadon)]
products = interacao_excel.excel_data_extraction('Produtos.xlsx')

# Inserindo os dados obtidos da planilha excel na tabela de dados dentro da database
c.executemany("INSERT INTO inventory VALUES (?,?,?,?)", products)

# Visualizando os dados inseridos na tabela de dados dentro da database
service = InventoryService("inventario.db")

# Chama o método get_all para obter os registros
registros = service.get_all()
print(registros)
