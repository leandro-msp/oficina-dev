/*Exemplo prático - tabela estudante

    colunas: id_ estudante, nome, ra, data_nascimento
*/


/*ORACLE*/
create table estudante (
    id_estudante NUMBER(4) PRIMARY KEY, /*tipo numero unico e obrigatório*/
    nome VARCHAR(100) NOT NULL, /*tipo carcatere e não poder ser nulo*/
    ra VARCHAR(10) NOT NULL UNIQUE, /*tipo carcatere, não poder ser nulo e é valor unico*/
    data_nascimento DATE;
)

/*MySQL*/

CREATE TABLE ESTUDANTE (
    id_estudante INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ra VARCHAR(10) NOT NULL UNIQUE,
    data_nascimento DATE
);

/*PostgreSQL*/

CREATE TABLE ESTUDANTE (
    id_estudante SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ra VARCHAR(10) NOT NULL UNIQUE,
    data_nascimento DATE
);