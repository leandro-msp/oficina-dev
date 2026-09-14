<?php
/*crie uma função que colete o nome do aluno, nota 1, nota 2, e calcule media
    posteriormente deve retornar o nome do aluno e a média adquirida.
*/

function calcularMedia(string $nome,int $nota1,int $nota2){
    $media = ($nota1+$nota2)/2;
    return "O aluno ".$nome." obteve a média ". $media;
}

$resultado = calcularMedia("Leandro",8,9);
echo $resultado;



?>