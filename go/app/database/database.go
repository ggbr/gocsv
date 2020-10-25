package database

import (
	"fmt"
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

func Database(){
	fmt.Println("teste database")
}

func TestConnection(){

	fmt.Println("Inicias teste postgres")

	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	"password=%s dbname=%s sslmode=disable",
	host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)

	if err != nil {
		panic(err)
	}

	defer db.Close()

	err = db.Ping()

	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected!")
}

func Start(){

	fmt.Println("Inicias teste postgres")

	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	"password=%s dbname=%s sslmode=disable",
	host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)

	if err != nil {
		panic(err)
	}

	defer db.Close()

	Exec(`CREATE TABLE clientes (
		
			id SERIAL PRIMARY KEY,
			cpf varchar(60),
			cpf_valido INT,
			private INT,
			incompleto INT,
			data_ultima_compra DATE null,
			ticket_medio FLOAT null,
			ticket_ultima_compra FLOAT null,
			loja_mais_frequente varchar(60) null,
			loja_da_ultima_compra varchar(60) null
	);`)

	fmt.Println("Create table clients")
}






func Exec(query string){

	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	"password=%s dbname=%s sslmode=disable",
	host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlInfo)

	if err != nil {
		panic(err)
	}

	_, err = db.Exec(query)

	if err != nil {
		panic(err)
	}


	defer db.Close()
}





