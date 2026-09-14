<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cálculo de Desconto</title>
</head>
<body>
    <h4>Projeto 2 - PHP</h4>
    <h2 style="color: crimson;">Cálculo de Desconto</h2>
        <form method="post" action="versao_navegador.php">
            Valor do Produto <input type="number" name="valor">
            <input type="submit" value="Calcular">
        </form>

            <?php
            
                $valor_produto = floatval($_POST["valor"]);
                $desc1=0.15;
                $desc2=0.05;

                    if(empty($valor_produto)){
                    echo "Informe o valor do produto!!<br>";
                    }else{
                        if ($valor_produto>100){
                            $valor_final = $valor_produto-($valor_produto*$desc1);
                            echo "Você ganho desconto de 15%, o valor final da compra é: R$". number_format($valor_final,2);

                        }elseif($valor_produto<=100){
                            $valor_final = $valor_produto-($valor_produto*$desc2);
                            echo "Você ganho desconto de 5%, o valor final da compra é: R$". number_format($valor_final,2);
                        }else{
                            echo "Valor inválido";

                        }
                    }
        
        
            ?>
    
</body>
</html>