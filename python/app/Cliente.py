import psycopg2


class Cliente:
  
    def __init__(self,):
        pass

    def __del__(self,):
        print("Encerar conexao")
        self.cursor.close()


    def getConnection(self,):
        try:
            self.connection = psycopg2.connect(user = "admin",
                                        password = "password",
                                        host = "postgres",
                                        port = "5432",
                                        database = "data")

            self.cursor = self.connection.cursor()

            return self.cursor
            #cursor.execute("SELECT version();")
            #record = cursor.fetchone()

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        return None

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

        conexao = self.getConnection()
        
        if conexao == None:
            print("Erro na conexao")
            return None

        try:
            conexao.execute(query)
            self.connection.commit()
            print("Table Clientes Criada")

        except Exception as e:
            print(e)
            print("Erro na conexao")
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
                \''''+ str(cliente['data_ultima_compra']) +'''',
                \''''+ str(cliente['ticket_medio']) +'''',
                \''''+ str(cliente['ticket_ultima_compra']) +'''',
                \''''+ str(cliente['loja_mais_frequente']) +'''',
                \''''+ str(cliente['loja_da_ultima_compra']) +''''
            ),'''
        query = query[:-1] + ";"

        conexao = self.getConnection()
        if conexao == None:
            print("Erro na conexao")
            return None

        try:
            conexao.execute(query)
        except Exception as e:
            print(e)
            print("Erro na conexao")
            return None
    
    def selectClientes(self, clientes):
        query = '''SELECT * FROM clientes WHERE false;'''
       
        conexao = self.getConnection()

        if conexao == None:
            print("Erro na conexao")
            return None

        try:
            conexao.execute(query)
            rows = conexao.fetchall()
            print("The number of parts: ", conexao.rowcount)
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
            print("Erro na conexao")
            return None

    