 let saida = document.getElementById('saida');
    for (let i = 1; i <= 50; i++) {
        if (i % 3 === 0) {
            continue;                // pula os múltiplos de 3
        } 
        if (i === 8) {
            break;                   // encerra o laço no 8
        }
        saida.innerHTML += `${i} `;
    }
    saida.innerHTML += '<br>Fim do laço.';

/*a função continue faz com que o laço continue, ou seja, ele não executa o que está abaixo do continue e volta para a próxima iteração do laço.

Essa função continue é últi quando se quer pular uma análise de um determinado valor, como no exemplo acima, que pula os múltiplos de 3.
*/