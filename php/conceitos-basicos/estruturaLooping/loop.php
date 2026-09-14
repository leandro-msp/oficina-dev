<?php  
# Estruturas de repetição
echo "<h2>Laço for</h2><hr>";

$pessoas = [
    ['id' => 1, 'nome' => 'Leandro'], #índice 0
    ['id' => 2, 'nome' => 'Carlos'],  #índice 1
    ['id' => 3, 'nome' => 'Adinan'], #índice 2
    ['id' => 4, 'nome' => 'Nicholas'] #índice 3

];
 

// qual seria o método convencional, s/utilizaçã do loop:
echo "Método convencional:<br>";
echo "ID: ".$pessoas[0]['id']."<br>"; // [0] > refere-se primeira linha, ['id'] qual campo a ser lido
echo "Usuário: ".$pessoas[0]['nome']."<hr>";

//LAÇO FOR
/*  possui 3 parâmetros , 1º uma variavel que amarzenar valores, e a necssidade define o valor que ela inicia, neste caso 0
    2º Condição, o laço vai rodar enquanto essa condição for verdadeira,
    3º Incremento, toda vez q o laço rodar ele vai acrescentar um valor na variável inicial
*/ 
echo "Método utilizando laço For:<br>";
for ($i=0;$i<2;$i++){
    echo "O laço rodou $i vezes<br>";

   }
echo "<hr>";     

for ($i=0;$i<count($pessoas);$i++){
    echo "ID:". $pessoas[$i]['id']."<br>Usuário: ". $pessoas[$i]['nome']."<hr>";
    // neste cenário foi de sumar importância iniciar a variável com valor 0, pois estamos resgatando índices, que imutávelmente começam por 0.
   }     

// Laço While
echo "<h2>Laço While</h2><hr>";

$i=0;
// o laço while(enquanto) vai rodar enquanto a condiçã for verdadeira, no caso abaixo, Enquanto $i for menor que a quantidade pessoas, rodar o laço
while($i<count($pessoas)){
    echo "ID:". $pessoas[$i]['id']."<br>Usuário: ". $pessoas[$i]['nome']."<hr>";
    $i++; // obrigatoriamente devemos colocar o incremento, ou a devida instrução para que em algum momento o loop finalize.

}

// Laço Foreach
echo "<h2>Laço Foreach</h2><hr>";

foreach($pessoas as $chave => $valor){
    echo "ID:". $valor['id']."<br>Usuário: ". $valor['nome'].", e está armazenado no índice $chave"."<hr>";

}

?>