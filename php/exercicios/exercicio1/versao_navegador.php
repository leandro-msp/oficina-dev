<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto 1</title>
</head>
<body>
    <h4>Projeto 1 - PHP</h4>
    <h2>Recuperando Dados</h2>
    <form method="post" action="projBrowser.php">
     Escreva seu nome: <input type="text" name="nome"><br>
     Digite sua idade: <input type="number" name="idade" min="1"><br>
     Digite sua profissão: <input type="text" name="profissao"><br>
     <input type="submit" value="Enviar!">
    </form>
        <?php

            $nome = ucwords($_POST["nome"]); //aplica tratamento de toda primeira letra de cada palavra ser maiúscula
            $idade = $_POST["idade"]; 
            $profissao = strtolower($_POST["profissao"]); // aplica tratamento todas as letras minúsculas
    
        if (empty($nome) || empty($idade) || empty($profissao)){ 
            echo "Preencha todos os campos:";}
        else{
        echo "$nome é $profissao e tem $idade anos de idade.\n";}
        
        ?>
    
</body>
</html>