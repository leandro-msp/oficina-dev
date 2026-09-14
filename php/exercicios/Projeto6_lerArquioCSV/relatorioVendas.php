<?php

// RELATÓRIO DE VENDAS com Filtro de Categorias

$arquivo = "vendas.csv";

function lerArquivo($arquivo){
    $relatorio = []; // cria arrazy vazio
    if(file_exists($arquivo)){ // verifica se o arquivo existe , caso exista executa a leitura e add cada linha no array
    $lerArquivo = fopen($arquivo,'r');
    while(($linha = fgetcsv($lerArquivo,0,','))!=FALSE){
        $relatorio[] = $linha;
    }
    fclose($lerArquivo); // fecha o arquivo na memória 
    }else{
        echo "Arquivo não encontrado! Por favor, verique se o nome e o endereço do arquivo estão corretos!\n";
    }
    return $relatorio; // array final com dados adicionados
}

$dadosResgatados = lerArquivo($arquivo); // recupera o valor chamando a função lerArquivo e salvando resultado na varíavel 
if(count($dadosResgatados)>0){ // verifica se tem dados recuperados
    echo "Digite a categoria que deseja filtrar, caso queira o relatório completo digite Todos:\n";

    $categoriasValidas =["Acessórios","Armazenamento","Aúdio","Celulares","Componentes",
    "Computadores","Monitores","Móveis","Periféricos","Redes","Todos"];
        echo implode(',',$categoriasValidas)."\n";

    $tipo = trim(ucfirst(readline("Digite a categoria: "))); // usuário digita qual categoria deseja gerar o relatório
    while(!in_array($tipo,$categoriasValidas)){ // certifica se usuário digitou apenas opção válida
        echo "Operação inválida! Por favor, digite uma das disponíveis.\n";
        $tipo = trim(ucfirst(readline("Digite a categoria: "))); // tratamento de string -> elimina espaços e deixando toda primeira letra maiúscula
    }

    echo "\nRELATÓRIO GERADO COM SUCESSO!!\n";

    foreach($dadosResgatados as $indice => $dados){ // para cada índice do array recupera a linha completa e salva em $dados
        if($indice==0){ // ignora o índice zero que é o cabeçalho
            echo implode(',',$dados)."\n";
            continue;
        }
        if ($tipo==="Todos"||$dados[3]===$tipo){//if aninhando com o foreach filtra cada linha gerada de acordo com a categoria digitada pelo usuário
            echo implode(',',$dados)."\n";
        }
    }
}else{
    echo "Não há dados a serem lidos!\n";
}

/*
if(count($dadosResgatados)>0){
    echo "DADOS LIDOS COM SUCESSO!!\n";
    foreach($dadosResgatados as $dados){
        echo implode(',',$dados)."\n";
    }
}else{
    echo "Não há dados a serem lidos!\n";
}
*/



?>