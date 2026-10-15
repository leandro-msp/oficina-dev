/*
Digitar um número inteiro
Mostrar o número digitado e informar
se o número é PAR ou ÍMPAR
Usando ternário
Detalhe, a saída deverá ser direcionada para o teste
Pergunta: 7.8 é PAR ou ÍMPAR????
Pergunta: como mudar a cor de fundo da página
para cinza, usando JS
*/
const teste = document.querySelector(".teste");
const num = parseInt(prompt("Digite um número inteiro"));
let msg = (num%2==0)?"PAR":"ÍMPAR";
teste.innerHTML=`O Número ${num} é ${msg}`;
teste.style.color="pink"; /*alterando a cor do elemento cujo a classe é "teste" */
document.querySelector("body").style.backgroundColor="gray"; /*manipulando a cor do background de td página */
