/*
Criar todas as tabuadas do 1 ao 10

*/
let saida = document.getElementById('saida');
let tabuada = 1;

for(tabuada=1;tabuada<=10;tabuada++){
saida.innerHTML += `<br>Tabuada do ${tabuada}:<br>`;
for (let i = 1; i <= 10; i++) {
    saida.innerHTML += `${tabuada} x ${i} = ${tabuada * i}<br>`;
}
}
