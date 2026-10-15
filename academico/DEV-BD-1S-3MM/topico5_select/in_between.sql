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

/*
selecione o nome dos produtos que 
não tenham data de cadastro
*/
select nome as "Produtos",dt_criacao as "data de cadastro"
  from produto
     where dt_criacao is null;
     
-- com datas não nulas

select id_prod, nome as "Produtos",dt_criacao as "data de cadastro"
  from produto
     where dt_criacao is not null;
     
/*
selecione o nome, categoria, preco e dt_criacao
dos produtos com datas de criação no dia 29/10/2023 ou produtos com categoria ssd
*/
select nome,categoria,preco, dt_criacao
  from produto
    where dt_criacao='2023-10-29'
      or categoria="ssd" order by preco desc;
      
-- operador and 
-- a principio nn exibe nada, pois nn tem sdd cadastrado no dia 29
-- por isso a troca para 26/10
-- pois o AND precisa que ambas condições sejam verdadeiras

select nome,categoria,preco, dt_criacao
  from produto
    where dt_criacao='2023-10-26'
      and categoria="ssd" order by preco desc;
      
/*
selecione todos os produtos cadastros
no mês de outubro de 2023
*/
select * from produto
where dt_criacao>='2023-10-01' and dt_criacao<='2023-10-31';

-- operador between e not between
-- selecione os ids que estenjam entre 3 e 7

select id_prod from produto
  where id_prod between 3 and 7;
  
-- valores q nn estão entre 3 e 7

select id_prod from produto
  where id_prod not between 3 and 7;
  
/*
IN , NOT IN
selecione todo os produtos 
que tenham categoria ssd, fone
*/

select * from produto
where categoria in ('ssd','fone');

--  que nn possuam as categorias acima

select * from produto
where categoria not in ('ssd','fone');

/*
selecione o id_prod e nome dos produtos
para os seguintes ids: 2,5,7 e 9
*/  

select id_prod, nome 
from produto
where id_prod in (2,5,7,9);

-- que nn sejam os ids 2,5,7,9

select id_prod, nome 
from produto
where id_prod not in (2,5,7,9);