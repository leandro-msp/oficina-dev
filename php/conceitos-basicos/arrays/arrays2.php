<?php

# MANIPULANDO ARRAYS

$num = [1,2,3,4,5,7];

$totalItens = count($num); // count -> conta quantidade de elementos

echo "Quantidade inicial de itens: $totalItens\n";

$num[] = 6; // add novo valor ao array

print_r($num);

$totalItens = count($num);
echo "Nova quantidade de itens: $totalItens\n";

# Organizar Array

sort($num); // ordena valores, quer seja número ou string

    // rsort()   <- ordena de forma decrescente
        // rsort($num);

print_r($num);

# INSERINDO VALORES

array_push($num,8); // função para add valores ao array

/* o array push possue dois parâmetros,sendo:
    1- o array que será modificado
    2- o valor que será adicionado */

print_r($num);

array_push($num,9,10,11,12); // pode adicionar mais de um valor

print_r($num);

# EXCLUINDO VALORES ARRAY INDEXADO

unset($num[10],$num[11]); // o unset() pode realizar diversos tipos de remoção, neste caso é para eliminar um elemento do array
print_r($num);

echo ":::::::::::: ADD VALORES ARRAYS ASSOCIATIVO :::::::::::::::\n";

$frutas = [
    "a" => "Goiaba",
    "b" => "Laranja",
    "c" => "Abacate",
    "d" => "Banana"
];

$frutas['e']= "Pêra";
$frutas['f']= "Uva";
$frutas['g']= "Abacaxi";

print_r($frutas);

/* no array associativo a utilização array_push não é eficaz neste caso(definimos as chaves manualmente).
Ele não identifica o tipo de chave e continua a sequência na forma natural, ele passa a criar novas chaves numéricas.

ex.: [a], [b], [c], [0], [1], [2] ... 

*/
