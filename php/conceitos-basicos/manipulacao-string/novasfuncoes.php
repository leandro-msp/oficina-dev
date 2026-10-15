<?php
$mensagem = "Curso completo de PHP";

//todas as funções abaixo retorna um valor booleano (true/false)

# Confirmar se a string possui o valor informado 

$possui = str_contains($mensagem,'completo');  
echo "Possui: ".$possui."\n"; 
echo "GETTYPE: ".gettype($possui)."\n"; // <-- get não mostra o valor, somente o tipo

var_dump($possui); // <- unção de depuração que exibe o tipo de dado, o valor , e o tamanho

//método curto 
echo "Str Contains: ";
var_dump(str_contains($mensagem,'completo')); 

# Confirmar se a string começa com valor informado 
echo "Start With: ";
var_dump(str_starts_with($mensagem,'Curso')); 


# Confirmar se a string termina com o valor informado 
echo "Ends With: ";
var_dump(str_ends_with($mensagem,'PHP')); 

#método com formatação para não cair no case sensitive

// ex.:
echo "\nEnds With -> php minúsculo:\n";
echo "var_dump+strtolower: ";
var_dump(str_ends_with(strtolower($mensagem),'php'));

$termina = str_ends_with(strtolower($mensagem),'php');
echo "Gettype: ".gettype($termina)."\n";
var_dump($termina);
