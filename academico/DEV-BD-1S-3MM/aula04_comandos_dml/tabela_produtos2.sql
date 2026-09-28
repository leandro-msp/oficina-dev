/*
PRODUTO				
id_produto	inteiro	obrigatório	chave primária	auto_increment
nome	texto variavel(100)	obrigatório		
valor	número(7,2)	obrigatório		99999.99
dt_inclusao	data			

visualizar a estrutura da tabela	

id_produto	nome	valor	dt_inclusao
1	          Celular	5789.35	2025-08-04
2	          Tablet	2500.00	2025-08-04
3	          Mouse	250.50	2025-08-04
4	          Monitor	1500.55	2025-08-05
5	          Capinha de celular	25.30	2025-08-05

Alterar o produto de Mouse para Mouse Gamer, 
mudando o valor para 550.30

Apagar o Tablet
*/

create table PRODUTO(
  id_produto int not null primary key auto_increment,
  nome varchar(100) not null,
  valor decimal(7,2) not null check(valor>0),
  dt_inclusao date
);

desc PRODUTO;

insert into PRODUTO values (null,'Celular',5789.35,'2025-08-04');
insert into PRODUTO values (null,'Tablet',2500.00,'2025-08-04');
insert into PRODUTO values (null,'Mouse',250.50,'2025-08-04');
insert into PRODUTO values (null,'Monitor',1500.55,'2025-08-05');
insert into PRODUTO values (null,'Capinha de celular',25.30,'2025-08-05');

select * from PRODUTO;

update PRODUTO set nome='Mouse Gamer',valor=550.30
  where id_produto=3;


select * from PRODUTO;

delete from PRODUTO where id_produto=2;

select * from PRODUTO;

