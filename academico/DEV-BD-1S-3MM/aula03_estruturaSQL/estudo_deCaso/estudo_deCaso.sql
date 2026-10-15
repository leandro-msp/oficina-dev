CREATE TABLE ESTUDANTE (
    id_estu INT PRIMARY KEY, 
    ra VARCHAR(10) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    nota DECIMAL(3,1)
);

/*adicionando constraint posteriormente*/

CREATE TABLE ESTUDANTE (
    id_estu INT NOT NULL,
    ra VARCHAR(10) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    nota DECIMAL(3,1),
    PRIMARY KEY (id_estu)
);