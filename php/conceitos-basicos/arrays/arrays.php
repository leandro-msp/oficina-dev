<?php 

# ARRAYS NUMÉRICO(INDEXADO)

echo ":::::::::::::ARRAY NUMÉRICO:::::::::::::\n";


$num = [1,2,3,4,5,7]; // a chave é definida automaticamente, sendo ela os índices
print_r($num); // <- usa-se para exibir a matriz completa | o echo serve para saídas simples como strings e números

//resgatando valores:
echo "\nValor do índice[3]: $num[3]\n"; 

# ARRAYS ASSOCIATIVO

echo ":::::::::::::ARRAY ASSOCIATIVO:::::::::::::\n";

$frutas = [
    "a" => "Goiaba",
    "b" => "Laranja",
    "c" => "Abacate",
    "d" => "Banana"
]; 
/*no arrays associativo nós definimos o nome das chaves, e a tribuição de valores é dada através do sinal de = e maior "=>"
    obs.: as chaves geramelmente não são adicionadas a mão, mas sim automaticamente, conforme as regras de negócio do sistema */

print_r($frutas);
echo "\nVaor do índice[b]: $frutas[b]\n";

