<?php
    # Recuperando dados dos alunos dentro do array

    // listar cada um dos alunos contendo RA, Nome e Nota. E conforme a nota tirada informar se foi aprovado ou reprovado.
    
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

    for($aluno=0;$aluno<count($media);$aluno++){ // para cada index da lista haverá uma listagem
        echo "RA: ".$media[$aluno]['RA']."<br>Nome: ".$media[$aluno]['nome']."<br>Média: ".$media[$aluno]['nota'];
        // recuperando valores por chave
        if($media[$aluno]['nota']>=6){// filtragem por nota para informar se o aluno foi aprovado ou reprovado
            echo "<br>Este aluno está aprovado!<hr>";
        }else{
            echo "<br>Este aluno foi reprovado!<hr>";
        }
    }



?>