<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores Aritiméticos</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php
     // OPERADORES ARITIMÉTICOS

    $a = 10;
    $b = 7;
    $c=2;
    
    #adição +
    $soma = $a+$b;
    echo "A soma de a+b é: $soma <hr>";

    #subtração -
    $subtracao = $a-$b;
    echo "A subtração de a-b é: $subtracao <hr>";

    #multiplicação *
    $multiplicacao = $a*$b;
    echo "A multiplicação de a*b é: $multiplicacao <hr>";

    #divisão /
    $divisao = $a/$c;
    echo "A divisão de a/c é: $divisao <hr>";

    # exponencial **
    $expo = $a**$c;
    echo "A potência de a/c é: $expo <hr>";

    # resto da divisão %
    $$mod = $a%$c;
    echo "O $mod da divisão de a/c é: $$mod <hr>";
    

    ?>
    </div>
</body>
</html>