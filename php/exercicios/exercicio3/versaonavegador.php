<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício - Par ou Ímpar</title>
    <style>
        body {background-color: dimgray;}
        .texto{
            color: white;
        }

    </style>
</head>
<body>
    <h4 class="texto">Projeto 3 - PHP</h4>
    <h2 class="texto">Par ou Ímpar</h2>
    <form method="post" action="versaonavegador.php">
        <label class="texto"> Digite um número </label> <input type="number" name="numero" min="1">
        <input type="submit" value="Verificar">
    </form>
       <div class="texto">     
        <?php
            $numero= intval($_POST["numero"]);

                if($numero%2==0){
                    echo "O Número digitado foi $numero, portanto é par.";
    
                }else{
                    echo "O Número digitado foi $numero, portanto é ímpar.";
                    
                }
        ?>
       </div>
</body>
</html>