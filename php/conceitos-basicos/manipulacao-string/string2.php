<?php

$string = "NOVO TEXTO";
$string1 = "Esse é um novo texto";


# Converter cadeia de caractere totalmente maíuscula em minúscula -> função strtolower()

$minuscula = strtolower($string);
echo "Sem tratamento: ".$string."\n"; // texto sem tratamento
echo "Minúscula:".$minuscula."\n"; // texto com tratamento

echo ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n";

# Converter cadeira de caracteres minúscula para maiúscula -> função strtoupper()

$maiuscula = strtoupper($string1);
$maiuscula2= mb_strtoupper($string1); // 2º método que inclui na conversão caracteres com acento, símbolos.

echo "Sem tratamento: ".$string1."\n"; // sem tratamento
echo "Maiúscula: ".$maiuscula ."\n"; // com tratamento
echo "Maiúscula 2: ".$maiuscula2 ."\n"; // com tratamento

echo ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n";

# Atribuir a letra maiúsculas somente para o primeiro caractere

$caps = ucfirst(strtolower($string));

/* a $string1 possui todos os caracteres em maíusculo, então foi utilizado um encadeamento de funções.
primeiro converte todos os caracteres para minúsculo e somente depois deixa a primeira letra em maiúsculo.
*/

echo "Primeira letra: ".$caps ."\n";

$caps2 = ucwords(strtolower($string));
// ucwords -> deixa a primeira letra de cada palavra da mensagem em maiúsculo.

echo "Primeira letra de cada palavra: ".$caps2."\n";


/* a formatação de entrada de caracteres é muito importante no momento que está armazenando/editando dados no banco de dados,
isso cria um padrão de escrita, a fim de evitar problemas na inserção de dados caso o usuário preencha campos deixando espaços, mistura de carcateres, etc.
*/