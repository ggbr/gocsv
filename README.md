# Processar lista

Script para processar uma lista de clientes e salvar no banco de dados.

O problema foi resolvido de duas formas diferente usando a linguagem **go** e **python** mas mantendo o mesmo fluxo abaixo.


## Fulxo do programa
```mermaid
graph TD
A[Iniciar banco de dados]  --> B[Criar tabela de clientes]
B --> C[Processar os dados do arquivo]
C --> D[Tratar os dados validar CPF e remover Caracteres]
D --> E[Criar query SQL e insere no banco]
E --> F[Expõe uma API de acesso aos dados]
```

## Teste escrito em Python
O projeto esta dentro do diretorio **python**

> cd  ./python


o projeto pode ser iniciado com o comando 

    make install
ou 

    docker-compose up

### Outros comandos

para reiniciar o projeto do zero (compilando e sem nada no banco de dados)

    make reset
Acessar o terminal do container da aplicação

    make bash

## Teste escrito em GO

O projeto esta dentro do diretorio **go**

> cd  ./go

o projeto pode ser iniciado com o comando 

    make install
ou 

    docker-compose up

### Outros comandos

para reiniciar o projeto do zero (compilando e sem nada no banco de dados)

    make reset
Acessar o terminal do container da aplicação

    make bash


