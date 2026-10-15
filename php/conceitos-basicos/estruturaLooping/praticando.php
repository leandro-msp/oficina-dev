<?php 
// for
    
    echo "Lista de Frutas:<br>";
    echo "<h3>For</h3>";
    $frutas =["Laranja","Maça","Uva","Melância"];

    for($i=0;$i<count($frutas);$i++){
        echo $frutas[$i]."<br>";
    }

    echo "<hr>";
    echo "<h3>While</h3>";
    $voltas = 0;
    while($voltas<count($frutas)){
        echo "$frutas[$voltas]<br>";
        $voltas++;
    }

    echo "<hr>";
    echo "<h3>Foreach</h3>";

    foreach($frutas as $fruta){
        echo "$fruta<br>";
    }

    echo "<hr>";

    //lista de alunos

    echo "Lista de Alunos:<br>";
    echo "<h3>For</h3>";

    $alunos = [
        ["RA" => 112345678, "nome" => "Leandro Marc" ],
        ["RA" => 123456789, "nome" => "Julia Rodrigues"],
        ["RA" => 234567890, "nome" => "Millene Silva"],
        ["RA" => 345678901, "nome" => "Gustavo Xavier"],
        ["RA" => 456789012, "nome" => "Aluoní Iune"],
        ["RA" => 567890123, "nome" => "Vitória Eduarda"],
        ["RA" => 678901234, "nome" => "Pedro Henrique"]
    ];

    for ($qtd=0;$qtd<count($alunos);$qtd++){
        echo "Aluno:<br>"."RA: ".$alunos[$qtd]['RA']."<br>Nome: ".$alunos[$qtd]['nome']."<hr>";
    }

    echo "<h3>While</h3>";

    $giro = 0;
    while($giro<count($alunos)){
         echo "Aluno:<br>"."RA: ".$alunos[$giro]['RA']."<br>Nome: ".$alunos[$giro]['nome']."<hr>";
         $giro++;
    }

    echo "<h3>Foreach</h3>";

    foreach($alunos as $aluno => $valor){
         echo "Aluno:<br>"."RA: ".$valor['RA']."<br>Nome: ".$valor['nome']."<hr>";
    }


    echo "<h3>Alunos + Notas</h3>";

    
    $media = [
        ["RA" => 112345678, "nome" => "João", "nota" => 8 ],
        ["RA" => 123456789, "nome" => "Kaique", "nota" => 7],
        ["RA" => 234567890, "nome" => "Leticia", "nota" => 3],
        ["RA" => 345678901, "nome" => "Catia", "nota" => 9],
        ["RA" => 456789012, "nome" => "Fabrício", "nota" => 5],
        ["RA" => 567890123, "nome" => "Mateus", "nota" => 10],
        ["RA" => 678901234, "nome" => "Rafaela", "nota" => 6]
    ];

    for($aluno=0;$aluno<count($media);$aluno++){
        echo "RA: ".$media[$aluno]['RA']."<br>Nome: ".$media[$aluno]['nome']."<br>Média: ".$media[$aluno]['nota'];
        if($media[$aluno]['nota']>=6){
            echo "<br>Este aluno está aprovado!<hr>";
        }else{
            echo "<br>Este aluno foi reprovado!<hr>";
        }
    }

?>