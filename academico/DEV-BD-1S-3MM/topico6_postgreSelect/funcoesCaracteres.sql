/*
 No PostgreSQL tem um comportamento na interface que estiver sendo utilizada : 
 Se você tiver vários comandos na tela e clicar em "Executar" (F5), o editor tenta rodar todo o script da tela de uma vez só,
 de cima para baixo. Se você não comentar ou não selecionar apenas o comando que quer, ele reexecutará tudo o que ficou para trás.
*/

-- NOS EXEMPLOS ABAIXO, AS LINHAS DE COMANDOS NÃO ESTÃO COMENTADAS. APÓS O TÉRMINO DAS ATIVIDADES E TESTES AÇÃO DE COMENTAR FOI REMOVIDA PARA FINS DIDÁTICOS

-- a tabela utilizada para os teste foi a "funcionarios.sql"


select * from funcionario; -- mostrar todos os dados da tabela
select lower(departamento),upper(nome) from funcionario; -- lower converte o texto para minúsculo 

--Selecione nome com letras maiúscula, departamento com letras minúscula da tabela funcionário, ordenado por nome.
select upper(nome), lower(departamento) 
from funcionario 
order by nome

-- Selecione o nome com a primeira letra Maiúscula e departamento da tabela funcionario de forma que os dados apareçam ordenados, observe qual foi o último nome mostrado!
select initcap(nome) as nome, departamento 
from funcionario
order by upper(nome); 

select upper ('perguntas'); --  upper converte o texto para maiúsculo
select CONCAT('Olá, ', 'Mundo!'); -- concatena string (sintaxe de função)

-- selecionar os campos nome e salario da tabela
select nome, salario 
from funcionario; 


-- seleciona o campo nome, e tbm seleciona o campo salario concatenado com o texto apresentado
select nome, concat('R$', salario) from funcionario; 

 -- comando de exemplo
select substr ('ABCDE', 1,3); -- extrai parte da uma string, funciona por índice (nº1 onde inicia, nº2 qtdd de caracateres)



select nome , substr (nome,1,4) 
from funcionario; 
-- a saída sera duas colunas, campo nome padrão, e campo nome com extração de apenas 4 caracteres, começando pelo primeiro caractere

select length ('sql'); -- 3 | obtém o comprimento da string


select concat (nome, ' - ', length(nome)) from funcionario; -- nome do funcionário e quantidade de caracatere daquele nome, ambos dados separados por um ífen adicionado por concat

select position ('SQL' in 'MySQL é um SGBD'); -- 3 | indica a posição que o elemento procurado se inicia dentro do outro conjunto/elemento indicado

select nome, position('a' in nome) from funcionario; -- indicando onde a letra aparece pela primeira vez dentro dos nomes dos funcionários
-- há um detalhe, essa função é case sensitive, caso tenha a letra for maiúscula não irá reportar como válida

select nome, position('a' in lower (nome)) from funcionario; -- desta forma se houver letras maísculas será todas convertidas

SELECT LPAD ('42', 5 ,'0'); -- preenche a esquerda | 1 parametro : o elemento base , 2 paramentro: qtdd de caracteres total deve ter , 3 parametro: o elemento que será usado para preencher

SELECT LPAD ('42', 5 ,'b');
SELECT RPAD ('42', 5 ,'1'); -- preenche a direita 

Select trim ('  texto  '); -- remove espaços das extremidades -> saida: "texto"

Select trim ('!  Texto  !'); -- neste caso espaços nn serão removidos

select concat('-','   texto   ','-'); -- concatena o ífen nas extremidades 

select concat('-',trim('   texto   '),'-'); -- remove o espaço vazio e concatena o ífen nas extremidades 

