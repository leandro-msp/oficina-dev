<?php 
/* Enunciado do Programa:

Faça um programa que receberá o valor de um produto como entrada.

Se o valor do produto for maior que 100, o programa deverá calcular e aplicar um desconto de 15% ao produto.

Se o valor do produto for menor ou igual a 100, o programa deverá aplicar um desconto de 5% ao produto.

*/

$metodo = (int)readline("Escolha o método que deseja utilizar, 1, 2 ou 3: "); // a escolha do método é apenas para cortar a necessidade de rodar os 3 métodos elaborados para o exercício
// para o usuário isso não teria relevância, pois ele nn precisa saber o que ocorre atrás dos panos, somente que a operação seja feita
    while ($metodo!= 1 && $metodo !=2 && $metodo!=3){
        $metodo = (int)readline("Operação inválida, escolha somente as disponíveis 1, 2 ou 3: ");
        }
        
switch($metodo){
    case 1:
        # método1 
        echo "Método 1\n";
        echo "Insira o valor do produto:";
        $valor_prod = (float)readline();

        if($valor_prod>100){
            $valor_prod = $valor_prod-($valor_prod*0.15);
            echo "Você ganhou 15% de desconto, o valor final é: R$". number_format($valor_prod,2)."\n";
        }elseif ($valor_prod<=100){
            $valor_prod = $valor_prod-($valor_prod*0.05);
            echo "Você ganhou 5% de desconto, o valor final é: R$". number_format($valor_prod,2)."\n";
        }else{
            echo "Nenhum valor inserido!\n";
        }
    break;

    case 2:
        #método2
        echo "Método 2\n";
        echo "Insira o Valor da produto: ";
        $valor_compra = (float)readline();

        if ($valor_compra>100){
            $desconto1 = $valor_compra * 0.15;
            $valor_final = $valor_compra - $desconto1;
            echo "Você ganhou 15% de desconto, o valor final da compra é: R$". number_format($valor_final,2)."\n"; 
                                                                            # number formata possui 2 paramentros, o valor a ser formato, e qual a formatação, neste caso, duas casas decimais
        } elseif($valor_compra<=100){
            $desconto2 = $valor_compra*0.05;
            $valor_final = $valor_compra - $desconto2;
            echo "Você ganhou 5% de desconto, o valor final da compra é: R$".number_format($valor_final,2)."\n";
        }else {
            echo "Nenhum valor inserido!\n";
        }
        break;

        case 3:
            #método 3
            echo "Método 3\n";
            echo "\nInsira o Valor do Produto:";
            $valor_produto = (float)readline();
            $desc1 = 0.15;
            $desc2 = 0.05;

            if ($valor_produto>100){
                $total_compra = $valor_produto-($valor_produto*$desc1);
                echo "Você ganhou 15% de desconto, o total da compra é: R$".number_format($total_compra,2)."\n";
            } elseif($valor_produto<=100){
                $total_compra = $valor_produto-($valor_produto*$desc2);
                echo "Você ganhou 5% de desconto, o total da compra é: R$".number_format($total_compra,2)."\n";
            }else{
                echo "Nenhum valor foi Inserido!\n";
            }
        break;

        default:
            echo "Operação Inválida"; # no caso nunc vai cair no default, pois foi definido que a operação só inicia caso digite um dos métodos disponíveis
}
?>