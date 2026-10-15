let saida;
saida = document.getElementById("saida")

/* Solicitar a digitação do num1 e num2
mostrar o resultado de todas as comparações
entre os dois numeros digitados*/

let num1,num2;

num1 = parseInt(prompt("Digite o primeiro número: "));
num2 = parseInt(prompt("Digite o segundo número: "));

saida.innerHTML = "Número 1 = "+ num1;
saida.innerHTML += "<br>Número 2 = "+ num2;

saida.innerHTML += "<h2>Igual, Idêntico , Diferente, e Não Idêntico<h2>";

saida.innerHTML +="<br>Os valores digitados são iguais?: "+(num1==num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>Os valores digitados são idênticos?: "+ (num1===num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>Os valores digitados são diferentes?: "+ (num1!=num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>Os valores digitados são não idênticos?: "+ (num1!==num2);
saida.innerHTML += "<hr>";

/*Maior, menor, maior igual e menor igal*/
saida.innerHTML += "<h2>Maior, Menor, Maior igual e Menor Igual<h2>";

saida.innerHTML += "<br>O num1 é maior que num2? "+ (num1>num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>O num1 é menor que num2? "+ (num1<num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>O num1 é maior ou igual ao  num2? "+ (num1>=num2);
saida.innerHTML += "<hr>";
saida.innerHTML += "<br>O num1 é menor ou igual ao num2? "+ (num1<=num2);
