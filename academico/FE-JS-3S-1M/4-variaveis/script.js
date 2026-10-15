// VARIÁVEIS

// método explícito :
let nome_Cliente;

nome_Cliente = "João da Silva";

//método implícito

let nome_Cliente2 = "João da Silva";

// métodos errados de declaração

/*
let 3nome; -> não pode começar com numero
let if; ->  não pode usar palavras reservadas
let nome completo; -> não pode ter espaços em branco
let @idade; -> 
*/


let oct = 0o10; // octal
let bin = 0b10; // binario
let hexa = 0x10; // hexadecimal
let dia, nota;
dia = 10;
nota = 9.7; // na notacao americana, valores float é de denominado com ponto e não virgula
let saida = document.getElementById("saida");
saida.innerHTML="nota: "+nota;
saida.innerHTML+="<br>dia: "+dia;
saida.innerHTML+="<br>oct: "+oct;
saida.innerHTML+="<br>bin: "+bin;
saida.innerHTML+="<br>hexa: "+hexa;
let cep="01012123"; // todo numero que começa por zero, nn pode ser representado por numero inteiro, e sim como string, pois o interpretador irá recuperar valor octal
saida.innerHTML+="<br>cep: "+cep; 
let mes,ano;
mes = 9;
ano = 2026;
ano = 2027;

//data:10/09/2026
saida.innerHTML+= "<br>Data: "+dia+"/"+mes+"/"+ano;

const PI = 3.14;
const TAG = "<hr>";
let x,y;
x =  PI +2;
x = PI;
// PI = 5; constante nn pode mudar o valor 

saida.innerHTML+= TAG+"X= "+x;