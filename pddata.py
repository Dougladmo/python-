import pandas as pd
import win32com.client as win32

# import data base

tab_sales = pd.read_excel('Vendas.xlsx')

# data base
pd.set_option('display.max_columns', None)

# billing per store
billing = tab_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(billing)
print("-" * 50)

# products per store

products_store = tab_sales[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(products_store)
print("-" * 50)

# product average price

tab = tab_sales[['ID Loja', 'Valor Final', 'Quantidade']].groupby('ID Loja').sum()
ticket = (tab['Valor Final'] / tab['Quantidade']).to_frame()
print(ticket)

# send email report
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'xplays.dm@gmail.com'
mail.Subject = 'sales and billing per store report'
mail.HTMLBody = '''

Prezados, 

segue o Relatório de vendas por cada Loja.

Faturamento:
{}

Quantidade Vendida:
{}

Ticket Médio:
{}



'''

mail.Send()
print("Email Enviado !!!")



