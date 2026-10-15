<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Match</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php
    # Estrutura de Controle - Match

    /*
    Diferente do Switch-case, no  match, resultado da verificação é armazenado é uma variável,
    e a expressão/instrução é atribuída direto no caso.
    */

    $turno = "Manhã";

    $resultado = match ($turno) {
        "Manhã" => "Bom dia!",
        "Tarde" => "Boa Tarde!",
        "Noite" => "Boa Noite!",
        default => "Horário Inválido"
    };

    echo $resultado;

    // o match também é uma expressão CaseSensitive, já que adota a verificação idêntico (===)

    ?>
    </div>
</body>
</html>