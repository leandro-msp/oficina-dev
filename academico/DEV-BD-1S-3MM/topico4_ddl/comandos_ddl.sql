CREATE table CLIENTE(
	id int primary key,
  	nome varchar(10),
  	email varchar(10)
);
/*
select * from CLIENTE; -- dados
desc CLIENTE;-- estrutura da tabela
*/
desc CLIENTE;
alter table CLIENTE add dt_nascimento date not null;
desc CLIENTE;
-- apagar a coluna email
alter table CLIENTE drop column email;
desc CLIENTE;
-- modificar o campo nome 
-- aumentando o tamanho para 100
-- obrigatório
alter table CLIENTE modify column nome varchar(100) not null;
desc CLIENTE;
-- renomear a coluna ou campo
-- dt_nascimento para dt_nasc
alter table CLIENTE rename column dt_nascimento to dt_nasc;
desc CLIENTE;
alter table CLIENTE add cpf varchar(14);
alter table cliente add CONSTRAINT cpf_uniq unique(cpf);
-- cpf - nnn.nnn.nn8-nn
desc CLIENTE;
alter table cliente drop CONSTRAINT cpf_uniq;
desc CLIENTE;
/*
Renomear a tabela CLIENTE para CLIENT 
usando alter table
Depois renomear a tabela para CLIENTES
usando rename 
*/
alter table CLIENTE rename to CLIENT;
desc CLIENT;
show tables; --  mostrar todas as tabelas criadas no ambiente de dev
rename table CLIENT TO CLIENTES;
SHOW TABLES;
drop table CLIENTES;
show tables;