<?php
// como definir e atribuir valor a uma constante

define("NOME","Lucia"); // uma constante não pode ter seu valor alterado 

echo NOME;

define("ADMIN","admin"); // padrão users em roteadores

echo "<hr>";

# método 2

const IDADE = 18;

echo IDADE."<hr>";

# CONSTANTES MÁGICAS

echo "Linha atual: ". __LINE__ ."<hr>";
// recupera o número da linha de código atual

echo "Caminho do arquivo atual: ".__FILE__."<hr>";
// recupera o endereço do arquivo atual

echo "Nome do diretório atual é: " . __DIR__."<hr>";
// recupera o diretório(pasta) atual


