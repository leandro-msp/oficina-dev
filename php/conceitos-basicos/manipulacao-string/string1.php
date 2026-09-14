<?php

$string = "  Novo texto  ";
$string1 = "Esse é um novo texto  ";


#Eliminar espaços em branco - função trim

$trim = trim($string); // elimina espaços no começo e no final 
$ltrim = ltrim($string); // elimina espaços em brano à esquerda 
$rtrim = rtrim($string); // elimina espaços em branco à direita

echo "$string\n"; // sem tratamento
echo "$trim\n"; // com tratamento trim (começo e fim)
echo "$ltrim\n"; // com tratamento ltrim (à esquerda)
echo "$rtrim\n"; // com tratamento rtrim (à direita)

echo "::::::::::::::::::::::::::::::::::::::::::::::::::\n";
echo "STRLEN E SUBSTR:\n";


# Mostrar a quantiade de caracateres de uma string - função strlen()

$contar  = strlen($string1);
echo "A string possui $contar caracateres \n";

# mostar um determinado número de caracteres - função substr()
$extrair = substr($string1,8,12);

/* função substr possui 3 parâmetros: 
1 - local onde será pesquisado
2 - índice onde inicia a contagem (extração)
3 - índice onde termina
*/

echo $extrair."\n";

$codigo = 5;

# Adicionar caracateres á string - função str_pad()

$padEsquerda = str_pad($codigo,8,'0',STR_PAD_LEFT);
$padDireita = str_pad($codigo,8,'0',STR_PAD_RIGHT);

/* função str_pad possui 4 parâmetros:
1 - onde será alterado
2 - a quantidade total de caracteres que deve possuir
3 - qual caracterese será adicionado até completar as quantidade definida
4 - a posição que será adicionado antes ou depois do valor resgatado do banco de dados, por exemplo.
*/

echo "\nValor original: $codigo \n";
echo "Caractere add à esquerda: $padEsquerda \n";
echo "Caractere add à direita: $padDireita \n";

