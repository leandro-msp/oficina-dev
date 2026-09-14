<?php
# LENDO ARQUIVOS CSV COM PHP

// CRIANDO A FUNÇÃO 


// 1 - criando nome do arquivo q vai ser lido, e a função informando o parâmetro


$nomeArquivo = "usuarios.csv"; // neste caso o arquivo está dentro da nossa pasta do projeto, caso contrário deveriamos colocar o diretório de onde o arquivo se encontra

function lerCsv($nomeArquivo){
    $usuarios = []; // cria lista vazia pra receber os dados

//2 - verificar se o arquivo existe, e se exisiter abir em modo leitura

    if(file_exists($nomeArquivo)) // file-exists -> uma função que verifica se determinado arquivo existe
        { $abrirArquivo = fopen($nomeArquivo,'r');
//3 - verificar se existem linhas dentro do arquivo utilizando função fget e passando especificações das linhas, enquanto existir linha, adicionar cada uma dentro do array usuarios

            while (($linha = fgetcsv($abrirArquivo,0,','))!== FALSE)
            // fgetcsv => captura as linhas do arquivo | Parametro 1: Arquivo aberto , Paramentro2 : qtd de caractere por linha, o valor 0 o PHP se encarrega de fazer a leitura
            // Parametro3: delimitador(separador), no nosso caso é a vírgula, FALSE -> verifica se a linha existe conforme as especificações passadas
            {
                $usuarios[] = $linha; // para cada linha encontrada add dentro do array
            }
//4 - fechando o arquivo
            fclose($abrirArquivo);
    }else{
        echo "Arquivo não encontrar, por favor verifique o caminho digitado.\n";
    }
//5 - retornar o resultado final
    return $usuarios; // ler o array
}

//6- Guardar os valores recuperados
$dadosLidos = lerCsv($nomeArquivo); // armazena o resultado na varíavel dados lidos


//7- Separar os dados e ordenadamnete
if(count($dadosLidos)>0): 
    echo "Dados encontrados: \n";
    foreach($dadosLidos as $dados){ 
        echo implode(',',$dados). "\n";
        // função implode do php cria uma separação toda vez que ele achar o caractere informado , neste caso a vírgula, e assim entende q o próximo é um novo valor e automaticamente define o tipo(string, int, float,bool)
        // 1 paramentro : O separador | 2 parametro : onde fazer a varredura
    }
else:
    echo "Nenhum dado foi encontrado!!";
endif;


?>