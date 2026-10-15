<?php

/*
Enunciado do Programa:

Desenvolva um programa em PHP 8 que receba um número inteiro fornecido pelo usuário e determine se ele é par ou ímpar.

O programa deve exibir uma mensagem indicando se o número é par ou ímpar.
*/


$numero = (int)readline("Digite um número: ");

if ($numero%2==0){ // com base no resto da divisão é possível saber se um número é par ou ímpar
    echo " O valor digitado foi: $numero, sendo ele um número par.\n"; 
}else{
    echo "O valor digitado foi: $numero, sendo ele um número ímpar.\n";
}



?>