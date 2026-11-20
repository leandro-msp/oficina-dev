   let saida = document.getElementById('saida');
   let i; // desta forma a variável i fica visível fora do bloco for, ou seja, ela é global. Se fosse declarada com let dentro do for, ela seria visível apenas dentro do bloco for.
    for (i = 0; i <= 5; i++) {
        saida.innerHTML += `Número: ${i}<br>`;
    }
    saida.innerHTML += `Valor que torna a cond falsa: ${i}<br>`;