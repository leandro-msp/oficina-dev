<?php
// exercicio 1 - rodar no terminal

echo "Escreva seu nome: \n";
$nome = readline(); // readline -> campo para o usuário digitar valores

echo "Informe sua idade: \n";

$idade =(int)readline(); 

# echo gettype($idade); // <-- função gettype() aponta o tipo de dado da variável (int,string,float,boolean)

/* por padrão qualquer tipo de dando inserido através da funcão readline() é do tipo string,
a variavel idade deve ser tratata como inteiro, para isso usamos o operador de conversão (int).
Há também a função intval() que executará mesmo processo, entretanto essa função possui algumas distinções técnicas, e usado conversões mais detalhadas. 
*/
echo "Digite a profissão: \n";
$profissao = readline();

echo "$nome é $profissao e tem $idade anos de idade.\n";








?>