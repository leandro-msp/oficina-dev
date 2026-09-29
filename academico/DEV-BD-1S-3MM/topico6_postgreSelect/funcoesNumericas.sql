-- exemplos

-- Arredondar o valor para determinado decimal e deixa duas casas decimais 
SELECT ROUND(12.3456, 2); -- 12.35 

-- descarta numeros decimais ou partres de uma data sem fazer o arredondamento tradicional
SELECT TRUNC(12.389, 1); -- 12.3

-- corta | arredondar
SELECT TRUNC(12.389, 1), round (12.389, 1); -- 12.3 | 12.4

SELECT TRUNC(12.789, 1), round (12.789, 1); -- 12.7 | 12.8

SELECT TRUNC(12.789, 0), round (12.489, 0); -- 12 | 12  -> nenhuma casa decimal


-- resto divisao
SELECT MOD ( 15,2) -- 1 

-- power -> eleva um número a uma potência - > POWER(base,expoente) ou POW(base,expoente)
select power (3,2); -- 9

-- calculo de raiz quadrada
select sqrt(25);

-- transformar um valor numérico em número inteiro(arredonda para baixo)

select floor (12.789) , trunc (12.789,0), round (12.789,0); -- 12 | 12 | 13

-- Calcule o restos da divisão de 8 por 2, 7 por 2 e 7 por 4.
SELECT mod(8,2), mod(7,2), mod(7,4); -- 0,1,3

-- Calcule a raiz quadrada de 16 e 4 elevado ao quadrado
SELECT sqrt(16), power(4,2)  ;

