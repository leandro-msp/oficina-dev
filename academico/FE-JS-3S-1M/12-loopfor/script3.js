/*
i j
2 0
2 1
2 2
2 3
3 0
3 1
3 2
3 3
*/

let saida = document.getElementById('saida');
for (let i = 2; i < 4; i++) {   //externo       // laço de fora: 4 voltas
    for (let j = 0; j < 4; j++) { //interno    // laço de dentro: 3 voltas por volta de fora
        saida.innerHTML += `${i} ${j}<br>`;
    }
}