saida = document.querySelector("#saida");
const av1 = parseInt(prompt("Digite a nota AV1:"));
const av2 = parseInt(prompt("Digite a nota AV2:"));

let media;
media = (av1+av2)/2;

saida.innerHTML= "AV1: "+ av1.toFixed(1);
saida.innerHTML+= "<br>AV2: "+ av2.toFixed(1);

saida.innerHTML+= "<br>A média foi: " + media.toFixed(2);

//mostra o valor da casa decimal

