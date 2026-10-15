CREATE TABLE produto(
	id_produto int not null PRIMARY key AUTO_INCREMENT,
  nome varchar(100) not null,
  valor decimal(6,2) not null check(valor > 0),
  obs varchar(200)
);

desc produto; /*para ver a estrutura da tabela*/

/*adicionando linha em uma tabela*/
insert into produto (id_produto,nome, valor, obs) 
values (100, 'Mouse',30.5,'com fio');

insert into produto (nome, valor)  /*como o id é autoincremente, automaticamente será preenchido*/
values ('Teclado',50.5);

/*inserindo linhas sem relacionar colunas*/
insert into produto values (null,'Monitor',350.5,'Usado'); 

select * from nome_da_tabela; /*pra visualizar os dados inseridos na tablea, utiliza-se este comnando*/

/*atualização de dados*/
update produto set nome = 'Mouse Logitec' /*mudando o nome do produto*/
where id_produto = 100;

update produto 
set valor = 75.3, obs='Teclado com fio' /*atualizando a descrição*/
where id_produto = 101;

select * from nome_da_tabela;

/*atualizando todos os valores de produtos, aumentando 10%*/
update produto 
set valor = valor * 1.1;

select * from nome_da_tabela;

/*sem a clásula WHERE todos os dados são alterados*/
update produto 
set valor = 150;

select * from nome_da_tabela;

/*Removendo dados*/
delete from produto
where id_produto = 100; /* apaga item específico definido*/

select * from produto;


/* apaga tudo

delete from produto; */

/*apagar todos os dados

truncate produto;

*/

