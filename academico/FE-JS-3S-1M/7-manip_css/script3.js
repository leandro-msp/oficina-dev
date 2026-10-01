/*Solicitar a difitação de uma cor
Mostrar a msg:
a cor difinida foi : red
Apenas a cor deverá receber a cor */

const saida = document.querySelector('#saida');
const cor = prompt("Digite uma cor:");

saida.innerHTML=`a cor definida foi: <p style="color:${cor};">${cor}</p>`; /* a tag é interpretada */
                            





