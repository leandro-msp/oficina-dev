/*
FILME
id_filme numérico obrigatório chave primária
titulo texto variável 100 obrigatório 
data_lanc data opcional
gênero texto variável 50 obrigatório 
*/
create table FILME(
  id_filme int not null primary key,
  titulo varchar(100) not null,
  data_lanc date,
  genero varchar(50) not null
);
desc FILME;-- mostrar a estrtura da tabela
/*
INSERT INTO Nome_Tabela (coluna1, coluna2, colunaN)
       VALUES (valor1, valor2, valorN);
       06/11/82
       date YYYY-MM-DD
*/
insert into FILME (id_filme,titulo,data_lanc,genero)
            values(1,'Rambo','1982-11-06','Ação');
            
insert into FILME (id_filme,genero,titulo)
            values (2,'Terror','Bob Esponja');
-- treino, incluir 2 filmes, 1 com data de lanc 
-- e outro sem data de lanc            
insert into FILME (id_filme,titulo,data_lanc,genero)
            values (3,'Matrix','1999-05-21','Ação');
insert into FILME (id_filme,titulo,genero) 
            values (4,'E o vento levou','Romance');
            
-- INSERT INTO Nome_Tabela VALUES (valor1, valor2, valorN);  
insert into FILME values(5,'Rambo 2','1985-05-22','Ação');
insert into FILME values(6,'Sexta feira 13',NULL,'Terror');

select * from FILME;  

/*
UPDATE nome_da_tabela
SET Coluna = Novo_Valor, Coluna = Novo Valor...
WHERE Condição;
*/
update FILME 
set genero='Animação'
where id_filme=2;
-- mudar a data e o genero para o filme E o vento levou
-- 01/01/1940 - Drama
update FILME
set data_lanc='1940-01-01',genero='Drama'
where id_filme=4;

select * from FILME;  
