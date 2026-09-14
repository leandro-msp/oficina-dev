<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>If e Else</title>

    <style>
        * { padding: 0; margin: 0; box-sizing: border-box;}
        body{ background-color: #282632;}
        .cmd{ color: #33FE00; padding: 20px;}
    </style>

</head>
<body>
    <div class="cmd">
    <?php

    # ESTRUTURA DE CONTROLE/CONDIÇÃO

    // If e Else

    $aluno = "Lucas";
    $nota1 = 8;
    $nota2 = 4;
    $media =  ($nota1+$nota2)/2;

    if ($media>=6){
        echo "Parabéns $aluno você foi aprovado com a média $media"; 
    }
    else {
        echo"Infelizmente você foi reprovado com a média $media";
    }
    
    echo "<hr>";
    $aluno = "Mateus";
    $nota1 = 3;
    $nota2 = 2;
    $media =  ($nota1+$nota2)/2;

    if ($media>=6){
        echo "Parabéns $aluno sua média foi aprovada";
    } elseif ($media>=3 && $media<6) {
        echo "$aluno, infelizmente você foi reprovado com a média $media";
    } else{
        echo "$aluno, infelizmente você foi reprovado, e tirou uma média muito abaixo do requisitado para recuperação. Sendo assim, terá que refazer o semestre! ";
    }
     echo "<hr>";

    # método para integrar a estrura de controle com HTML

    // endif
    $logado = true;
    if ($logado):?>
        <h3> Usuário logado com sucesso! Bem-Vindo</h3> <!-- válido para trechos grandes em html-->
    <?php else: ?>
        <h3>é necessário fazer o login</h3>
    <?php endif ?>
    </div>
</body>
</html>