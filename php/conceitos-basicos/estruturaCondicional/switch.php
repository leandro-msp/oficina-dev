<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Switch Case</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php

    //Switch Case
   
    #o switch-case serve para analisar um estado(valor) fixo de uma varíavel, diferente do if else que pode idenficar intervalos
    $horario = "tarde";

    switch($horario){
        case "manhã":
            echo "Bom Dia!";
            break;
        case "tarde":
            echo "Boa tarde!";
            break;
        case "noite":
            echo "Boa noite!";
            break;
        default:
        echo "valor inválido";
    }
    
    echo"<hr>";

    $mtd_pagamento = "Pix";

    switch($mtd_pagamento){
        case "Cartão":
            echo "Insira ou aproxime o cartão";
            break;
        case "Dinheiro":
            echo "Contar cédulas";
            break;
        case "Pix":
            echo "Escaneie o QR Code";
            break;
        default:
        echo " Não Aceitamos Fiado!!";
    }


 
    ?>

    </div>
</body>
</html>