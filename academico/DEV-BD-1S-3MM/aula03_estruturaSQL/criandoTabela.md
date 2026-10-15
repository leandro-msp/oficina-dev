# Criação de Tabelas 
* Para a criação de tabelas são utilizados os comandos DDL  do subconjunto de comandos SQL
* DDL - Data Definition Language - Linguagem de definição de Dados
* Conjunto de comandos que trabalhamd a estrutura de uma tabela.

## Convenções para Nomeação
* Deve começar com uma letra 
* Pode ter de 1 a 30 caracteres
* Deve conter somente A-Z,a-z,0-9,_,$ e #
* Não deve duplicar o nome de outro objeto de propriedade do mesmo usuário

## Comando ```CREATE TABLE``` - sintaxe
```SQL
create table  nome_da_table (
    nome_coluna1 tipo_dado (tamanho) [constraint],
    nome_coluna2 tipo_dado (tamanho) [constraint]
);
```