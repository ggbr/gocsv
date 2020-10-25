package model

import (
    "strconv"
    "github.com/klassmann/cpfcnpj"
    "github.com/ggbr/gocsv/database"
    "fmt"
    "strings"
    "database/sql"
  _ "github.com/lib/pq"

)

const (
    host     = "postgres"
    port     = 5432
    user     = "admin"
    password = "password"
    dbname   = "data"
  )
  

type Cliente struct {
    ID   int
    CPF   string
    CPF_VALIDO int
	PRIVATE   int
	INCOMPLETO   int
	DATA_ULTIMA_COMPRA   string
	TICKET_MEDIO   string
	TICKET_ULTIMA_COMPRA   string
	LOJA_MAIS_FREQUENTE   string
	LOJA_DA_ULTIMA_COMPRA   string
}

var clientes []Cliente

func ClienteNew(
                cpf string,
                private int,
                imcompleto int,
                data_ultima_compra string,
                ticket_medio string,
                ticket_ultima_compra string,
                loja_mais_frequente string,
                loja_da_ultima_compra string){
                 
    var cliente Cliente
    var cpfValido int

    cpf = cpfcnpj.Clean(cpf)

    isValidCpf := cpfcnpj.ValidateCPF(cpf)

    if isValidCpf {
        cpfValido = 1
    }else{
        cpfValido = 0
    }

    if(ticket_medio == "NULL"){
        ticket_medio = "0"
    }
    if(ticket_ultima_compra == "NULL"){
        ticket_ultima_compra = "0"
    }

    if(loja_mais_frequente == "NULL"){
        loja_mais_frequente = ""
    }
    

    if(loja_da_ultima_compra == "NULL"){
        loja_da_ultima_compra = ""
    }
    
	cliente.CPF   				    = cpf
	cliente.CPF_VALIDO   			= cpfValido
	cliente.PRIVATE   			    = private
	cliente.INCOMPLETO   		    = imcompleto
	cliente.DATA_ULTIMA_COMPRA      = data_ultima_compra
	cliente.TICKET_MEDIO   		    = strings.Replace(ticket_medio,",",".",1)
	cliente.TICKET_ULTIMA_COMPRA    = strings.Replace(ticket_ultima_compra,",",".",1)
	cliente.LOJA_MAIS_FREQUENTE     = cpfcnpj.Clean(loja_mais_frequente)
	cliente.LOJA_DA_ULTIMA_COMPRA   = cpfcnpj.Clean(loja_da_ultima_compra)
    
	clientes = append(clientes, cliente)
    
}

func GetClientes() []Cliente{
    return clientes
}

func InsertClients(){
    var row string

    sqlStatement := `
        INSERT INTO clientes (
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
        VALUES `
    
        
        for _, cliente := range clientes {

                date_ultima_compra :=  `'`+ cliente.DATA_ULTIMA_COMPRA +`'`

                if(cliente.DATA_ULTIMA_COMPRA == "NULL"){
                    date_ultima_compra =  `NULL`
                }

                row = `('` + cliente.CPF + `',
                 `+ strconv.Itoa(cliente.CPF_VALIDO) +`,
                 `+ strconv.Itoa(cliente.PRIVATE) +`,
                 `+ strconv.Itoa(cliente.INCOMPLETO) +`,
                 `+ date_ultima_compra +`,
                 `+ cliente.TICKET_MEDIO +`,
                 `+ cliente.TICKET_ULTIMA_COMPRA +`,
                 '`+ cliente.LOJA_MAIS_FREQUENTE +`',
                 '`+ cliente.LOJA_DA_ULTIMA_COMPRA +`'
                  ),`   
            
            sqlStatement = sqlStatement + row

        }
        
        sqlStatement = sqlStatement[0:len(sqlStatement)-1]
        sqlStatement = sqlStatement + ";"
        
        database.Exec(sqlStatement)
}


func All(){
    database.Exec(`SELECT * FROM clientes WHERE false;` )
}


func Find(id int) Cliente{


    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	"password=%s dbname=%s sslmode=disable",
	host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlInfo)

	if err != nil {
		panic(err)
	}

	defer db.Close()

    var cliente  Cliente

    query  := `SELECT * FROM clientes WHERE id = $1` 

    err = db.QueryRow(query, 1).Scan(
                                    &cliente.ID,
                                    &cliente.CPF,
                                    &cliente.CPF_VALIDO,
                                    &cliente.PRIVATE,
                                    &cliente.INCOMPLETO,
                                    &cliente.DATA_ULTIMA_COMPRA,
                                    &cliente.TICKET_MEDIO,
                                    &cliente.TICKET_ULTIMA_COMPRA,
                                    &cliente.LOJA_MAIS_FREQUENTE,
                                    &cliente.LOJA_DA_ULTIMA_COMPRA,
                                )

    return cliente
}

