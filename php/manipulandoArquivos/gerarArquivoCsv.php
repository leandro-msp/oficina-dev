<?php
//Trabalhando com manipulação de arquivos 

#local onde as informações serão extraídas
$usuarios = [
    ["Nome","Idade","e-mail"],
    ["Mateus",34,"mateus@yahoo.com"],
    ["Lucas",27,"lucas@teste.com"],
    ["Bruna",22,"bruna@outlook.com"],
    ["Letícia",32,"leticia@gmail.com"]
];

#função para criar o arquivo
function gerarArquivosCsv($nomeArquivo,$usuarios) // primeiro parâmetro onde vai armazenar(criar), segundo de onde vai retirar
{
    //1º verificar se os dados existem
    if(count($usuarios)>0): // se maior que zero, tem dados
        $escreverCsv = fopen($nomeArquivo,'w'); // função fopen ela serve para ler e escrever arquivos, e os parâmetros utilizados foram: 
        //1º nome do arquivo a ser acessado
        //2º qual o método de manipulação será usado, ler ou escrever?, para ler usa-se 'r' de read, e para escrever usa-se 'w' de write.
        foreach ($usuarios as $dados){
            fputcsv($escreverCsv,$dados);// 1ºparametro: Arquivo que foi aberto, 2º os dados que serão escritos nesse arquivo
        } // para cada dado dentro de $usuarios, salvar na variável $dados, e escrever no arquivo aberto
        fclose($escreverCsv); // fechar o arquivo
    else:
        echo " Não há dados";
    endif;
}

$nomeArquivo = "usuarios.csv";

gerarArquivosCsv($nomeArquivo,$usuarios);

?>