let a,b;
let saida = document.getElementById("saida");
a=10;
b="10";
saida.innerHTML="Igualdade = "+(a==b)+"<br>"; // true
saida.innerHTML+="Idêntico = "+(a===b)+"<br>"; //false
saida.innerHTML+="Não igual = "+(a!=b)+"<br>"; // false
saida.innerHTML+="Não Idêntico = "+(a!==b)+"<br>"; // true