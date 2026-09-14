<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores Relacionais</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php
    
    // Operadores 

    $a = "a";
    $b = "c";
    $c = 9;
    $d = 5;
    $e = 5;

    #OPERADORES DE COMPARAÇÃO

    //Igualdade
    $igual = $a==$b; # compara se os valores são iguais 
    echo "Igualdade: ";
    var_dump($igual);
    echo "<hr>";

    //Idêntico
    $identico = $c===$d; # além de comparar valores, compara se o tipo de dados também é o mesmo
    echo "Idêntico: ";
    var_dump($identico);
    echo "<hr>";

    //diferente
    $dif = $c != $d ;  # verifica se os valores não são iguais
    echo "Diferente: ";
    var_dump($dif);
    echo "<hr>";

    //Menor que | Maior que 
    $menor = $c < $d; # verifica se o valor primeiro elemento é menor que o segundo
    echo "Menor que: ";
    var_dump($menor);
    echo "<hr>";

    $maior = $c > $d; # verifica se o valor primeiro elemento é maior que o segundo
    echo "Maior que: ";
    var_dump($maior);
    echo "<hr>";


    //Menor igual | Maior igual
    $men_igual = $c <= $e; # verifica se o valor do primeiro elemento é menor ou igual que o segundo
    echo "Menor ou igual: ";
    var_dump($men_igual);
    echo "<hr>";

    $mai_igual = $e >= $d;  # verifica se o valor do primeiro elemento é maior ou igual que o segundo
    echo "Maior ou igual: ";
    var_dump($mai_igual);
    echo "<hr>";


    ?>
    </div>
</body>
</html>