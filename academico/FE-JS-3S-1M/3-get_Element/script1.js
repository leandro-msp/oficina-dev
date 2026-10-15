document.write("Script1"); // comando de saída de texto
alert("ALERTA\n!!!"); // caixa de diáloho pop-up
console.log("Onde Estou?");// comando de saída dentro da aba console do navegador



document.getElementById("saida").innerHTML="<br>Funciona?"; //escreve, sobrepõe dentro da tag que possui o id='saida'
// get element só funciona se tiver id
document.getElementById("saida").innerHTML+="<hr>Good Morno!!"
// ao adicionar o sinal de "+" junto ao sinal de atribuição (innerHTML+=), acontece uma concatenação, junta o novo valor ao anterior, sendo assim não sobrepõe e sim adiciona.

document.querySelector(".teste").innerHTML="classe";
// Quando se coloca o ponto ".", está indicando que é uma class (.teste)

document.querySelector("#saida").innerHTML="id";
// para trabalhar com id utiliza-se o hashtag (#)

document.querySelector("h1").innerHTML+="-JavaScript";
// para manipular tag basta somente inserir o nome da tag
