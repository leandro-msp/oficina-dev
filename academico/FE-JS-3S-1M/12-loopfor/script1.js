    let saida = document.getElementById('saida');
    let tabuada = 2; // valor da tabuada que será exibida

    saida.innerHTML += 'Regressiva: ';
    for (let i = 5; i >= 1; i--) {
        saida.innerHTML += `${i} `;
    }

    saida.innerHTML += '<br>De 2 em 2: ';
    for (let i = 0; i <= 10; i += 2) {
        saida.innerHTML += `${i} `;
    }

    saida.innerHTML += `<br>Tabuada do ${tabuada}:<br>`;
    for (let i = 1; i <= 10; i++) {
        saida.innerHTML += `${tabuada} x ${i} = ${tabuada * i}<br>`;
    }