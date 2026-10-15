-- mostrar a data e hora atual do sistema

select now(); -- saida sera a data e hora atual do servidor

-- formatar DATA para String

SELECT TO_CHAR(NOW(), 'DD/MM/YYYY HH24:MI') AS "data/hora atual"; -- exemplo : 24/10/2025 09:30
-- o comando converteu o formato da hora para formato string, conforme a padrão solicitado, 
-- e foi atribuido um apelido a coluna

-- UTILIZANDO A TABELA EXEMPLO "FUNCIONARIO.SQL"

select * from funcionario;

select nome, dt_nascimento 
from funcionario;

-- utilizando formatação na data -> convertendo data para string
select nome,to_char(dt_nascimento, 'DD/MM/YYYY')
from funcionario;

-- mostrar os campos nome e data de nascimento no formato dd/mm/aaaa da tabela funcionario, sendo a saída ordenada pela data de nascimento
select nome as "Nome",to_char(dt_nascimento, 'DD/MM/YYYY') as "Data de nascimento"
from funcionario
order by dt_nascimento desc;


SELECT EXTRACT (year from now()) as ano_atual;




