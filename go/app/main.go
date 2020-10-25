package main

import (
	"fmt"
    "strings"
    "strconv"
	"os"
	"time"
    "encoding/csv"
    "github.com/ggbr/gocsv/database"
    "github.com/ggbr/gocsv/model"
    "net/http"
    "github.com/gin-gonic/gin"
)


func main() {

        fmt.Println("Aguardando o banco ser startado ...")
        
        time.Sleep(8 * time.Second)
        
        database.Start()
        
        database.Database()
        
        impostFileCSV()
        
        r := gin.Default()

        r.GET("/", func(c *gin.Context) {
            c.JSON(200, gin.H{
                "url": "http://localhost:81/cliente/1",
            })
        })

        r.GET("cliente/:id", func(c *gin.Context) {

            id, err := strconv.Atoi(c.Param("id"))

            if err != nil {
                panic(err)
            }

            cliente := model.Find(id)
            c.JSON(http.StatusOK, gin.H{
                    "id"            :cliente.ID,
                    "cpf"           :cliente.CPF,
                    "valido"        :cliente.CPF_VALIDO,
                    "private"       :cliente.PRIVATE,
                    "incompleto"    :cliente.INCOMPLETO,
                    "data_ultima_compra" :cliente.DATA_ULTIMA_COMPRA,
                    "ticket_medio"  :cliente.TICKET_MEDIO,
                    "ticket_ultima_compra"  :cliente.TICKET_ULTIMA_COMPRA,
                    "loja_mais_frequente" :cliente.LOJA_MAIS_FREQUENTE,
                    "loja_ultima_compra" :cliente.LOJA_DA_ULTIMA_COMPRA})    
        })

        r.Run()
}

func impostFileCSV(){

    csvfile, err := os.Open("file.csv")
    
    if err != nil {
        panic(err)
    }
    
	defer csvfile.Close()

    reader := csv.NewReader(csvfile)
    
	reader.Comma = '\t'

	rawCSVdata, err := reader.ReadAll()

	if err != nil {
		 fmt.Println(err)
		 os.Exit(1)
	}


	for l, lineCSV := range rawCSVdata {
        if l > 1{

            clientData := strings.Fields(lineCSV[0])

            private, err := strconv.Atoi(clientData[1])
            
            if err != nil {
                panic(l)
            }
            incompleto, err := strconv.Atoi( clientData[2])
            if err != nil {
                panic(err)
            }

            model.ClienteNew(
                clientData[0],
                private,
                incompleto,
                clientData[3],
                clientData[4],
                clientData[5],
                clientData[6],
                clientData[7])
        }
    }
    
    model.InsertClients()
}





