let saida= document.getElementById("saida"); // primeira variavel que deve ser declarada ao criar o arquivo
const n1 = parseInt(prompt("Digite o primeiro número: "));
const n2 = parseInt(prompt("Digite o segundo número: "));
// toda entrada de dados é do tipo string
let resultado;
resultado = n1+n2;
 
saida.innerHTML = "<br>N1: "+n1;
saida.innerHTML += "<br>N2: "+n2;
saida.innerHTML +="<br> Resultado: "+resultado;

// converte tipo de dados

// parseInt
//parseFloat
//Number
//typeof -> ver o tipo de dado

