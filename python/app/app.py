import pandas as pd
import time
import Cliente
import re
from flask import Flask
import logging
from flask import jsonify
from validate_docbr import CPF

# a pausa é feita para que de tempo do postgres no docker subir
logging.warning("Esperando o banco de dados iniciar ...")
time.sleep(10)


# assim que a classe Cleinte é instanciada conecta com o banco
logging.warning("Connectando com o banco ...")
clienteModel = Cliente.Cliente()


#o metodo createTable funciona como o migrate de banco
logging.warning("Criando tabelas ...")
clienteModel.createTable()


# Todos os parametros usados para a leitura do CSV são pasados 
# para o Lib do Pandas
logging.warning("lendo file.csv ...")
df = pd.read_csv('file.csv', sep='\t', error_bad_lines=False)


#Aqui os dados são processados (retirado caracters e convertido valores)
logging.warning("Processando dados ...")
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
    cliente['private']              = client_array[1] if client_array[1] != "NULL" else 0
    cliente['incompleto']           = client_array[2] if client_array[2] != "NULL" else 0
    cliente['data_ultima_compra']   = "'"+client_array[3]+"'" if client_array[3] != "NULL" else "NULL"
    cliente['ticket_medio']         = client_array[4] if client_array[4] != "NULL" else '0'
    cliente['ticket_ultima_compra'] = client_array[5] if client_array[5] != "NULL" else '0' 
    cliente['loja_mais_frequente']  = re.sub('[^0-9]', '', client_array[6])
    cliente['loja_da_ultima_compra']= re.sub('[^0-9]', '', client_array[7])

    cliente['ticket_medio'] = float(cliente['ticket_medio'].replace(',','.') )
    cliente['ticket_ultima_compra'] = float(cliente['ticket_ultima_compra'].replace(',','.') )

    matrix_clientes.append(cliente)
    

# Os dados são salvos no banco usando a mesma conexao ja criada anteriormente
logging.warning("Salvando dados no banco ...")
clienteModel.insertClientes(matrix_clientes)


#sobe um servidor usando o framework flask, expondo 2 rotas
logging.warning("Iniciando servidor web...")
app = Flask(__name__)

@app.route('/')
def home():
    return 'http://127.0.0.1:82/cliente/1'

@app.route('/cliente/<id>')
def getCliente(id):
    logging.warning(">>>>>")
    cli = clienteModel.find(id)
    logging.warning(cli)
    return jsonify(cli)