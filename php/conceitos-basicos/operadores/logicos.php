<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores Lógicos</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php
    
    //Operadores Lógics
    $a = 9 ;
    $b = 7 ;
    $c = 14;
    
    #OU or ||
    $ou = ($a==$b || $a >8); # basta somente que uma das comparações seja verdadeira, para que toda a expressão serja verdadeira
    echo "Ou: ";
    var_dump($ou);
    echo "<hr>";
    
    #E and &&
    $e = ($a==$b && $a<8 && $c >=13); # requer que todas as comparações\condições sejam verdadeiras
    echo "e: ";
    var_dump($e);
    echo "<hr>";
    $e = ($a!=$b && $a>8 && $c >=13); # requer que todas as comparações\condições sejam verdadeiras
     echo "e: ";
    var_dump($e);
    echo "<hr>";


    #Não - Not !
    $nao = ($a <= $b);
    echo "não: ";
    var_dump($nao);
    echo "<hr>";

    #negação inverte o valor da expressão , se true, passa a ser false. Se false, passa a ser true
    $nao = !($a <= $b);   // mesmo que afirmar: "Não é verdade que $a é menor ou igual a $b)" isto é uma afirmação verdadeira
    echo "não: ";
    var_dump($nao);
    echo "<hr>";

    ?>
    </div>
</body>
</html>