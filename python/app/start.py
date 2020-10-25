import pandas as pd
import time
import Cliente
import re
import flask
from validate_docbr import CPF
cpf = CPF()

print("Esperando o banco de dados iniciar ...")
time.sleep(10)

clienteModel = Cliente.Cliente()

clienteModel.createTable()

print("Processar file.csv ...")

df = pd.read_csv('file.csv', sep='\t', error_bad_lines=False)

lista = df.values

matrix_clientes = []
for row in lista:
    cpf = CPF()

    client_array = row[0].split()
    cliente = {}

    if cpf.validate(client_array[0]):
        cpf_valido = 1
    else:
        cpf_valido = 0
        
    cliente['cpf']                  = re.sub('[^0-9]', '', client_array[0])
    cliente['cpf_valido']           = cpf_valido
    cliente['private']              = client_array[1] 
    cliente['incompleto']           = client_array[2] if client_array[5] != "NULL" else 0
    cliente['data_ultima_compra']   = client_array[3] if client_array[5] != "NULL" else ''
    cliente['ticket_medio']         = client_array[4] if client_array[5] != "NULL" else ''
    cliente['ticket_ultima_compra'] = client_array[5] if client_array[5] != "NULL" else ''
    cliente['loja_mais_frequente']  = re.sub('[^0-9]', '', client_array[6])
    cliente['loja_da_ultima_compra']= re.sub('[^0-9]', '', client_array[7])

    matrix_clientes.append(cliente)
    

clienteModel.insertClientes(matrix_clientes)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()  # run our Flask app
