import psycopg2
import logging




class Cliente:
  
    def __init__(self,):
        pass

    def __del__(self,):
        logging.warning("Encerar conexao com banco de dados...")
        self.cursor.close()


    def getConnection(self,):
        try:
            logging.warning("nova conexao")

            self.connection = psycopg2.connect(user = "admin",
                                        password = "password",
                                        host = "postgres",
                                        port = "5432",
                                        database = "data")

            self.cursor = self.connection.cursor()


        except(Exception, psycopg2.Error) as error :
            logging.warning("Erro ao conectar no banco")
            self.cursor = None

    def createTable(self,):

        query = '''CREATE TABLE clientes(
                id SERIAL PRIMARY KEY,
                cpf varchar(60),
                cpf_valido INT,
                private INT,
                incompleto INT,
                data_ultima_compra DATE null,
                ticket_medio FLOAT null,
                ticket_ultima_compra FLOAT null,
                loja_mais_frequente varchar(60) null,
                loja_da_ultima_compra varchar(60) null );'''

        conexao = self.cursor
        
        if conexao == None:
            logging.warning("Erro de conexao com o banco")
            return None

        try:
            conexao.execute(query)
            self.connection.commit()
            logging.info(">Table Clientes Criada")

        except Exception as e:
            logging.warning("Erro ao executar a query")
            logging.warning(e)
            return None

    
    def insertClientes(self, clientes):

        query = '''INSERT INTO clientes(
                            cpf, 
                            cpf_valido,
                            private,
                            incompleto,
                            data_ultima_compra,
                            ticket_medio,
                            ticket_ultima_compra,
                            loja_mais_frequente,
                            loja_da_ultima_compra
                        )
            VALUES '''
        
        for cliente in clientes:
            query = query + '''(
                \''''+ str(cliente['cpf']) +'''',
                  '''+ str(cliente['cpf_valido']) +''',
                  '''+ str(cliente['private']) +''',
                  '''+ str(cliente['incompleto']) +''',
                '''+ str(cliente['data_ultima_compra']) +''',
                '''+ str(cliente['ticket_medio']) +''',
                '''+ str(cliente['ticket_ultima_compra']) +''',
                \''''+ str(cliente['loja_mais_frequente']) +'''',
                \''''+ str(cliente['loja_da_ultima_compra']) +''''
            ),'''
        query = query[:-1] + ";"

        conexao = self.cursor
        
        if conexao == None:
            logging.warning("Erro de conexao com o banco")
            return None

        try:
            conexao.execute(query)
        except Exception as e:
            logging.warning("Erro ao executar a query")
            logging.warning(e)
            return None
    
    def find(self, id):
        conexao = self.cursor
        logging.warning("Bunscando id no banco ...")
        try:
            conexao.execute("SELECT * FROM clientes WHERE  id=%(id)s;", {'id': id })
            row = conexao.fetchall()
            logging.warning(row)
            row = row[0]
            cliente = {
                "id" : row[0],
                "cpf": row[1],
                "cpf_valido": row[2],
                "private": row[3],
                "incompleto": row[4],
                "data_ultima_compra": row[5],
                "ticket_medio" : row[6],
                "ticket_ultima_compra" : row[7],
                "loja_mais_frequente": row[8], 
                "loja_da_ultima_compra" : row[9]
            }
            return cliente
           
        except Exception as e:
            logging.warning("Erro ao executar a query")
            logging.warning(e)
            return None

    