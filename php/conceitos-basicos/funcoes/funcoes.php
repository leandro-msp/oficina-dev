<?php

/* trabalhando com funções 
---- > as funções são blocos de códigos que realizam uma tarefas específica
*/

// função sem parâmetro
function imprimirMensagem(){
    echo "Olá Mundo!\n";
}

imprimirMensagem();

// função que recebe parâmetro
function mensagem($msg){
    echo "$msg\n";
}
 
mensagem("Olá Mundo PHP, esta é uma função com parâmetro"); // o parametro é adicionado no momento que chamar a função VV
mensagem("Nova Mensagem!!"); // toda vez q função é chamada ela não sobrescreve a saída anterior


// função com parâmetros e retornos

function funcaoSoma(int $num1,int $num2){
    #metodo1
    $soma = $num1+$num2; 
    return $soma;
    #metodo 2 
    // return $num1+$num2
}

$ret = funcaoSoma(4,4); // dessa maneira o valor é armazenado na variavel $ret
echo "O resultado da função soma é: ".$ret;

echo "\nO resultado do segundo método de impressão da função soma: ".funcaoSoma(5,18); 
// dessa maneira ja faz a impressão direta da função com os valores atribuidos no parametro

