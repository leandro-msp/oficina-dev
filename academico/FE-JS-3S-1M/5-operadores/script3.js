//operador de incremento

let a;
let saida = document.getElementById("saida");
a=parseInt(prompt("Digite um número"));//10
saida.innerHTML+="<br>a final ="+ a;//10
a++;//11 -> pós incremento
a++;//12
++a;//13 -> pré incremento
++a;//14
saida.innerHTML+="<br>a final ="+ a;//14
a--;//13 -> pós decremento
a--;//12
--a;//11 -> pré incremento
saida.innerHTML+="<br>a final ="+ a;