create table PRODUTO(
 id_prod int not null primary key auto_increment,
 nome varchar (100) not null,
 preco decimal (7,2) not null,
 categoria varchar(40) not null,
 estoque int not null,
 dt_criacao date);
 
insert into produto (nome, preco, categoria,estoque) values ('HD Ssd 480gb',309.50,'ssd',10);
insert into produto (nome, preco, categoria,estoque) values ('HD Ssd 240gb',188.00,'ssd',15);
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('HD Ssd 100gb',135.00,'ssd',20,'2023-10-26');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Pen Drive 32GB',24.90,'pendrive',50,'2023-10-27');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Pen Drive 128GB',109.53,'pendrive',50,'2023-10-27');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Mouse Gamer 12.000 DPI ',159.99,'mouse',7,'2023-10-28');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Mouse Gamer Pro M7 Rgb ',51.24 ,'mouse',9,'2023-10-28');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Teclado Semi Mecânico Gamer Profissional USB Abnt2 Iluminado Led Rgb',41.90 ,'teclado',12,'2023-10-29');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Teclado Gamer Cyclosa + Mouse Gamer Abyssus 1.800 DPI',123.67 ,'teclado',4,'2023-10-29');
insert into produto (nome, preco, categoria,estoque, dt_criacao) values ('Fone De Ouvido Headset Gamer P2 Para Ps4 Xbox One Notebook Macbook Com Microfone',79.29 ,'fone',25,'2023-10-29'); 

desc PRODUTO;

select * from PRODUTO; -- ordem de criação(insert)

select nome,preco from PRODUTO order by nome; --  ordenado pelo nome

select nome,preco from PRODUTO order by preco; -- ordenado pelo preco

select nome,preco from PRODUTO order by preco desc;

select nome from PRODUTO order by nome desc;

/*
como selecionar o nome e categoria da tabela produto,
ordenado pelo nome em ordem decrescente
*/

select nome,categoria from PRODUTO order by nome desc;

/*
Como selecionar o nome com alias Produto e preço com alias
Preçp do Produto da tabela produto?
*/

select nome as Produto, preco as "Preço do Produto" from PRODUTO;

-- criar relatório mostrando todos os campos com apelido
-- ordenado pela data de forma decrescente

select
id_prod as "Código do Produto",
nome as Produtos,
preco as "Preço do Produto",
categoria as Categoria,
estoque as Estoque,
dt_criacao as "Data de Cadastro"
    from PRODUTO
    order by dt_criacao desc;
    
    
select distinct categoria from PRODUTO order by categoria;


select distinct estoque from PRODUTO order by estoque;

-- Utilizando operadores artiméticos

select 27/2;
select 27%2;


/*
Selecione os campos nome, preco, preco + 10, 
categoria da tabela produto, ordenado por preco
*/
  
select nome,preco,preco+10 as "Aumento de R$10",categoria
from produto order by preco desc;

select nome,preco,preco*1.10 "Aumento de 10%",categoria
from produto order by preco desc;


/*
selecionar todos os nomes dos produtos, 
com preço e preço com desconto de 5%
*/

select nome,preco,preco*0.95 as "Desconto de 5%" from produto order by preco desc;

select 17%2 as "resto de 17 por 2";

/*
selecione o nome e datas dos produtos 
com data de cadastro do dia 28/10/2023 
*/

select nome,dt_criacao as "Data de criação" 
  from produto 
    where dt_criacao='2023-10-28';

-- a partir do dia 
select nome,dt_criacao as "data"
  from produto 
    where dt_criacao>='2023-10-28';

-- após o dia 
select nome,dt_criacao  as "data"
  from produto 
    where dt_criacao>'2023-10-28';
