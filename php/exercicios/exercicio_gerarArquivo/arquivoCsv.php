<?php

// RELATÓRIO DE ESTOQUE

#criando a lista de produtos

$produtos = [
    ["Produto","Quantidade","Valor UND"],
    ["Mouse",1000,200],
    ["Teclado Mecânico",950,370],
    ["Monitor 180Hz",400,899],
    ["Notebook",700,3500],
    ["Celular",800,2500],
    ["Fone de Ouvido",2000,120],
    ["TV",900,2300],
    ["Geladeira",500,2400],
    ["JBL",1300,3000],
    ["PS5 Slim",980,4700],
    ["Aspirador",1200,300],
    ["Fogão",800,900],
    ["Tablet",1300,700]
];

# adicionar coluna valor total
$produtos[0][3]="Valor Total";
for ($i=1;$i<count($produtos);$i++){
    $produtos[$i][3]= $produtos[$i][1]*$produtos[$i][2];
}

#arquivo que será gerado
$nomeArquivo = "relatorioProd.csv";

#criando a função para criar o arquivo

function criarRelatorio($nomeArquivo,$produtos){
    if(count($produtos)>0){ // 
        $abriEscreverArq = fopen($nomeArquivo,'w'); // abre o arquivo "relatoriosProd.csv"
        foreach($produtos as $produto){
            fputcsv($abriEscreverArq,$produto); // escreve cada produto dentro do arquivo aberto
        }
        fclose($abriEscreverArq);  // fecha o arquivo
    }else{
        echo "Não há dados a serem lidos.";
    }

 }

 #chamando a função

criarRelatorio($nomeArquivo,$produtos); 
